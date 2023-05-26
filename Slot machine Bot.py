import discord
import random
from discord.ext import commands

TOKEN = 'YOUR_BOT_TOKEN'

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command()
async def play(ctx, bet: int):
    symbols = ['🍒', '🍊', '🍋', '🍇', '🍉']
    emojis = [random.choice(symbols) for _ in range(3)]
    
    if bet <= 0:
        await ctx.send("Please place a bet greater than zero.")
        return

    if bet > 100:
        await ctx.send("The maximum bet amount is 100.")
        return

    result = f"{' '.join(emojis)}\n"

    if emojis[0] == emojis[1] == emojis[2]:
        winnings = bet * 10
        result += f"You won {winnings} coins! 🎉"
    else:
        winnings = -bet
        result += "Better luck next time. 😢"

    await ctx.send(result)

bot.run(TOKEN)
