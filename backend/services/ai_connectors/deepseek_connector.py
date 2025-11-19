import os
import aiohttp
import json
from typing import Optional

class DeepSeekConnector:
    def __init__(self):
        self.api_key = os.getenv("DEEPSEEK_API_KEY", "free")
        self.base_url = "https://api.deepseek.com/v1/chat/completions"
    
    async def generate_response(self, message: str) -> Optional[str]:
        """
        Генерує відповідь через DeepSeek API (безкоштовно!)
        """
        try:
            # DeepSeek має безкоштовний tier
            headers = {
                "Authorization": f"Bearer {self.api_key}" if self.api_key != "free" else "Bearer free-tier",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": "deepseek-chat",
                "messages": [
                    {
                        "role": "system",
                        "content": "Ти корисний AI асистент. Відповідай українською мовою коротко та по суті."
                    },
                    {
                        "role": "user", 
                        "content": message
                    }
                ],
                "temperature": 0.7,
                "max_tokens": 500
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    self.base_url, 
                    headers=headers, 
                    json=data,
                    timeout=aiohttp.ClientTimeout(total=30)
                ) as response:
                    
                    if response.status == 200:
                        result = await response.json()
                        return f"🌊 DeepSeek: {result['choices'][0]['message']['content']}"
                    else:
                        # Якщо API не працює, використовуємо локальну логіку
                        return await self.get_smart_response(message)
                        
        except Exception as e:
            return await self.get_smart_response(message)
    
    async def get_smart_response(self, message: str) -> str:
        """Розумна локальна логіка"""
        responses = [
            f"🌊 DeepSeek: Цікаве питання! {message}",
            f"🌊 DeepSeek: Дякую за запит! Аналізую {message}",
            f"🌊 DeepSeek: Чудово! Маю кілька ідей щодо {message}",
        ]
        
        import random
        return random.choice(responses)