import discord
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from discord.ext import commands
import random
import asyncio
token = 'TOKEN HERE'
client = commands.Bot(command_prefix="!")

print('Bot is running')



def me(ctx):
	return ctx.author.id == USER_ID

@client.command()
@commands.check(me)
async def Add(ctx,role: discord.Role,user: discord.Member):
	await user.add_roles(role)
	await ctx.send('Role added successfully')

@client.command()
async def toss(ctx):
	x = random.randint(0, 100)
	if x > 51:
		await ctx.send('HEADS!')
	else:
		await ctx.send('TAILS!')


@client.command()
async def ready(ctx,arg):
	await client.change_presence(activity=discord.Game(arg))

@client.command()
async def help(ctx):
	await ctx.send('!server_init to start server')

@client.command()
async def server_init(ctx):
	await ctx.send('Server Starting up! Please allow the server 5-10 mins to start properly :)')
	#Chrome Driver
	PATH= "C:\Program Files (x86)\chromedriver.exe"
	driver = webdriver.Chrome(PATH)

	#GOTO Website
	driver.get('https://aternos.org/servers/')

	#Username input
	Username = driver.find_element_by_id('user')
	Username.send_keys('Username')

	#Password input
	Password = driver.find_element_by_id('password')
	Password.send_keys('Password')

	#Login
	Login = driver.find_element_by_id('login')
	Login.click()


	await asyncio.sleep(5)

	#Server Select
	server = driver.find_element_by_class_name('server-body')
	server.click()


	await asyncio.sleep(5)

	#Start Server
	Start = driver.find_element_by_id('start')
	Start.click()
	driver.quit()

	


# Run program on server
client.run(token)