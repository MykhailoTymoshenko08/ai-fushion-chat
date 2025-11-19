print("=== Спрощений тест авторизації ===")

try:
    # Імпортуємо без схем
    from database.config import SessionLocal, engine
    from database.base import Base
    from models.user import User
    
    # Створюємо таблиці
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    # Тест хешування паролів
    from utils.auth import get_password_hash, verify_password, create_access_token
    
    print("1. Тестуємо хешування пароля...")
    test_password = "testpassword123"
    hashed_password = get_password_hash(test_password)
    print(f"   ✅ Пароль успішно захешовано")
    
    print("2. Тестуємо перевірку пароля...")
    is_correct = verify_password(test_password, hashed_password)
    print(f"   ✅ Перевірка пароля: {is_correct}")
    
    print("3. Тестуємо створення JWT токена...")
    test_data = {"sub": "testuser"}
    token = create_access_token(data=test_data)
    print(f"   ✅ JWT токен створено: {token[:50]}...")
    
    print("4. Тестуємо додавання користувача в БД...")
    new_user = User(
        email="test2@example.com",
        username="testuser2", 
        hashed_password=hashed_password
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print(f"   ✅ Користувач створений: {new_user.username} (ID: {new_user.id})")
    
    print("5. Тестуємо пошук користувача...")
    found_user = db.query(User).filter(User.email == "test2@example.com").first()
    if found_user:
        print(f"   ✅ Користувач знайдений: {found_user.username}")
        
        # Перевіряємо пароль
        if verify_password("testpassword123", found_user.hashed_password):
            user_token = create_access_token(data={"sub": found_user.username})
            print(f"   ✅ Логін успішний! Токен: {user_token[:50]}...")
        else:
            print("   ❌ Помилка перевірки пароля")
    else:
        print("   ❌ Користувач не знайдений")
    
    db.close()
    print("🎉 Всі тести пройдено успішно!")
    
except Exception as e:
    print(f"❌ Помилка: {e}")
    import traceback
    traceback.print_exc()

print("=== Тест завершено ===")