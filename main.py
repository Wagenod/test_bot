import logging
from selenium import webdriver
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

PROXY_URL = "http://proxy.server:3128"
load_dotenv()

bot = Bot(token=os.environ.get("TOKEN"), proxy=PROXY_URL)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com")
    await message.reply(driver.title)

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)
