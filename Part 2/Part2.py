import discord
from discord.ext import commands
import json

with open("config.json", "r") as file:
    data = json.load(file)
    token = data["token"]
    prefix = data["prefix"]

bot = commands.Bot(command_prefix=prefix)


@bot.event
async def on_ready():
    print("Bot is ready to go")


@bot.command()
async def ping(ctx: commands.Context):
    await ctx.send(f"bot's ping is : {round(bot.latency * 1000)}")


@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5, x="hello"):
    if amount > 100 or amount < 1:
        await ctx.send(f"you put {amount} in, but allowed range is 1 - 100")
        return
    textchannel: discord.TextChannel = ctx.channel
    await textchannel.purge(limit=amount+1)
    await ctx.send(f"deleted {amount} messages in {ctx.channel.name}")



bot.run(token)