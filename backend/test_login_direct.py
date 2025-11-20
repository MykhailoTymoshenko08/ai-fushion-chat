import requests
import json

def test_direct():
    print("=== Прямий тест логіну ===")
    
    # Тестуємо різні способи відправки даних
    test_cases = [
        {
            "name": "JSON body",
            "url": "http://127.0.0.1:8000/auth/login",
            "data": {"email": "test@example.com", "password": "password123"},
            "headers": {"Content-Type": "application/json"}
        }
    ]
    
    for test in test_cases:
        print(f"\n🔧 Тест: {test['name']}")
        try:
            response = requests.post(
                test["url"],
                json=test["data"],
                headers=test["headers"]
            )
            print(f"📊 Статус: {response.status_code}")
            print(f"📋 Тіло: {response.text}")
        except Exception as e:
            print(f"❌ Помилка: {e}")

if __name__ == "__main__":
    test_direct()