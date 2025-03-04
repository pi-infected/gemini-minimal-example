from utils import decode_json
from google.genai import types
from time import sleep
from pydantic import BaseModel, ValidationError
from typing import Type, Union, List, Optional

# Implémentation de la génération JSON avec Gemini avec :
# - gestion des erreurs de rate limit
# - délai exponentiel entre les tentatives
# - décodage de JSON même malformé
# - validation du JSON avec Pydantic
class GeminiClient:
  def __init__(self, client):
    self._client = client
  
  def generate_json(
    self,
    messages: Union[str, List[str]],
    schema_model: Type[BaseModel],
    model: str = 'gemini-2.0-flash',
    max_tokens: Optional[int] = 500,
    creative_writing: bool = False,
    system_prompt: Optional[str] = None,
    max_retries: int = 3
  ) -> BaseModel:
    params = {
      'response_mime_type': 'application/json',
      'max_output_tokens': max_tokens
    }
    
    if system_prompt:
      params['system_instruction'] = system_prompt
    if creative_writing:
      params['temperature'] = 1.2
      params['top_p'] = 0.9
    else:
      params['temperature'] = 0.7
      params['top_p'] = 0.7
    
    retry_count = 0
    base_delay = 10
    
    while retry_count <= max_retries:
      try:
        response = self._client.models.generate_content(
          model=model,
          contents=messages,
          config=types.GenerateContentConfig(**params),
        )
        result = decode_json(response.text)
        
        # Validation avec le modèle Pydantic
        validated_data = schema_model.model_validate(result)
        return validated_data
        
      except ValidationError as e:
        raise ValueError(f"Le JSON ne correspond pas au schéma défini : {e}")
      except Exception as e:
        if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):
          if retry_count >= max_retries:
            raise ValueError(f"Nombre maximum de tentatives atteint ({max_retries})")
          
          wait_time = base_delay * (2 ** retry_count)  # Calcul exponentiel du délai
          print(f"Rate limit atteint (429), nouvelle tentative dans {wait_time} secondes... (tentative {retry_count+1}/{max_retries})")
          sleep(wait_time)
          retry_count += 1
        else:
          print(f"Une erreur est survenue : {type(e).__name__}: {e}")
          raise