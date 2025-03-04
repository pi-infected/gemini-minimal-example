# Gemini Minimal Example

Ce projet est un exemple minimal d'utilisation robuste de l'API Gemini de Google pour extraire des informations structurées d'un texte. Il utilise un CV comme exemple pour extraire le nom, le niveau d'éducation et les compétences de la personne, et retourne ces informations dans un format JSON validé par Pydantic.

## Installation de Python

### Windows
1. Téléchargez Python depuis [python.org](https://www.python.org/downloads/windows/)
2. Lancez l'installateur
3. **Important**: Cochez la case "Add Python to PATH" pendant l'installation
4. Vérifiez l'installation en ouvrant un terminal (cmd) et en tapant:
   ```bash
   python --version
   ```

### macOS
1. Installez Homebrew si ce n'est pas déjà fait:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Installez Python:
   ```bash
   brew install python
   ```
3. Vérifiez l'installation:
   ```bash
   python3 --version
   ```

### Linux (Ubuntu/Debian)
1. Python est généralement pré-installé. Si ce n'est pas le cas:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```
2. Vérifiez l'installation:
   ```bash
   python3 --version
   ```

## Installation des dépendances

1. Clonez ce repository:
   ```bash
   git clone https://github.com/votre-username/gemini-minimal-example.git
   cd gemini-minimal-example
   ```

2. Installez les dépendances:
   ```bash
   # Windows
   pip install -r requirements.txt

   # macOS/Linux
   pip3 install -r requirements.txt
   ```

## Configuration

1. Obtenez une clé API Gemini depuis [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Remplacez `<your-api-key>` dans `example.py` par votre clé API

## Exécution du script de test

```bash
python example.py
```

ou

```bash
python3 example.py
```

## Résultat attendu

```json
{
  "name": "Sophie Dubois",
  "education": "Doctorat en Biologie Moléculaire",
  "skills": ["PCR", "séquençage génétique", "culture cellulaire", "Analyse de données biologiques", "Rédaction scientifique", "Gestion d'équipe de recherche"]
}
```

## Notes
- Mettez votre clé API dans le fichier `example.py`