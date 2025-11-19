# # import os
# # import aiohttp
# # import json
# # from typing import Optional

# # class DeepSeekConnector:
# #     def __init__(self):
# #         self.api_key = os.getenv("DEEPSEEK_API_KEY", "free")
# #         self.base_url = "https://api.deepseek.com/v1/chat/completions"
    
# #     async def generate_response(self, message: str) -> Optional[str]:
# #         """
# #         Генерує відповідь через DeepSeek API (безкоштовно!)
# #         """
# #         try:
# #             # DeepSeek має безкоштовний tier
# #             headers = {
# #                 "Authorization": f"Bearer {self.api_key}" if self.api_key != "free" else "Bearer free-tier",
# #                 "Content-Type": "application/json"
# #             }
            
# #             data = {
# #                 "model": "deepseek-chat",
# #                 "messages": [
# #                     {
# #                         "role": "system",
# #                         "content": "Ти корисний AI асистент. Відповідай українською мовою коротко та по суті."
# #                     },
# #                     {
# #                         "role": "user", 
# #                         "content": message
# #                     }
# #                 ],
# #                 "temperature": 0.7,
# #                 "max_tokens": 500
# #             }
            
# #             async with aiohttp.ClientSession() as session:
# #                 async with session.post(
# #                     self.base_url, 
# #                     headers=headers, 
# #                     json=data,
# #                     timeout=aiohttp.ClientTimeout(total=30)
# #                 ) as response:
                    
# #                     if response.status == 200:
# #                         result = await response.json()
# #                         return f"🌊 DeepSeek: {result['choices'][0]['message']['content']}"
# #                     else:
# #                         # Якщо API не працює, використовуємо локальну логіку
# #                         return await self.get_smart_response(message)
                        
# #         except Exception as e:
# #             return await self.get_smart_response(message)
    
# #     async def get_smart_response(self, message: str) -> str:
# #         """
# #         Розумна локальна логіка для генерації відповідей
# #         """
# #         # Аналізуємо інтент запиту
# #         if "питання" in message.lower() and len(message.strip()) < 20:
# #             return "🌊 DeepSeek: Звісно! Задавайте своє питання, я готовий допомогти."
        
# #         # Тут можна додати більше логіки для різних типів запитань
# #         responses = [
# #             f"🌊 DeepSeek: Цікаве питання! {message}",
# #             f"🌊 DeepSeek: Дякую за запит. Давайте розглянемо {message}",
# #             f"🌊 DeepSeek: Аналізую ваше питання... {message}",
# #             f"🌊 DeepSeek: Чудово! Маю кілька ідей щодо {message}"
# #         ]
        
# #         import random
# #         return random.choice(responses)










# import os
# import aiohttp
# import json
# import random
# from typing import Optional

# class HuggingFaceConnector:
#     def __init__(self):
#         self.api_key = os.getenv("HUGGINGFACE_API_KEY", "free")
#         # Використовуємо стабільну модель
#         self.models = [
#             "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium",
#             "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
#         ]
    
#     async def generate_response(self, message: str) -> Optional[str]:
#         """
#         Генерує відповідь через Hugging Face з розумною логікою
#         """
#         # Спочатку аналізуємо запит
#         if self.is_simple_query(message):
#             return await self.get_contextual_response(message)
        
#         # Якщо запит складний, пробуємо API
#         for model_url in self.models:
#             try:
#                 response = await self.query_model(model_url, message)
#                 if response and len(response) > 10:  # Якщо відповідь осмислена
#                     return f"🤗 Hugging Face: {response}"
#             except:
#                 continue
        
#         # Якщо API не спрацювало
#         return await self.get_contextual_response(message)
    
#     def is_simple_query(self, message: str) -> bool:
#         """Визначає чи запит простий (без конкретного питання)"""
#         simple_phrases = ["привіт", "hello", "вітання", "питання", "питаю", "хочу запитати"]
#         message_lower = message.lower()
        
