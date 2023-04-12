# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = "MTA5NTYwMzcyNTczMDU5NDg3Nw.GPJskW.pWHqNjvBYpuc3HwafttoW5u52KWzXSnbyqaar4"
GUILD = "general"

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Who are you?":
        content = "I'm a ROWBOUGHT!"
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    await message.channel.send(content)


client.run(TOKEN)