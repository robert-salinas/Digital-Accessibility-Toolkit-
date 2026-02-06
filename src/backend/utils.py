import json
import os
from typing import Dict

LOCALIZATION_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "localization")

def load_translations(lang: str = "es") -> Dict[str, str]:
    file_path = os.path.join(LOCALIZATION_DIR, f"{lang}.json")
    if not os.path.exists(file_path):
        file_path = os.path.join(LOCALIZATION_DIR, "es.json") # Default to Spanish
        
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def translate(key: str, lang: str = "es", **kwargs) -> str:
    translations = load_translations(lang)
    text = translations.get(key, key)
    if kwargs:
        return text.format(**kwargs)
    return text