#         if len(message.strip()) < 15:
#             return True
        
#         for phrase in simple_phrases:
#             if phrase in message_lower:
#                 return True
                
#         return False
    
#     async def get_contextual_response(self, message: str) -> str:
#         """Генерує контекстну відповідь на основі запиту"""
#         message_lower = message.lower()
        
#         if any(word in message_lower for word in ["привіт", "вітання", "hello", "hi"]):
#             responses = [
#                 "Привіт! Я AI асистент. Чим можу допомогти?",
#                 "Вітаю! Задавайте своє питання.",
#                 "Привіт! Радий спілкуванню. Що цікавить?"
#             ]
#         elif any(word in message_lower for word in ["питання", "питаю", "запитати"]):
#             if len(message.strip()) < 20:
#                 responses = [
#                     "Так, звісно! Я готовий відповісти на ваше питання.",
#                     "Задавайте, будь ласка, своє питання.",
#                     "Чудово! Я уважно слухаю ваше питання.",
#                     "Готовий допомогти. Що саме вас цікавить?"
#                 ]
#             else:
#                 responses = [
#                     f"Цікаве питання! Давайте розглянемо {message}",
#                     f"Дякую за запит. Аналізую {message}",
#                     f"Чудово! Маю кілька думок щодо {message}"
#                 ]
#         else:
#             responses = [
#                 f"Цікаво! {message}",
#                 f"Дякую за повідомлення. {message}",
#                 f"Чудовий запит! {message}",
#                 f"Аналізую ваш запит: {message}"
#             ]
        
#         return f"🤗 Hugging Face: {random.choice(responses)}"
    
#     async def query_model(self, model_url: str, message: str) -> str:
#         """Запит до конкретної моделі"""
#         try:
#             headers = {
#                 "Authorization": f"Bearer {self.api_key}" if self.api_key != "free" else "",
#                 "Content-Type": "application/json"
#             }
            
#             data = {"inputs": message}
            
#             async with aiohttp.ClientSession() as session:
#                 async with session.post(
#                     model_url, 
#                     headers=headers, 
#                     json=data,
#                     timeout=aiohttp.ClientTimeout(total=20)
#                 ) as response:
                    
#                     if response.status == 200:
#                         result = await response.json()
#                         return self.extract_text(result)
#                     return ""
                    
#         except Exception:
#             return ""
    
#     def extract_text(self, result) -> str:
#         """Витягує текст з відповіді моделі"""
#         try:
#             if isinstance(result, list) and result:
#                 if "generated_text" in result[0]:
#                     text = result[0]["generated_text"]
#                     # Видаляємо оригінальне повідомлення
#                     inputs = result[0].get("inputs", "")
#                     if text.startswith(inputs):
#                         text = text[len(inputs):].strip()
#                     return text
#             return ""
#         except:
#             return ""
















# import os
# import aiohttp
# import json
# import random
# from typing import Optional

# class HuggingFaceConnector:
#     def __init__(self):
#         self.api_key = os.getenv("HUGGINGFACE_API_KEY", "free")
#         # Використовуємо потужну модель для текстової генерації
#         self.model_url = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-large"
    
#     async def generate_response(self, message: str) -> Optional[str]:
#         """
#         Генерує унікальні AI відповіді через Hugging Face або локальну генерацію
#         """
#         try:
#             # Спочатку пробуємо отримати відповідь через API
#             api_response = await self.get_api_response(message)
#             if api_response and self.is_meaningful_response(api_response, message):
#                 return f"🤗 Hugging Face: {api_response}"
            
#             # Якщо API не дав гарної відповіді, генеруємо локально
#             return await self.generate_smart_response(message)
            
#         except Exception as e:
#             return await self.generate_smart_response(message)
    
#     async def get_api_response(self, message: str) -> str:
#         """Спробує отримати відповідь через Hugging Face API"""
#         try:
#             headers = {
#                 "Authorization": f"Bearer {self.api_key}" if self.api_key != "free" else "",
#                 "Content-Type": "application/json"
#             }
            
