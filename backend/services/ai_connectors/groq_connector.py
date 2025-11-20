# import os
# import aiohttp
# import json
# from typing import Optional

# class GroqConnector:
#     def __init__(self):
#         self.api_key = os.getenv("GROQ_API_KEY")
#         self.base_url = "https://api.groq.com/openai/v1/chat/completions"
    
#     async def generate_response(self, message: str) -> Optional[str]:
#         """
#         Генерує відповідь через реальне Groq API (безкоштовно!)
#         """
#         try:
#             # Якщо немає ключа, повертаємо тестову відповідь
#             if not self.api_key:
#                 return f"🚀 Groq: {message} [Потрібен API ключ]"
            
#             headers = {
#                 "Authorization": f"Bearer {self.api_key}",
#                 "Content-Type": "application/json"
#             }
            
#             # ОНОВЛЕНІ МОДЕЛІ - актуальні на 2024
#             available_models = [
#                 "llama-3.1-8b-instant",    # 🆕 Нова швидка модель
#                 "llama-3.1-70b-versatile", # 🆕 Потужна модель
#                 "mixtral-8x7b-32768",      # 🎯 Надійна модель
#                 "gemma2-9b-it"             # 🔮 Нова модель від Google
#             ]
            
#             # Використовуємо першу доступну модель
#             model = available_models[0]
            
#             data = {
#                 "messages": [
#                     {
#                         "role": "system",
#                         "content": "Ти корисний AI асистент. Відповідай українською мовою. Будь ласка, будь корисним та інформативним. Відповідай коротко та по суті."
#                     },
#                     {
#                         "role": "user", 
#                         "content": message
#                     }
#                 ],
#                 "model": model,
#                 "temperature": 0.7,
#                 "max_tokens": 1024,
#                 "top_p": 1,
#                 "stream": False
#             }
            
#             print(f"🔧 Використовуємо модель: {model}")
            
#             async with aiohttp.ClientSession() as session:
#                 async with session.post(
#                     self.base_url, 
#                     headers=headers, 
#                     json=data,
#                     timeout=aiohttp.ClientTimeout(total=30)
#                 ) as response:
                    
#                     if response.status == 200:
#                         result = await response.json()
#                         return f"🚀 Groq ({model}): {result['choices'][0]['message']['content']}"
#                     else:
#                         error_text = await response.text()
#                         print(f"❌ Помилка Groq: {error_text}")
                        
#                         # Спробуємо іншу модель якщо перша не працює
#                         if "model_decommissioned" in error_text or "model_not_found" in error_text:
#                             return await self.try_alternative_models(message, available_models[1:])
#                         else:
#                             return f"❌ Помилка Groq ({response.status}): {error_text}"
                        
#         except aiohttp.ClientError as e:
#             return f"❌ Помилка мережі Groq: {str(e)}"
#         except asyncio.TimeoutError:
#             return "❌ Таймаут запиту до Groq"
#         except Exception as e:
#             return f"❌ Помилка Groq: {str(e)}"
    
#     async def try_alternative_models(self, message: str, alternative_models: list) -> str:
#         """
#         Спробуємо альтернативні моделі якщо основна не працює
#         """
#         if not alternative_models:
#             return "❌ Жодна з моделей Groq не працює. Спробуйте пізніше."
        
#         headers = {
#             "Authorization": f"Bearer {self.api_key}",
#             "Content-Type": "application/json"
#         }
        
#         for model in alternative_models:
#             try:
#                 print(f"🔧 Спробуємо модель: {model}")
                
#                 data = {
#                     "messages": [
#                         {
#                             "role": "system",
#                             "content": "Ти корисний AI асистент. Відповідай українською мовою."
#                         },
#                         {
#                             "role": "user", 
#                             "content": message
#                         }
#                     ],
#                     "model": model,
#                     "temperature": 0.7,
#                     "max_tokens": 512
#                 }
                
#                 async with aiohttp.ClientSession() as session:
#                     async with session.post(
#                         "https://api.groq.com/openai/v1/chat/completions", 
#                         headers=headers, 
#                         json=data,
#                         timeout=aiohttp.ClientTimeout(total=20)
#                     ) as response:
                        
#                         if response.status == 200:
#                             result = await response.json()
#                             return f"🚀 Groq ({model}): {result['choices'][0]['message']['content']}"
#                         else:
#                             continue  # Спробуємо наступну модель
                            
#             except Exception:
#                 continue  # Спробуємо наступну модель
        
#         return "❌ Усі моделі Groq тимчасово недоступні. Спробуйте пізніше."













import os
import aiohttp
from typing import Optional

class GroqConnector:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.base_url = "https://api.groq.com/openai/v1/chat/completions"
    
    async def generate_response(self, message: str) -> Optional[str]:
        """
        Генерує відповідь через реальне Groq API
        """
        # 🔍 ДЕБАГ: перевірка ключа
        print(f"🔑 Groq API Key: {self.api_key}")
        
        try:
            # Перевірка чи ключ валідний
            if not self.api_key or self.api_key == "free-mode":
                return f"🚀 Groq: {message} [Потрібен API ключ в .env файлі]"
            
            # Перевірка формату ключа
            if not self.api_key.startswith("gsk_"):
                return f"🚀 Groq: Неправильний формат API ключа. Ключ має починатись з 'gsk_'"
            
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            available_models = [
                "llama-3.1-8b-instant",
                "llama-3.1-70b-versatile",
                "mixtral-8x7b-32768", 
                "gemma2-9b-it"
            ]
            
            model = available_models[0]
            
            data = {
                "messages": [
                    {
                        "role": "system",
                        "content": "Ти корисний AI асистент. Відповідай українською мовою. Будь ласка, будь корисним та інформативним."
                    },
                    {
                        "role": "user", 
                        "content": message
                    }
                ],
                "model": model,
                "temperature": 0.7,
                "max_tokens": 500,
                "top_p": 1,
                "stream": False
            }
            
            print(f"🔧 Використовуємо модель: {model}")
            print(f"🔧 Відправляємо запит до Groq API...")
            
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    self.base_url, 
                    headers=headers, 
                    json=data,
                    timeout=aiohttp.ClientTimeout(total=30)
                ) as response:
                    
                    print(f"🔧 Статус відповіді: {response.status}")
                    
                    if response.status == 200:
                        result = await response.json()
                        print("✅ Успішна відповідь від Groq API")
                        return f"🚀 Groq ({model}): {result['choices'][0]['message']['content']}"
                    
                    elif response.status == 401:
                        error_text = await response.text()
                        print(f"❌ Помилка автентифікації: {error_text}")
                        return "🚀 Groq: Помилка автентифікації. Перевірте API ключ."
                    
                    elif response.status == 429:
                        error_text = await response.text()
                        print(f"❌ Перевищено ліміт: {error_text}")
                        return "🚀 Groq: Перевищено ліміт запитів. Спробуйте пізніше."
                    
                    else:
                        error_text = await response.text()
                        print(f"❌ Помилка Groq ({response.status}): {error_text}")
                        return f"🚀 Groq: Помилка API ({response.status})"
                        
        except aiohttp.ClientError as e:
            print(f"❌ Помилка мережі: {e}")
            return f"🚀 Groq: Помилка мережі - {str(e)}"
        except asyncio.TimeoutError:
            print("❌ Таймаут запиту")
            return "🚀 Groq: Таймаут запиту. Спробуйте ще раз."
        except Exception as e:
            print(f"❌ Загальна помилка: {e}")
            return f"🚀 Groq: Помилка - {str(e)}"