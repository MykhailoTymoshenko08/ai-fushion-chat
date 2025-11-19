import os
import random
from typing import Optional

class OpenAIConnector:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY", "free-mode")
    
    async def generate_response(self, message: str) -> Optional[str]:
        """
        Безкоштовний режим - не використовує реальний API
        """
        try:
            responses = [
                f"🎯 OpenAI (тестовий): Аналізую '{message}'...",
                f"🎯 OpenAI (тестовий): '{message}' - цікаве питання!",
                f"🎯 OpenAI (тестовий): Для реальних відповідей додайте API ключ",
                f"🎯 OpenAI (тестовий): Обробляю ваш запит про '{message}'"
            ]
            return random.choice(responses)
            
        except Exception as e:
            return f"❌ Помилка OpenAI: {str(e)}"