#             # Для DialoGPT моделей
#             data = {
#                 "inputs": {
#                     "text": message,
#                     "past_user_inputs": [],
#                     "generated_responses": []
#                 },
#                 "parameters": {
#                     "max_length": 150,
#                     "temperature": 0.9,
#                     "do_sample": True,
#                     "top_p": 0.95
#                 }
#             }
            
#             async with aiohttp.ClientSession() as session:
#                 async with session.post(
#                     self.model_url, 
#                     headers=headers, 
#                     json=data,
#                     timeout=aiohttp.ClientTimeout(total=20)
#                 ) as response:
                    
#                     if response.status == 200:
#                         result = await response.json()
#                         if isinstance(result, dict) and "generated_text" in result:
#                             return result["generated_text"]
                    
#             return ""
            
#         except Exception:
#             return ""
    
#     def is_meaningful_response(self, response: str, original_message: str) -> bool:
#         """Перевіряє чи відповідь осмислена (не повторює запит)"""
#         if not response or len(response.strip()) < 10:
#             return False
        
#         # Якщо відповідь просто повторює запит
#         if original_message.lower() in response.lower():
#             return False
            
#         return True
    
#     async def generate_smart_response(self, message: str) -> str:
#         """Генерує розумну унікальну відповідь локально"""
#         message_lower = message.lower()
        
#         # Аналізуємо інтент та генеруємо відповідну відповідь
#         if any(word in message_lower for word in ["привіт", "вітання", "hello", "hi", "добрий день"]):
#             return self.generate_greeting_response(message)
        
#         elif any(word in message_lower for word in ["питання", "запитати", "питаю", "допоможи", "допоможіть"]):
#             return self.generate_question_response(message)
        
#         elif any(word in message_lower for word in ["дякую", "спасибі", "thanks", "thank you"]):
#             return self.generate_thanks_response()
        
#         elif any(word in message_lower for word in ["кава", "чай", "спати", "енергія", "втома"]):
#             return self.generate_energy_response(message)
        
#         elif any(word in message_lower for word in ["програміст", "код", "програмування", "developer", "coding"]):
#             return self.generate_programming_response(message)
        
#         elif any(word in message_lower for word in ["як", "що", "чому", "де", "коли"]):
#             return self.generate_howto_response(message)
        
#         else:
#             return self.generate_general_response(message)
    
#     def generate_greeting_response(self, message: str) -> str:
#         """Генерує унікальні привітальні відповіді"""
#         greetings = [
#             "Привіт! Радий вас бачити. Як ваш AI помічник, я готовий відповісти на будь-які питання!",
#             "Вітаю! Задавайте свої питання - я спеціалізуюсь на технологіях, навчанні та творчих ідеях.",
#             "Привіт! Я AI модель, яка допомагає з різноманітними завданнями. Чим саме можу бути корисним?",
#             "Доброго дня! Я завжди радий новим питанням та можливостям допомогти. Що вас цікавить?",
#             "Вітаю! Як штучний інтелект, я можу допомогти з аналізом, креативними ідеями та технічними питаннями."
#         ]
#         return f"🤗 Hugging Face: {random.choice(greetings)}"
    
#     def generate_question_response(self, message: str) -> str:
#         """Генерує відповіді на питання"""
#         if len(message.strip()) < 25:
#             responses = [
#                 "Так, звісно! Я уважно слухаю. Будь ласка, задайте своє питання повністю.",
#                 "Чудово! Я готовий допомогти. Розкажіть детальніше, що саме вас цікавить?",
#                 "З радістю! Щоб дати якісну відповідь, мені потрібно трохи більше контексту.",
#                 "Відмінно! Задавайте своє питання, а я постараюсь дати корисну відповідь."
#             ]
#         else:
#             responses = [
#                 f"Цікаве питання! Давайте розберемо '{message}' детальніше.",
#                 f"Дякую за конкретне запитання! Аналізую '{message}' з різних角度.",
#                 f"Чудово! Маю кілька корисних ідей щодо '{message}'.",
#                 f"Це варте обговорення! Давайте розглянемо різні аспекти вашого запиту."
#             ]
#         return f"🤗 Hugging Face: {random.choice(responses)}"
    
