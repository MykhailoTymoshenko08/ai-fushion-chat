import asyncio
import random
from typing import List, Dict
from services.ai_connectors.groq_connector import GroqConnector
from services.ai_connectors.deepseek_connector import DeepSeekConnector
from services.ai_connectors.huggingface_connector import HuggingFaceConnector

class AIAggregator:
    def __init__(self):
        self.connectors = {
            "groq": GroqConnector(),           # 🚀 Швидкий API
            "deepseek": DeepSeekConnector(),   # 🌊 Безкоштовний та потужний
            "huggingface": HuggingFaceConnector(), # 🤗 Резервний варіант
        }
    
    async def get_ai_responses(self, message: str) -> List[str]:
        """
        Отримує відповіді від всіх доступних AI-провайдерів
        """
        tasks = []
        
        # Створюємо асинхронні задачі для всіх коннекторів
        for connector_name, connector in self.connectors.items():
            task = asyncio.create_task(
                connector.generate_response(message),
                name=connector_name
            )
            tasks.append(task)
        
        # Чекаємо на всі відповіді (з таймаутом)
        try:
            responses = await asyncio.wait_for(
                asyncio.gather(*tasks, return_exceptions=True),
                timeout=45.0
            )
        except asyncio.TimeoutError:
            responses = ["⏰ Час очікування відповіді вийшов"]
        
        # Фільтруємо успішні відповіді
        successful_responses = []
        for response in responses:
            if isinstance(response, str) and response:
                successful_responses.append(response)
            elif isinstance(response, Exception):
                # Можна додати логування помилок тут
                continue
        
        # Якщо немає успішних відповідей, повертаємо заглушку
        if not successful_responses:
            return ["🤖 Наразі сервіси тимчасово недоступні. Спробуйте ще раз!"]
        
        # Перемішуємо відповіді для різноманітності
        random.shuffle(successful_responses)
        return successful_responses
    
    async def get_single_best_response(self, message: str) -> str:
        """
        Повертає одну найкращу відповідь (першу успішну)
        """
        responses = await self.get_ai_responses(message)
        return responses[0] if responses else "🤖 Наразі не можу відповісти"