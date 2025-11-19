from database.config import SessionLocal, engine
from database.base import Base
from models.user import User
from models.chat import Chat
from models.message import Message

def test_all_models():
    print("=== Тест всіх моделей ===")
    
    # Створюємо таблиці
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        # Створюємо користувача
        user = User(email="test@test.com", username="tester", hashed_password="test")
        db.add(user)
        db.commit()
        db.refresh(user)
        print(f"✅ Користувач: {user.username}")
        
        # Створюємо чат
        chat = Chat(title="Тестовий чат", user_id=user.id)
        db.add(chat)
        db.commit()
        db.refresh(chat)
        print(f"✅ Чат: {chat.title}")
        
        # Створюємо повідомлення
        message = Message(chat_id=chat.id, content="Тестове повідомлення", role="user")
        db.add(message)
        db.commit()
        print(f"✅ Повідомлення: {message.content}")
        
        print("🎉 Всі моделі працюють!")
        
    except Exception as e:
        print(f"❌ Помилка: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    test_all_models()