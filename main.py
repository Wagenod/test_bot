import os
import logging
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types
from db_context_manager import Database

load_dotenv()

#bot = Bot(token=os.environ.get("BOT_TOKEN"), proxy=os.environ.get("PROXY_URL"))
bot = Bot(token=os.environ.get("BOT_TOKEN"))
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
try:
    service = Service(ChromeDriverManager().install())
except ValueError as error:
    service = Service(executable_path="chromedriver.exe")

driver = webdriver.Chrome(service=service, options=options)

@dp.message_handler(commands="test1")
async def cmd_test1(message: types.Message):
    driver.get("https://www.google.com")
    with Database() as db:
        n_records = db.execute("select count(*) from AUTHOR;").fetchone()[0]
        db.execute(f"insert into AUTHOR(FIO, AGE) values('', {random.randint(20, 100)});")
    await message.reply(f"driver title = {driver.title} \n total records in DB = {n_records}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
