import os
import random
from typing import Optional

class ClaudeConnector:
    def __init__(self):
        self.api_key = os.getenv("ANTHROPIC_API_KEY", "free-mode")
    
    async def generate_response(self, message: str) -> Optional[str]:
        try:
            responses = [
                f"🧠 Claude (тестовий): Аналізую '{message}'...",
                f"🧠 Claude (тестовий): Це цікаве питання для міркувань",
                f"🧠 Claude (тестовий): Для складних аналізів потрібен API ключ",
                f"🧠 Claude (тестовий): Міркую над '{message}'"
            ]
            return random.choice(responses)
        except Exception as e:
            return f"❌ Помилка Claude: {str(e)}"