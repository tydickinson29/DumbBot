import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random

Client = discord.Client()
bot_prefix= "/"
bot  = commands.Bot(command_prefix=bot_prefix)

def update_dex(name):
	dex1 = open("text/pokedex_gen1.txt","r")
	dex2 = open("text/pokedex_gen2.txt","r")
	dex3 = open("text/pokedex_gen3.txt","r")

	if name=='brian':
		file = open("text/brian_dex.txt","r")
		need = open("text/brian_need.txt","w")
	elif name=='ty':
		file = open("text/ty_dex.txt","r")
		need = open("text/ty_need.txt","w")

	cont = file.readlines()
		
	need.write("@@@@@@@@@@ GEN 1 @@@@@@@@@@\n")
	for line in dex1:
		if not line in cont:
			need.write(line)
	need.write("@@@@@@@@@@ GEN 2 @@@@@@@@@@\n")
	for line in dex2:
		if not line in cont:
			need.write(line)
	need.write("@@@@@@@@@@ GEN 3 @@@@@@@@@@\n")
	for line in dex3:
		if not line in cont:
			need.write(line)
	need.close()

	file.close()
	dex1.close()
	dex2.close()
	dex3.close()

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
def bryony():
	'''Just tells it as it is'''
	yield from bot.say('''Bryony is a savage
and needs to stop dabbing''')

@bot.command()
@asyncio.coroutine
def alex():
	'''Just tells it as it is'''
	yield from bot.say('Alex is the most badass of them all')

@bot.command()
@asyncio.coroutine
def link(*arg):
	'''Provides the link desired
	<arg> which link you want. Links are:
	  api
	  rl
	  ?
	  repo
	  nests
	  map (only works in ann arbor)'''
	if arg[0] == 'api':
		yield from bot.say('https://discordpy.readthedocs.io/en/latest/api.html')
	elif arg[0] == 'rl':
		yield from bot.say('https://www.twitch.tv/rocketleague')
	elif arg[0] == '?':
		yield from bot.say('https://www.youtube.com/watch?v=9G7aT6p_aGk')
	elif arg[0] == 'repo':
		yield from bot.say('https://github.com/Brigoon/DumbBot')
	elif arg[0] == 'nests':
		yield from bot.say('https://thesilphroad.com/atlas')
	elif arg[0] == 'map':
		yield from bot.say('https://www.joshwoodward.com/mod/pokemon/map/#1111000030')
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
	  both: shows what both Ty and Brian do not have
	  example: /pokedex brian
	<arg1> <arg2>: adds a pokemon to the pokedex
	  <arg1> same as previous
	  <arg2> name of pokemon to be added
	  example: /pokedex brian Bulbasaur
	    Yes, the capitalization is required'''
	if (len(arg)==1) and (arg[0]=='both'):
		dex_brian = open("text/brian_dex.txt","r")
		dex_ty = open("text/ty_dex.txt","r")
		dex1 = open("text/pokedex_gen1.txt","r")
		dex2 = open("text/pokedex_gen2.txt","r")
		dex3 = open("text/pokedex_gen3.txt","r")
		need = open("text/both_need.txt","w")

		cont_brian = dex_brian.readlines()
		cont_ty = dex_ty.readlines()

		need.write("@@@@@@@@@@ GEN 1 @@@@@@@@@@\n")
		for line in dex1:
			if not ((line in cont_brian) or (line in cont_ty)):
				need.write(line)
		need.write("@@@@@@@@@@ GEN 2 @@@@@@@@@@\n")
		for line in dex2:
			if not ((line in cont_brian) or (line in cont_ty)):
				need.write(line)
		need.write("@@@@@@@@@@ GEN 3 @@@@@@@@@@\n")
		for line in dex3:
			if not ((line in cont_brian) or (line in cont_ty)):
				need.write(line)

		dex_brian.close()
		dex_ty.close()
		dex1.close()
		dex2.close()
		dex3.close()
		need.close()

		need = open("text/both_need.txt","r")

		yield from bot.say('Both still need:')
		yield from bot.say(need.read())

		need.close()

	elif len(arg) == 1:
		update_dex(arg[0])

		if arg[0]=='brian':
			need = open("text/brian_need.txt","r")
		elif arg[0]=='ty':
			need = open("text/ty_need.txt","r")

		yield from bot.say("{} still needs:".format(arg[0]))
		yield from bot.say(need.read())

		need.close()

	elif len(arg) == 2:
		dex1 = open("text/pokedex_gen1.txt","r")
		dex2 = open("text/pokedex_gen2.txt","r")
		dex3 = open("text/pokedex_gen3.txt","r")
		pokedex1 = dex1.readlines()
		pokedex2 = dex2.readlines()
		pokedex3 = dex3.readlines()
		dex1.close()
		dex2.close()
		dex3.close()

		valid = False

		for i in range(len(pokedex1)):
			if arg[1] == pokedex1[i].rstrip():
				valid = True
				break
		for i in range(len(pokedex2)):
			if (arg[1] == pokedex2[i].rstrip()) or valid:
				valid = True
				break
		for i in range(len(pokedex3)):
			if (arg[1] == pokedex3[i].rstrip()) or valid:
				valid = True
				break

		if valid:
			if arg[0]=='brian':
				file = open("text/brian_dex.txt","r")
			elif arg[0]=='ty':
				file = open("text/ty_dex.txt","r")

			cont = file.readlines()
			file.close()

			for j in range(len(cont)):
				if arg[1] == cont[j].rstrip():
					valid = False
					break

			if valid:
				if arg[0]=='brian':
					file = open("text/brian_dex.txt","a")
				elif arg[0]=='ty':
					file = open("text/ty_dex.txt","a")

				file.write(arg[1])
				file.write('\n')
				file.close()
				yield from bot.say('{} successfully added!'.format(arg[1]))
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

bot_ID_txt = open("text/bot_ID.txt","r")
bot_ID = bot_ID_txt.read()
bot_ID_txt.close()
bot.run(bot_ID)