import discord
import requests
import json
from discord.ext import commands

TOKEN = 'Your Token here'

intents = discord.Intents.default()
intents.typing = True
intents.presences = True
intents.messages = True
intents.guilds = True

bot = commands.Bot(command_prefix='!', intents=intents)

def get_random_joke():
    response = requests.get('https://official-joke-api.appspot.com/random_joke')
    joke_data = json.loads(response.text)
    joke = joke_data['setup'] + '\n' + joke_data['punchline']
    return joke

@bot.event
async def on_ready():
    print('Logged in as {0}'.format(bot.user.name))


@bot.command(name='joke')
async def joke_command(ctx):
    joke = get_random_joke()
    await ctx.send(joke)


bot.run(TOKEN)

