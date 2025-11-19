class OllamaConnector:
    async def generate_response(self, message: str) -> Optional[str]:
        try:
            return f"🦙 Ollama: {message}. Локальні моделі - ніяких платежів!"
        except Exception as e:
            return f"❌ Помилка Ollama: {str(e)}"