import openai
from util.config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

class TranslationEngine:
    def __init__(self):
        pass

    def translate_to_english(self, text: str) -> str:
        prompt = f"Translate the following text to English:\n\n{text}"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            temperature=0.3,
            n=1,
            stop=None
        )
        translated_text = response.choices[0].text.strip()
        return translated_text
