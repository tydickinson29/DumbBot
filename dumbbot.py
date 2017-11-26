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
		yield from bot.send_message(message.channel, 'kkk*')

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
def ryan():
	'''Just tells it as it is
	Ryan is such a faggot, ugh, hate that guy'''
	yield from bot.say('Ryan is a faggot')

@bot.command()
@asyncio.coroutine
def link(*arg):
	'''Provides the link desired
	<arg> which link you want. Links are:
	  api
	  rl
	  ?
	  repo'''
	if len(arg) != 2:
		yield from bot.say('use \'/help link\'')
	elif arg == 'api':
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
	if len(args) > 1:
		yield from bot.say(random.choice(args))
	else:
		yield from bot.say('use \'/help bet\'')

@bot.command()
@asyncio.coroutine
def pokedex(*arg):
	'''Shows which Pokemon the user still needs to catch
	<arg1>:
	  brian: shows Brians needed pokemon
	  ty: shows Tys needed pokemon
	  example: /pokedex brian
	<arg1> <arg2>: adds a pokemon to the pokedex
	  <arg1> same as previous
	  <arg2> name of pokemon to be added
	  example: /pokedex brian Bulbasaur
	  	Yes, the capitalization is required'''
	if len(arg) == 1:
		dex = open("pokedex.txt","r")

		if arg[0]=='brian':
			file = open("brian_dex.txt","r")
			need = open("brian_need.txt","w")
		elif arg[0]=='ty':
			file = open("ty_dex.txt","r")
			need = open("ty_need.txt","w")

		cont = file.readlines()
		
		for line in dex:
			if not line in cont:
				need.write(line)
		need.close()

		if arg[0]=='brian':
			need = open("brian_need.txt","r")
		elif arg[0]=='ty':
			need = open("ty_need.txt","r")

		yield from bot.say('{} still needs:'.format(arg[0]))
		yield from bot.say(need.read())

		file.close()
		dex.close()
		need.close()
	elif len(arg) == 2:
		dex = open("pokedex.txt","r")
		complete = dex.readlines()
		dex.close()

		if arg[1] in complete:
			if arg[0]=='brian':
				file = open("brian_dex.txt","r")
			elif arg[0]=='ty':
				file = open("ty_dex.txt","r")

			cont = file.readlines()
			file.close()

			if arg[1] in cont:
				if arg[0]=='brian':
					file = open("brian_dex.txt","w")
				elif arg[0]=='ty':
					file = open("ty_dex.txt","w")

				for line in cont:
					file.write(line)
				file.write(arg[1])
				file.write('\n')
				file.close()
			else:
				yield from bot.say('This Pokemon is already registered in {}s Pokedex'.format(arg[0]))
		else:
			yield from bot.say('Invalid Pokemon, be sure you capitilized correctly')
	else:
		yield from bot.say('use \'/help pokedex\'')

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