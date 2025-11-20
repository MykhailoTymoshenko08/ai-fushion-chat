from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from database.config import engine, Base
from utils.config import settings

# Створюємо таблиці в БД
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Fusion Chat API",
    description="Чат-платформа з інтеграцією кількох AI моделей",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],  # Додано фронтенд URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Підключаємо роутери
from routers import auth, chat

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])  # ДОДАНО

@app.get("/")
async def root():
    return {"message": "AI Fusion Chat API", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)