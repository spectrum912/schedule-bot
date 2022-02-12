from aiogram import Bot,Dispatcher,executor
from config import bot_token
import asyncio

loop = asyncio.get_event_loop()
bot = Bot(bot_token,parse_mode="HTML")
dp = Dispatcher(bot,loop=loop) #обработчик

if __name__ == "__main__":




# API_LINK = "https://api.telegram.org/bot5167627424:AAFGOxsZa3YH4egdKF2FjDBsrsbh37rhqRs"




