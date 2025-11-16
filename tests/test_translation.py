import pytest
from backend.translation_engine import TranslationEngine

@pytest.fixture
def translator():
    return TranslationEngine()

def test_translate_to_english(translator):
    # Example test with fixed input
    spanish_text = "Hola, ¿cómo estás?"
    english = translator.translate_to_english(spanish_text)
    assert "how are you" in english.lower()
