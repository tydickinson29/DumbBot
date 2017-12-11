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
	elif 'yeet' in message.content.lower():
		yield from bot.add_reaction(message,'\N{EYES}')

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
def pokedex(name='broken',gen='0'):
	'''Shows which Pokemon the user still needs to catch
	<arg1>:
	  brian: shows Brians needed pokemon
	  ty: shows Tys needed pokemon
	  both: shows what both Ty and Brian do not have
	  example: /pokedex brian
	<arg1> <arg2>:
	  <arg1> same as previous
	  <arg2> generation to be shown
	  example: /pokedex brian 1
	<arg1> <arg2>: adds a pokemon to the pokedex
	  <arg1> same as previous
	  <arg2> name of pokemon to be added
	  example: /pokedex brian bulbasaur
	<arg1> <arg2>: registers a new user
	  <arg1> register
	  <arg2> name of registee
	  example: /pokedex register brian'''

	try:
		name = name.lower()
		gen = gen.lower()
		approved_file = open('text/approved.txt','r')
		approved = approved_file.readlines()
		approved_file.close()
		# Adds a new user to the approved list
		if name=='register':
			if gen+'\n' in approved:
				yield from bot.say(gen[0].upper()+gen[1:].lower()+' has already been approved')
				return

			new_dex = open('text/'+gen+'_dex.txt','w')
			new_dex.close()
			new_approved = open('text/approved.txt','a')
			new_approved.write(gen+'\n')
			new_approved.close()
			yield from bot.say(gen[0].upper()+gen[1:]+' has been approved!')
			
		# Outputs what <arg1> needs with the option to restrict the generation
		elif gen=='0' or gen=='1' or gen=='2' or gen=='3':
			if not (((name+'\n') in approved) or name=='both'):
				yield from bot.say(name[0].upper()+name[1:].lower()+' is not a valid user')
				return

			need = open('text/'+name+'_need.txt','w')
			if gen=='0':
				dex1 = open('text/pokedex_gen1.txt','r')
				dex2 = open('text/pokedex_gen2.txt','r')
				dex3 = open('text/pokedex_gen3.txt','r')
				dex = [dex1, dex2, dex3]
			else:
				dex1 = open('text/pokedex_gen'+gen+'.txt','r')
				dex = [dex1]

			if name=='both':
				ty_dex = open('text/ty_dex.txt','r')
				brian_dex = open('text/brian_dex.txt','r')
				ty_cont = ty_dex.readlines()
				brian_cont = brian_dex.readlines()
				check = [ty_cont, brian_cont]
				ty_dex.close()
				brian_dex.close()
				addition = ''
			else:
				check_dex = open('text/'+name+'_dex.txt','r')
				cont = check_dex.readlines()
				check = [cont]
				check_dex.close()
				addition = 's'

			for i in range(len(dex)):
				if len(dex)>1:
					need.write('@@@@@@@@@@ GEN '+str(i+1)+' @@@@@@@@@@\n')
				for line in dex[i]:
					if len(check)==2:
						if not ((line in check[0]) or (line in check[1])):
							if 'mr. mime' in line:
								need.write('Mr. Mime\n')
							else:
								need.write(line[0].upper()+line[1:])
					else:
						if not (line in check[0]):
							if 'mr. mime' in line:
								need.write('Mr. Mime\n')
							else:
								need.write(line[0].upper()+line[1:])
				dex[i].close()
			need.close()

			need = open('text/'+name+'_need.txt','r')

			yield from bot.say(name[0].upper()+name[1:].lower()+' still need'+addition+':')
			read = need.read()
			need.close()
			if(len(read)==0):
				yield from bot.say('Nothing! You got all of them!')
			else:
				yield from bot.say(read)

		# Adds <arg2> to <arg1>s pokedex
		else:
			if not ((name+'\n') in approved):
				yield from bot.say(name[0].upper()+name[1:].lower()+' is not a valid user')
				return

			dex1 = open('text/pokedex_gen1.txt','r')
			dex2 = open('text/pokedex_gen2.txt','r')
			dex3 = open('text/pokedex_gen3.txt','r')
			dex = [dex1, dex2, dex3]

			pokemon = (gen+'\n')

			valid = False

			for i in range(len(dex)):
				if pokemon in dex[i]:
					valid = True
					break

			if valid:
				check_dex = open('text/'+name+'_dex.txt','r')
				check = check_dex.readlines()
				check_dex.close()

				if pokemon not in check:
					file = open('text/'+name+'_dex.txt','a')
					file.write(pokemon)
					file.close()
					yield from bot.say(pokemon[0].upper()+pokemon[1:].rstrip()+' has been succesfully added!')
				else:
					yield from bot.say(pokemon[0].upper()+pokemon[1:].rstrip()+' is already in '+name[0].upper()+name[1:]+'\'s Pokedex')

			else:
				yield from bot.say(pokemon[0].upper()+pokemon[1:].rstrip()+' is not a valid Pokemon')

	except:
		yield from bot.say('use \'/help pokedex\'')
		raise

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