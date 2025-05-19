import os, discord
from discord.ext import commands

TOKEN      = os.getenv("DISCORD_TOKEN")
PHRASE     = "memento mori"

EMOJI_ID   = 1367615846259621908          # ← replace with your ID
custom     = None                        # will hold the Emoji object

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    global custom
    custom = bot.get_emoji(EMOJI_ID)     # returns discord.Emoji or None
    if not custom:
        print("Couldn’t find that emoji—check ID or permissions.")
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if PHRASE.lower() in message.content.lower() and custom:
        await message.add_reaction(custom)   # pass the Emoji object
    await bot.process_commands(message)

bot.run(TOKEN)
