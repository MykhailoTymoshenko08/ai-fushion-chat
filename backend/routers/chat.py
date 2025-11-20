from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.config import get_db
from models.chat import Chat
from models.message import Message
from models.user import User
from services.aggregator import AIAggregator  # ДОДАНО

router = APIRouter()

@router.post("/chats")
def create_chat(title: str, db: Session = Depends(get_db)):
    """
    Створює новий чат
    """
    # Тимчасово використовуємо першого користувача
    user = db.query(User).first()
    if not user:
        raise HTTPException(status_code=404, detail="Користувач не знайдений")
    
    new_chat = Chat(title=title, user_id=user.id)
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)
    
    return new_chat

@router.post("/chats/{chat_id}/message")
async def send_message(chat_id: int, message: str, db: Session = Depends(get_db)):
    """
    Надсилає повідомлення в чат і отримує відповіді від ВСІХ AI моделей
    """
    # Перевіряємо чи існує чат
    chat = db.query(Chat).filter(Chat.id == chat_id).first()
    if not chat:
        raise HTTPException(status_code=404, detail="Чат не знайдений")
    
    # Зберігаємо повідомлення користувача
    user_message = Message(
        chat_id=chat_id,
        content=message,
        role="user"
    )
    db.add(user_message)
    db.commit()
    
    # Отримуємо відповіді від ВСІХ AI моделей
    aggregator = AIAggregator()
    all_responses = await aggregator.get_all_responses(message)
    
    # Зберігаємо всі відповіді AI
    ai_messages = []
    for model_name, response in all_responses.items():
        ai_message = Message(
            chat_id=chat_id,
            content=f"[{model_name.upper()}] {response}",
            role="assistant"
        )
        db.add(ai_message)
        ai_messages.append(ai_message)
    
    db.commit()
    
    return {
        "user_message": user_message,
        "ai_responses": all_responses,  # Всі відповіді окремо
        "ai_messages": ai_messages     # Всі збережені повідомлення
    }

@router.post("/chats/{chat_id}/message/{model}")
async def send_message_to_model(chat_id: int, model: str, message: str, db: Session = Depends(get_db)):
    """
    Надсилає повідомлення до конкретної AI моделі
    """
    chat = db.query(Chat).filter(Chat.id == chat_id).first()
    if not chat:
        raise HTTPException(status_code=404, detail="Чат не знайдений")
    
    # Зберігаємо повідомлення користувача
    user_message = Message(
        chat_id=chat_id,
        content=f"[{model.upper()}] {message}",
        role="user"
    )
    db.add(user_message)
    db.commit()
    
    # Отримуємо відповідь від конкретної моделі
    aggregator = AIAggregator()
    ai_response = await aggregator.get_single_response(model, message)
    
    # Зберігаємо відповідь AI
    ai_message = Message(
        chat_id=chat_id,
        content=ai_response,
        role="assistant"
    )
    db.add(ai_message)
    db.commit()
    db.refresh(ai_message)
    
    return {
        "user_message": user_message,
        "ai_response": ai_response,
        "model_used": model
    }

@router.get("/chats/{chat_id}/messages")
def get_chat_messages(chat_id: int, db: Session = Depends(get_db)):
    """
    Отримує всі повідомлення чату
    """
    messages = db.query(Message).filter(Message.chat_id == chat_id).order_by(Message.created_at).all()
    return messages

@router.get("/chats")
def get_user_chats(db: Session = Depends(get_db)):
    """
    Отримує всі чати користувача
    """
    user = db.query(User).first()
    if not user:
        return []
    
    chats = db.query(Chat).filter(Chat.user_id == user.id).all()
    return chats

@router.get("/models")
async def get_available_models():
    """
    Повертає список доступних AI моделей
    """
    return {
        "available_models": [
            "groq",           # 🚀 Безкоштовний реальний API
            "huggingface",    # 🤗 Безкоштовний API  
            "openai",         # 🎯 Тестовий режим
            "claude",         # 🧠 Тестовий режим
            "gemini",         # 🔮 Тестовий режим
            "mistral"         # 🌪️ Тестовий режим
        ],
        "free_apis": ["groq", "huggingface"],
        "description": "AI Fusion Chat - з безкоштовними API та тестовими режимами"
    }

@router.get("/groq/models")
async def get_groq_models():
    """
    Повертає список доступних моделей Groq
    """
    return {
        "available_groq_models": [
            "llama-3.1-8b-instant",
            "llama-3.1-70b-versatile", 
            "mixtral-8x7b-32768",
            "gemma2-9b-it"
        ],
        "recommended": "llama-3.1-8b-instant"
    }