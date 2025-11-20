print("=== Тест бази даних AI Fusion Chat ===")

try:
    # Спочатку імпортуємо Base та створимо всі таблиці
    from database.base import Base
    from database.config import engine
    
    print(" Імпорт модулів...")
    
    # Тепер імпортуємо моделі
    from models.user import User
    from models.chat import Chat
    from models.message import Message
    
    print(" Моделі імпортовані")
    
    # Створюємо всі таблиці
    print(" Створення таблиць...")
    Base.metadata.drop_all(bind=engine)  # Спочатку видаляємо старі таблиці
    Base.metadata.create_all(bind=engine)
    print(" Таблиці створені успішно!")
    
    # Тестовий запис
    from database.config import SessionLocal
    db = SessionLocal()
    
    try:
        # Створюємо тестового користувача
        test_user = User(
            email="test@example.com",
            username="testuser", 
            hashed_password="testhash123"
        )
        db.add(test_user)
        db.commit()
        db.refresh(test_user)
        
        # Створюємо тестовий чат
        test_chat = Chat(
            title="Перший тестовий чат",
            user_id=test_user.id
        )
        db.add(test_chat)
        db.commit()
        db.refresh(test_chat)
        
        # Створюємо тестове повідомлення
        test_message = Message(
            chat_id=test_chat.id,
            content="Привіт, це тестове повідомлення!",
            role="user"
        )
        db.add(test_message)
        db.commit()
        
        print("Тестові дані додані успішно!")
        print(f"   Користувач: {test_user.username} (ID: {test_user.id})")
        print(f"   Чат: {test_chat.title} (ID: {test_chat.id})")
        print(f"   Повідомлення: {test_message.content}")
        
    except Exception as e:
        db.rollback()
        print(f" Помилка при додаванні даних: {e}")
    finally:
        db.close()
    
except Exception as e:
    print(f" Помилка: {e}")
    import traceback
    traceback.print_exc()

print("=== Тест завершено ===")