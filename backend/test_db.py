print("=== Тест бази даних AI Fusion Chat ===")

try:
    from database.config import engine, SessionLocal
    from models.user import User
    from models.chat import Chat
    from models.message import Message
    
    print("✅ Модулі успішно імпортовані")
    
    # Створюємо таблиці
    from database.base import Base
    Base.metadata.create_all(bind=engine)
    print("✅ Таблиці створені успішно!")
    
    # Тестовий запис
    db = SessionLocal()
    
    # Створюємо тестового користувача
    test_user = User(
        email="test@example.com",
        username="testuser", 
        hashed_password="testhash123"
    )
    db.add(test_user)
    db.commit()
    
    # Створюємо тестовий чат
    test_chat = Chat(
        title="Перший тестовий чат",
        user_id=test_user.id
    )
    db.add(test_chat)
    db.commit()
    
    # Створюємо тестове повідомлення
    test_message = Message(
        chat_id=test_chat.id,
        content="Привіт, це тестове повідомлення!",
        role="user"
    )
    db.add(test_message)
    db.commit()
    
    print("✅ Тестові дані додані успішно!")
    print(f"   Користувач: {test_user.username}")
    print(f"   Чат: {test_chat.title}")
    print(f"   Повідомлення: {test_message.content}")
    
    db.close()
    
except ImportError as e:
    print(f"❌ Помилка імпорту: {e}")
    print("Перевірте структуру файлів та імпорти")
except Exception as e:
    print(f"❌ Інша помилка: {e}")

print("=== Тест завершено ===")