from backend.translation_engine.py import TranslationEngine

class ResponseGenerator:
    def __init__(self):
        self.translator = TranslationEngine()

    def generate_response(self, query: str) -> dict:
        translated = self.translator.translate_to_english(query)
        # More complex logic can be added here

        response_data = {
            "original_query": query,
            "translated_query": translated,
            "response": f"Received and translated your query: {translated}"
        }
        return response_data
