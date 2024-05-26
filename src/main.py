from os import getenv

from dotenv import load_dotenv
from loguru import logger
from vkbottle.bot import Bot, Message

load_dotenv()
logger.disable("vkbottle")

VK_TOKEN = getenv("VK_TOKEN")
bot = Bot(VK_TOKEN)


@bot.on.message()
async def logging_handler(message: Message):
    user = await message.get_user()
    try:
        full_name = user.first_name + " " + user.last_name
    except TypeError:
        full_name = "[group]"
    msg = message.text or "[attachment]"
    logger.info(f"{full_name}: {msg}")


if __name__ == "__main__":
    logger.info("Starting script...")
    bot.run_forever()
