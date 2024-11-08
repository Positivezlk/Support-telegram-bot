from bot_instance import bot, dp
from handlers import router as handlers_router
from callback import router as callback_router

dp.include_router(handlers_router)
dp.include_router(callback_router)

print("БОТ ЗАПУЩЕН УСПЕШНО!")

if __name__ == "__main__":
    dp.run_polling(bot)
