# import random
# import sqlite3
import discord
# from discord import app_commands
from discord.ext import commands
import requests
from config import *
url = "https://csfloat.com/api/v1/"

# Create a bot instance
intents = discord.Intents.default()
intents.message_content = True
intents.messages = True


bot = commands.Bot(command_prefix="$", intents=intents, help_command=None)

async def get_bot():
    return bot

# Confirme la connexion
@bot.event
async def on_ready():
    print('Logged in as', bot.user)
    try:
        synced = await bot.tree.sync()
        print(f"Synced {synced} commands.")
    except Exception as e:
        print(f"Failed to sync commands: {e}")
    await bot.change_presence(activity=discord.Game(name="What's up guys, Quandale Dingle here!"))

# Commandes
    
@bot.tree.command(name='ping', description='Ping le bot')
async def ping(ctx):
    await ctx.response.send_message('Pong!')

@bot.tree.command(name='listings', description='Get Listings')
async def GetListings(ctx):
    response = requests.get(url + "listings") + "?key=" + FLOAT_API_KEY
    await ctx.response.send_message(response.json())

print(FLOAT_API_KEY)
headers = {
    'Authorization': f'Bearer {FLOAT_API_KEY}',
}
response = requests.get(f"{url}listings", headers=headers)
print(response.json())

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
response = requests.get("https://csfloat.com/api/v1/listings", headers=headers)
print(response.json())

@bot.tree.command(name='help', description='Affiche les commandes')

@bot.event
async def on_message(message):
    #ignore lui meme
    if message.author == bot.user:
        return

    if bot.user in message.mentions:
        ping()

bot.run(TOKEN) #run bot