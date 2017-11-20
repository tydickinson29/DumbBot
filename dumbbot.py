import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random

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
	print('{} said:\"{}\" in #{}'.format(message.author.name, message.content, message.channel.name))

	if message.content.startswith('http') and message.author.id != message.server.me.id:
		yield from bot.send_message(discord.Object(id='380028343611031565'), message.content)
	elif (not message.content.startswith('!')) and message.channel.id == '381123909556371456':
		if message.author.id != '190198409150464001':
			yield from bot.delete_message(message)
	elif (not message.content.startswith('http')) and message.channel.id == '380028343611031565':
		if not message.attachments:
			yield from bot.delete_message(message)
	elif message.content == 'kk':
		yield from bot.send_message(message.channel, 'It\'s kkk ya fag')

	yield from bot.process_commands(message)

@bot.command()
@asyncio.coroutine
def ty():
	'''Just tells it as it is
	Ty is such a little bitch that it required a command'''
	yield from bot.say('Ty is a big ass bitch')

@bot.command()
@asyncio.coroutine
def brian():
	'''Just tells it as it is
	Brian is so swaggy that it required a command'''
	yield from bot.say('Brian is the swaggiest motherfucker')

@bot.command()
@asyncio.coroutine
def link(arg):
	'''Provides the link desired
	<arg> which link you want. Links are:
	  api
	  rl
	  ?
	  repo'''
	if arg == 'api':
		yield from bot.say('https://discordpy.readthedocs.io/en/latest/api.html')
	elif arg == 'rl':
		yield from bot.say('https://www.twitch.tv/rocketleague')
	elif arg == '?':
		yield from bot.say('https://www.youtube.com/watch?v=9G7aT6p_aGk')
	elif arg == 'repo':
		yield from bot.say('https://github.com/Brigoon/DumbBot')
	else:
		yield from bot.say('use \'/help link\' for valid links')

@bot.command()
@asyncio.coroutine
def bet(*args):
	'''YOU WANNA BET??
	<argn> nth bet string'''
	yield from bot.say(random.choice(args))

@bot.command(pass_context=True)
@asyncio.coroutine
def nuke(ctx):
	'''Only Brigoon can use this command
	removes all messages of a channel'''
	if ctx.message.author.id == '236886430616518666':
		yield from bot.purge_from(ctx.message.channel)

@bot.command(pass_context=True)
@asyncio.coroutine
def clean(ctx,arg):
	'''Only Brigoon can use this command
	<arg> is number of lines to remove'''
	if ctx.message.author.id == '236886430616518666':
		yield from bot.purge_from(ctx.message.channel,limit=int(arg))

bot.run("MzgwOTM1MzExNTQwMzU1MDcy.DPATMQ.AVpi46yuhrnzoaVKeNuVieWWXOM")