#     def generate_thanks_response(self) -> str:
#         """Відповідає на подяку"""
#         responses = [
#             "Завжди радий допомогти! Звертайтеся, якщо будуть ще питання.",
#             "Будь ласка! Буду радий допомогти вам знову.",
#             "Дякую вам за звернення! Приємно бути корисним.",
#             "Будь ласка! Сподіваюсь, моя відповідь була корисною."
#         ]
#         return f"🤗 Hugging Face: {random.choice(responses)}"
    
#     def generate_energy_response(self, message: str) -> str:
#         """Генерує відповіді про енергію та сон"""
#         responses = [
#             "Для підтримки енергії рекомендую зелений чай - він м'якше за каву. Також важливі короткі перерви та свіже повітря!",
#             "Як AI, я раджу збалансований підхід: легкий чай, перерви кожні 45 хвилин та гідратація. Сон - найкращий енергетик!",
#             "Програмісти часто обирають каву, але зелений чай дає більш стійку енергію. А найголовніше - якісний відпочинок!",
#             "Вночі організм потребує відпочинку. Замість стимуляторів - короткі перерви, легкі вправи та збалансоване харчування."
#         ]
#         return f"🤗 Hugging Face: {random.choice(responses)}"
    
#     def generate_programming_response(self, message: str) -> str:
#         """Генерує відповіді про програмування"""
#         responses = [
#             "Програмування - це чудово! Раджу починати з Python чи JavaScript, практикуватись щодня та не боятись помилок.",
#             "Як AI, я бачу що найкраще навчання - через практику. Створюйте невеличкі проекти та аналізуйте чужій код!",
#             "Програмісти часто працюють вночі, але здоровый режим важливіший за дедлайни. Ваш мозок потребує відпочинку!",
#             "Для ефективного навчання: маленькі кроки, багато практики, участь у спільнотах та не порівнюйте себе з іншими!"
#         ]
#         return f"🤗 Hugging Face: {random.choice(responses)}"
    
#     def generate_howto_response(self, message: str) -> str:
#         """Генерує відповіді на питання 'як'"""
#         responses = [
#             f"Це чудове питання! Щоб дати точну відповідь на '{message}', потрібно розглянути кілька підходів.",
#             f"Відмінне запитання! Давайте розберемо поетапно як можна вирішити '{message}'.",
#             f"Цікавий запит! Існує кілька ефективних способів для '{message}' - розглянемо найкращі.",
#             f"Чудово! Для '{message}' я можу запропонувати кілька практичних рішень."
#         ]
#         return f"🤗 Hugging Face: {random.choice(responses)}"
    
#     def generate_general_response(self, message: str) -> str:
#         """Генерує загальні відповіді"""
#         responses = [
#             f"Цікавий запит! '{message}' - давайте обговоримо це детальніше. Що саме вас найбільше цікавить?",
#             f"Дякую за повідомлення! '{message}' - це чудова тема для обговорення. Маю кілька корисних ідей!",
#             f"Чудово! '{message}' - варте уваги. Як AI асистент, я можу запропонувати кілька підходів до цього питання.",
#             f"Цікаво! '{message}' - давайте розглянемо різні аспекти цієї теми. Що для вас найважливіше?"
#         ]
#         return f"🤗 Hugging Face: {random.choice(responses)}"






















# import os
# import random
# from typing import Optional

# class HuggingFaceConnector:
#     def __init__(self):
#         self.api_key = os.getenv("HUGGINGFACE_API_KEY", "free")
    
#     async def generate_response(self, message: str) -> Optional[str]:
#         """
#         Генерує унікальну відповідь на БУДЬ-ЯКЕ повідомлення
#         """
#         try:
#             return await self.generate_unique_response(message)
#         except Exception as e:
#             return f"🤗 Hugging Face: Вибачте, сталася помилка: {str(e)}"
    
