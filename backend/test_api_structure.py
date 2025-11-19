import requests
import json

def test_api_structure():
    print("=== Тест структури API ===")
    
    # Створюємо чат
    response = requests.post("http://127.0.0.1:8000/chat/chats", params={"title": "Тест структури"})
    chat_id = response.json()["id"]
    print(f"✅ Чат створений: ID {chat_id}")
    
    # Тестуємо всі моделі
    print("\n1. Тестуємо всі моделі:")
    response = requests.post(
        f"http://127.0.0.1:8000/chat/chats/{chat_id}/message",
        params={"message": "Тестове повідомлення"}
    )
    result = response.json()
    print("📋 Структура відповіді для всіх моделей:")
    print(json.dumps(result, indent=2, ensure_ascii=False))
    
    # Тестуємо одну модель
    print("\n2. Тестуємо одну модель (openai):")
    response = requests.post(
        f"http://127.0.0.1:8000/chat/chats/{chat_id}/message/openai",
        params={"message": "Тест для OpenAI"}
    )
    result = response.json()
    print("📋 Структура відповіді для однієї моделі:")
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    test_api_structure()