import logging
from selenium import webdriver
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os


load_dotenv()


# Объект бота
bot = Bot(token=os.environ.get("TOKEN"))
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

# Хэндлер на команду /test1
@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.get("https://hashdork.com/ru/best-heroku-alternatives/")
    await message.reply(driver.title)


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)