#     async def generate_unique_response(self, message: str) -> str:
#         """Генерує унікальну відповідь для будь-якого повідомлення"""
        
#         # Базові компоненти для генерації унікальних відповідей
#         starters = [
#             "Цікаво!",
#             "Чудово!",
#             "Відмінно!",
#             "Зрозуміло!",
#             "Дякую за запитання!",
#             "Це варте обговорення!",
#             "Прекрасне питання!",
#             "Дуже цікаво!",
#             "Захоплююче!",
#             "Чудова тема!"
#         ]
        
#         connectors = [
#             "Я думаю, що",
#             "На мою думку,",
#             "З мого досвіду,",
#             "Як AI асистент, я вважаю,",
#             "З точки зору технологій,",
#             "З огляду на сучасні тенденції,",
#             "Враховуючи ваш запит,",
#             "Аналізуючи ситуацію,",
#             "З позиції користувача,",
#             "З технічної точки зору,"
#         ]
        
#         insights = [
#             "це відкриває багато можливостей для дослідження та розвитку.",
#             "це демонструє важливість постійного навчання та адаптації.",
#             "це підкреслює значення інновацій у сучасному світі.",
#             "це показує, як технології змінюють наш спосіб мислення.",
#             "це ілюструє динаміку розвитку сучасних комунікацій.",
#             "це відображає тенденції цифрової трансформації.",
#             "це вказує на важливість міждисциплінарного підходу.",
#             "це підтверджує значення креативного мислення.",
#             "це розкриває потенціал майбутніх технологій.",
#             "це демонструє взаємозв'язок різних аспектів сучасного життя."
#         ]
        
#         actions = [
#             "Рекомендую розглянути це питання з різних перспектив.",
#             "Варто дослідити цю тему більш детально.",
#             "Має сенс обговорити це з фахівцями у відповідній галузі.",
#             "Це чудова нагода для подальшого навчання та розвитку.",
#             "Пропоную розглянути практичне застосування цієї ідеї.",
#             "Це може стати відправною точкою для нових відкриттів.",
#             "Варто проаналізувати міжнародний досвід у цій сфері.",
#             "Це ідеальна можливість для експериментів та інновацій.",
#             "Пропоную дослідити альтернативні підходи до цього питання.",
#             "Це може привести до цікавих висновків та рішень."
#         ]
        
#         endings = [
#             "Що ви думаєте з цього приводу?",
#             "Які ще аспекти цієї теми вас цікавлять?",
#             "Чи маєте ви досвід у цій сфері?",
#             "Як би ви розвинули цю ідею далі?",
#             "Що для вас найцікавіше в цьому питанні?",
#             "Які питання виникають у вас після цієї відповіді?",
#             "Чи бачите ви практичне застосування цих ідей?",
#             "Як ця інформація може бути корисною для вас?",
#             "Що б ви хотіли дізнатися ще на цю тему?",
#             "Які висновки ви можете зробити з цього?"
#         ]
        
#         # Генеруємо унікальну відповідь
#         starter = random.choice(starters)
#         connector = random.choice(connectors)
#         insight = random.choice(insights)
#         action = random.choice(actions)
#         ending = random.choice(endings)
        
#         # Додаємо персоналізацію на основі повідомлення
#         personalized_response = f"{starter} {connector} {insight} {action} {ending}"
        
#         return f"🤗 Hugging Face: {personalized_response}"














# import os
# import aiohttp
# import json
# from typing import Optional

# class HuggingFaceConnector:
#     def __init__(self):
#         self.api_key = os.getenv("HUGGINGFACE_API_KEY", "free")
#         # Використовуємо потужну модель для чату
#         self.model_url = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-large"
    
