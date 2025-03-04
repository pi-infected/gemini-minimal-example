from google import genai
from gemini_ai import GeminiClient
from pydantic import BaseModel

api_key = "<your-api-key>"
client = genai.Client(api_key=api_key)

document_test = """
Curriculum Vitae de Sophie Dubois

Informations personnelles:
Nom: Sophie Dubois
Date de naissance: 15 avril 1988
Adresse: 45 rue des Lilas, 75011 Paris
Email: sophie.dubois@email.com
Téléphone: 06 12 34 56 78

Formation:
- Doctorat en Biologie Moléculaire, Université Paris-Saclay (2015)
- Master en Sciences Biomédicales, Université de Lyon (2012)
- Licence en Biologie, Université de Bordeaux (2010)

Expérience professionnelle:
Depuis 2018: Chercheuse principale, Institut Pasteur, Paris
2015-2018: Post-doctorante, CNRS, Strasbourg
2012-2015: Assistante de recherche (pendant doctorat), Université Paris-Saclay

Compétences:
- PCR, séquençage génétique, culture cellulaire
- Analyse de données biologiques
- Rédaction scientifique
- Gestion d'équipe de recherche
"""


prompt = f"""Ton but est d'extraire les informations suivantes du document:
- le nom de la personne
- son niveau d'éducation
- ses compétences

Voici le document de test:
'''
{document_test}
'''

Tu retourneras un JSON valide, formaté de la manière suivante :"""+"""
{
  "name": "<ici, tu écriras le nom de la personne, ou null si tu n'en trouves pas>",
  "education": "<ici, tu écriras le niveau d'éducation, ou null si tu n'en trouves pas>",
  "skills": [
    "skill 1",
    "skill 2",
    "skill 3",
    ...
  ] ou null si tu n'en trouves pas
}
"""

class Person(BaseModel):
  name: str | None
  education: str | None
  skills: list[str] | None

gemini_client = GeminiClient(client)
person = gemini_client.generate_json(prompt, schema_model=Person)

print(person)
