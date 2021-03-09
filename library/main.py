# This example requires the 'members' privileged intents
from discord.ext import commands
import discord
import random

description = '''This is a bot to welcome new people to the server, respond to some messages and to grant low level 
permissions '''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.event
async def on_member_join(member):
    """Checks when a new member joins and welcomes them to the server with a random greeting"""
    ## These are Star Wars, Still Game and Shrek in order.
    listOfGreetings = ["Hello there,", "Weclome,", "OH HELLO THERE,"]
    guild = member.guild
    if guild.system_channel is not None:
        result = random.randint(0, 2)
        to_send = listOfGreetings[result] + ' {0.mention}!'.format(member)
        await guild.system_channel.send(to_send)


@bot.command()
async def hello(ctx):
    """Replies to hello by saying hello back"""
    await ctx.message.channel.send('Hello {0.author.mention}'.format(ctx.message))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)


@bot.command(pass_context=True)
async def addrole(ctx, role: discord.Role, member: discord.member = None):
    member = member or ctx.message.author
    auth = ctx.message.content
    if auth == '!addrole Admin':
        # this command only works on my bot server ATM.
        await ctx.message.channel.send("I am not allowed to assign that role. <@&780521077842640919> Is this person "
                                       "allowed this role?")
        return
    else:
        await member.add_roles(role)


f = open("./botToken", "r")
token = f.readline()
f.close()


bot.run(token)