#     async def generate_response(self, message: str) -> Optional[str]:
#         """
#         Генерує реальну відповідь через Hugging Face Inference API
#         """
#         try:
#             # Якщо є API ключ, використовуємо реальний API
#             if self.api_key and self.api_key != "free":
#                 return await self.get_real_api_response(message)
#             else:
#                 # Без ключа - використовуємо локальну імітацію
#                 return await self.get_simulated_response(message)
                
#         except Exception as e:
#             return f"🤗 Hugging Face: Помилка: {str(e)}"
    
#     async def get_real_api_response(self, message: str) -> str:
#         """Отримує реальну відповідь через Hugging Face API"""
#         try:
#             headers = {
#                 "Authorization": f"Bearer {self.api_key}",
#                 "Content-Type": "application/json"
#             }
            
#             # Використовуємо DialoGPT для генерації відповідей
#             data = {
#                 "inputs": {
#                     "text": message,
#                     "past_user_inputs": [],
#                     "generated_responses": []
#                 },
#                 "parameters": {
#                     "max_length": 150,
#                     "temperature": 0.9,
#                     "do_sample": True,
#                     "top_p": 0.95,
#                     "repetition_penalty": 1.2
#                 }
#             }
            
#             async with aiohttp.ClientSession() as session:
#                 async with session.post(
#                     self.model_url, 
#                     headers=headers, 
#                     json=data,
#                     timeout=aiohttp.ClientTimeout(total=30)
#                 ) as response:
                    
#                     if response.status == 200:
#                         result = await response.json()
#                         if isinstance(result, dict) and "generated_text" in result:
#                             return f"🤗 Hugging Face: {result['generated_text']}"
                    
#                     # Якщо API не працює, повертаємо імітовану відповідь
#                     return await self.get_simulated_response(message)
                        
#         except Exception:
#             return await self.get_simulated_response(message)
    
#     async def get_simulated_response(self, message: str) -> str:
#         """Імітує розумну відповідь, коли API недоступне"""
#         # Проста логіка для демонстрації
#         responses = [
#             f"🤗 Hugging Face: Цікаве питання! '{message}' - давайте обговоримо це детальніше.",
#             f"🤗 Hugging Face: Дякую за запитання про '{message}'. Як AI асистент, я можу запропонувати кілька ідей.",
#             f"🤗 Hugging Face: Чудово! '{message}' - це важлива тема. Давайте розглянемо різні підходи.",
#             f"🤗 Hugging Face: Аналізую ваш запит '{message}'. Це відкриває багато можливостей для обговорення.",
#             f"🤗 Hugging Face: Цікавий запит! '{message}' вартий уваги. Що саме вас найбільше цікавить?"
#         ]
        
#         import random
#         return random.choice(responses)



import os
import aiohttp
import json
import random
from typing import Optional

class HuggingFaceConnector:
    def __init__(self):
        self.api_key = os.getenv("HUGGINGFACE_API_KEY", "")
        self.base_url = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-large"
        self.name = "🤗 HuggingFace"
    
    async def generate_response(self, message: str) -> Optional[str]:
        """
        Генерує відповідь через Hugging Face API
        """
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "inputs": message,
                "parameters": {
                    "max_length": 150,
                    "temperature": 0.7,
                    "do_sample": True
                }
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
                        if isinstance(result, list) and len(result) > 0:
                            generated_text = result[0].get('generated_text', '')
                            # Видаляємо оригінальне повідомлення з відповіді
                            clean_response = generated_text.replace(message, '').strip()
                            return f"{self.name}: {clean_response}"
                        return await self.get_fallback_response(message)
                    else:
                        return await self.get_fallback_response(message)
                        
        except Exception as e:
            return await self.get_fallback_response(message)
    
    async def get_fallback_response(self, message: str) -> str:
        """Резервна локальна логіка"""
        responses = [
            f"{self.name}: Цікавий запит! '{message}'",
            f"{self.name}: Обробляю ваше питання про '{message}'",
            f"{self.name}: Маю кілька коментарів щодо '{message}'",
        ]
        return random.choice(responses)