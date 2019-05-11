import random
import discord
from discord.ext import commands

sampleroll = '2d100' # roll two 20-sided die
MAX_ROLL = 100
# Discord ID 576823697671847937
# Discord Token NTc2ODIzNjk3NjcxODQ3OTM3.XNcHIA.AkgQvKXvXXAcEdIEPdN_VEaN5tI
# Permissions integer 67648
# https://discordapp.com/oauth2/authorize?client_id=576823697671847937&scope=bot&permissions=67648


client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(f'{message.channel}: {message.author}: {message.author.name}: {message.content}')

@client.command(aliases=['r'])
async def roll(ctx, *, rollvalue):
    # Parse the roll into number of dice and sides on the dice
    dice, sided = map(int, rollvalue.split('d'))

    # check to make sure there's not too big of a number
    if (dice and sided) <= MAX_ROLL:
        # Generate a random roll for each dice
        results = [random.randint(1,sided) for _ in range(dice)]

        await ctx.send(f'You rolled {results}')
        print(results)

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


client.run("NTc2ODIzNjk3NjcxODQ3OTM3.XNcHIA.AkgQvKXvXXAcEdIEPdN_VEaN5tI")




