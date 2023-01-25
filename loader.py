from config import CONFIG
import discord
from discord.ext import commands


intents = discord.Intents.default()  # Подключаем "Разрешения"
intents.message_content = True

bot = commands.Bot(command_prefix=CONFIG.BOT.PREFIX, intents=discord.Intents.all())
