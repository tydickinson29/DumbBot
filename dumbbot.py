import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands

Client = discord.Client()
bot_prefix= "/"
bot  = commands.Bot(command_prefix=bot_prefix)

@bot.event
@asyncio.coroutine
def on_ready():
	print("Bot Online!")

@bot.event
@asyncio.coroutine
def on_message(message):
    if message.content.startswith('http') and message.author.id != message.server.me.id:
    	yield from bot.send_message(discord.Object(id='380028343611031565'), message.content)
    elif (not message.content.startswith('!')) and message.channel.name == 'stat_tracker':
    	if message.author.id != '190198409150464001':
    		yield from bot.delete_message(message)

    yield from bot.process_commands(message)

@bot.command()
@asyncio.coroutine
def ty():
	"""Just tells it as it is"""
	yield from bot.say('Ty is a big ass bitch')

@bot.command()
@asyncio.coroutine
def brian():
	"""Just tells it as it is"""
	yield from bot.say('Brian is the swaggiest motherfucker')

@bot.command(pass_context=True)
@asyncio.coroutine
def nuke(ctx):
	"""Only Brigoon can use this command: removes all messages of a channel"""
	if ctx.message.author.id == '236886430616518666':
		yield from bot.purge_from(ctx.message.channel)

@bot.command(pass_context=True)
@asyncio.coroutine
def clean(ctx,arg):
	"""Only Brigoon can use this command: <arg> is number lines to remove"""
	if ctx.message.author.id == '236886430616518666':
		yield from bot.purge_from(ctx.message.channel,limit=int(arg))

bot.run("MzgwOTM1MzExNTQwMzU1MDcy.DPATMQ.AVpi46yuhrnzoaVKeNuVieWWXOM")