import requests
import json

def test_ai_chat():
    print("=== Тест AI Чату ===")
    
    # 1. Створюємо чат
    try:
        response = requests.post(
            "http://127.0.0.1:8000/chat/chats",
            params={"title": "Тестовий AI чат"}
        )
        print(f"📊 Створення чату: {response.status_code}")
        if response.status_code == 200:
            chat = response.json()
            chat_id = chat["id"]
            print(f"✅ Чат створений: ID {chat_id}")
        else:
            print(f"❌ Помилка створення чату: {response.text}")
            return
    except Exception as e:
        print(f"❌ Помилка: {e}")
        return
    
    # 2. Надсилаємо повідомлення
    try:
        response = requests.post(
            f"http://127.0.0.1:8000/chat/chats/{chat_id}/message",
            params={"message": "Привіт! Розкажи щось цікаве"}
        )
        print(f"📊 Відповідь AI: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"✅ Користувач: {result['user_message']['content']}")
            print(f"🤖 AI: {result['ai_response']['content']}")
        else:
            print(f"❌ Помилка: {response.text}")
    except Exception as e:
        print(f"❌ Помилка: {e}")

if __name__ == "__main__":
    test_ai_chat()