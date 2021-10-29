import discord
from discord.ext import commands


bot = commands.Bot(command_prefix=">")


@bot.event
async def on_ready():
    print("Bot is ready to go")


@bot.event
async def on_message(message: discord.Message):
    if not message.author.bot:
        if message.content == f"{bot.command_prefix}ping":
            ping = bot.latency * 1000 #ms
            await message.channel.send(f"Bots ping is : {round(ping)}ms")


bot.run("YOUR TOKEN")