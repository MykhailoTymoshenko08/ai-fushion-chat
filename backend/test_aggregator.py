import asyncio
from services.aggregator import AIAggregator

async def test_aggregator():
    print("=== Тест агрегатора ===")
    
    aggregator = AIAggregator()
    
    # Тест 1: Перевірка методу get_all_responses
    print("1. Тестуємо get_all_responses...")
    try:
        responses = await aggregator.get_all_responses("Привіт")
        print("✅ get_all_responses працює!")
        for model, response in responses.items():
            print(f"   {model}: {response}")
    except Exception as e:
        print(f"❌ Помилка: {e}")
    
    # Тест 2: Перевірка методу get_single_response
    print("\n2. Тестуємо get_single_response...")
    try:
        response = await aggregator.get_single_response("groq", "Тест")
        print(f"✅ get_single_response працює: {response}")
    except Exception as e:
        print(f"❌ Помилка: {e}")

if __name__ == "__main__":
    asyncio.run(test_aggregator())
    