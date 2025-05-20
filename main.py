import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.guilds = True
intents.members = True

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=intents,
            application_id=os.getenv("APP_ID")
        )
        self.initial_extensions = [
            "cogs.economy"
        ]

    async def setup_hook(self):
        for ext in self.initial_extensions:
            await self.load_extension(ext)
        await self.tree.sync()
        print("[+] Slash commands synced globally.")

bot = MyBot()

@bot.event
async def on_ready():
    print(f"[+] Logged in as {bot.user} ({bot.user.id})")

bot.run(TOKEN)
