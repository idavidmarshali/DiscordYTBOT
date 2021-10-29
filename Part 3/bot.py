import discord
from discord.ext import commands
import json, random, time

with open("config.json", "r") as file:
    data = json.load(file)
    token = data["token"]
    prefix = data["prefix"]
intent = discord.Intents.all()
bot = commands.Bot(command_prefix=prefix, intents=intent)


@bot.event
async def on_ready():
    print("Bot is ready to go")

@bot.command()
async def ping(ctx: commands.Context):
    await ctx.send(f"bot's ping is : {round(bot.latency * 1000)}")


@bot.command()
async def clear(ctx, amount=5):
    if ctx.author.guild_permissions.manage_messages:
        if amount > 100 or amount < 1:
            await ctx.send(f"you put {amount} in, but allowed range is 1 - 100")
            return
        textchannel: discord.TextChannel = ctx.channel
        await textchannel.purge(limit=amount+1)
        await ctx.send(f"deleted {amount} messages in {ctx.channel.name}")
    else:
        await ctx.reply("You dont have the needed permissions to call this command!")

@bot.command()
async def say(ctx: commands.Context, *, to_say: str):
    await ctx.send(to_say)
    await ctx.message.delete()

@bot.command()
async def coinflip(ctx: commands.Context):
    choices = ["shir", "khat"]
    await ctx.reply(f"**i flipped a coin and it turned out to be : **`{random.choice(choices)}`")

@bot.command()
async def moveall(ctx: commands.Context):
    if ctx.author.voice != None:
        moved_members = []
        for voice_channel in ctx.guild.voice_channels:
            for member in voice_channel.members:
                await member.move_to(ctx.author.voice.channel)
                moved_members.append(member)
        await ctx.reply(f"**Done!** `{len(moved_members)} members` were moved to our channel, aka `{ctx.author.voice.channel}`")
    else:
        await ctx.reply("**You're not in any VoiceChats!**")

@bot.command()
async def kick(ctx: commands.Context, member: discord.Member, *, reason: str = "None Given"):
    Ownembed = discord.Embed(title=f"User Kicked", description=f"**Kicked Users Name** : `{member.display_name}`\n"
                                                               f"**Kicked By** : `{ctx.author.display_name}`\n"
                                                               f"**Reason** : {reason}", color=0x57ff36)
    await member.kick(reason=reason)
    await ctx.send(embed=Ownembed)
bot.run(token)