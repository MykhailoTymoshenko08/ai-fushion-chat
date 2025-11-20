import requests
import json

def test_all_models():
    print("=== Тест всіх AI моделей ===")
    
    # 1. Створюємо чат
    response = requests.post("http://127.0.0.1:8000/chat/chats", params={"title": "Тест всіх моделей"})
    chat_id = response.json()["id"]
    print(f"✅ Чат створений: ID {chat_id}")
    
    # 2. Тестуємо всі моделі разом
    print("\n🔧 Тестуємо всі моделі одночасно...")
    response = requests.post(
        f"http://127.0.0.1:8000/chat/chats/{chat_id}/message",
        params={"message": "Привіт! Розкажи про себе"}
    )
    
    result = response.json()
    print("📋 Відповіді від всіх моделей:")
    for model, response in result["ai_responses"].items():
        print(f"  🤖 {model.upper()}: {response[:80]}...")
    
    # 3. Тестуємо кожну модель окремо
    models = ["openai", "claude", "gemini", "mistral"]
    
    for model in models:
        print(f"\n🔧 Тестуємо {model}...")
        response = requests.post(
            f"http://127.0.0.1:8000/chat/chats/{chat_id}/message/{model}",
            params={"message": f"Привіт, {model}! Як справи?"}
        )
        
        result = response.json()
        print(f"  📊 Статус: {response.status_code}")
        
        # Безпечний вивід
        if 'user_message' in result and 'content' in result['user_message']:
            print(f"  💬 Користувач: {result['user_message']['content']}")
        else:
            print(f"  💬 Користувач: {result.get('user_message', 'Немає даних')}")
        
        print(f"  🤖 Відповідь: {result.get('ai_response', 'Немає відповіді')}")
        
        # Додатковий вивід для дебагу
        print(f"  🔍 Повна відповідь: {json.dumps(result, indent=2, ensure_ascii=False)[:200]}...")

if __name__ == "__main__":
    test_all_models()