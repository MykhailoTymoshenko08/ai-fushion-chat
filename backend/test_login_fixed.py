import requests
import json

def test_login():
    print("=== Тест логіну ===")
    
    login_data = {
        "email": "test@example.com",
        "password": "password123"
    }
    
    try:
        response = requests.post(
            "http://127.0.0.1:8000/auth/login", 
            json=login_data,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"📊 Статус: {response.status_code}")
        print(f"📋 Відповідь: {response.text}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Успішний вхід!")
            print(f"🔑 Токен: {data['access_token'][:50]}...")
        else:
            print("❌ Помилка входу")
            
    except Exception as e:
        print(f"❌ Помилка: {e}")

if __name__ == "__main__":
    test_login()