# Basic Discord Bot in Python By The Basic Bot Team!

# <--- DO NOT EDIT IMPORTS --->
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='b!') # If you have bots with ! change it to another prefix inside e.g 'prefixhere'
token = 'NDQ5ODk5NDM1ODU4NzIyODI3.Dg1lfg._LcCjjLGl2qUUq6ZdUaP-1DEKcg' # Get your token from https://discordapp.com/developers/applications/ You need to create a bot account and copy the bots token!
# <---- DO NOT EDIT --->
bot.remove_command('help')

# <--- Console Ready --->
@bot.event
async def on_ready():
    print("Basic Bot: Successfully Booted Up!")
    print("Errors: ")
    await bot.change_presence(game=discord.Game(name="BasicBot.xyz | b!help")) # You may change the bot of the game to what you want!

# <--- Welcome Message Event --->
@bot.event
async def on_member_join(member):
    welcome = discord.Object("CHANNELIDHERE") # Please Copy the ID Of the Welcome Channel and Put it inside e.g "channelid"
    embed = discord.Embed(title="Welcome to {0} Club, {1}".format(member.server.name, member.name), description="Make sure to check out the rules! \nBut enjoy your stay at {} !".format(member.server.name), color=0x0072ff) # To change the color find a hex color you want and put it after 0x
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text="Basic Bot by The Basic Bot Team")
    await bot.send_message(welcome, embed=embed)

@bot.event
async def on_member_remove(member):
    leave = discord.Object("CHANNELIDHERE") # Please Copy the ID Of the Welcome Channel and Put it inside e.g "channelid"
    embed = discord.Embed(title="Bye Bye {}!".format(member.name), description="We hope you had a Good Time at {}, See you soon!".format(member.server.name), color=0x0072ff)
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text="Basic Bot by The Basic Bot Team")
    await bot.send_message(leave, embed=embed)

@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Basic Bot Help", description="Here is all of the commands for Basic Bot!", color=0x0072ff)
    embed.add_field(name="Information Commands", value="b!ping - Ping Pong!\n!userinfo @user - Shows you info about the user!\n!serverinfo - Shows you info about the server!")
    embed.add_field(name="Staff Commands", value="b!purge number - Purges the amount of messages you want!\nb!mute @user - Mutes mentioned user. **MUST HAVE A ROLE CALLED Muted** \nb!unmute @user - Unmutes Mentioned User\nb!kick @user - Kicks mentioned user from the server\nb!ban @user - Bans mentioned user from the server")
    embed.add_field(name="Love Commands", value="b!Love - Love Someone\nb!Loveback - Love Someone back\nb!Marry - Ask Someone to marry you")
    embed.add_field(name="Misc Commands", value="b!Support - Need Any Help With Basic Bot?")
    embed.set_footer(text="Basic Bot by The Basic Bot Team")
    await bot.say(embed=embed)

# <--- Support --->
@bot.command(pass_context=True)
async def support(ctx):
    embed = discord.Embed(title="Support", description="Email: Support@BasicBot.xyz\nWebsite: BasicBot.xyz", color=0x0072ff)
    embed.set_footer(text="Basic Bot By The Basic Bot Team")
    await bot.say(embed=embed)

# <--- Love --->
@bot.command(pass_context=True)
async def love(ctx):
    embed = discord.Embed(title="I Love You :heart:", description="", color=0x0072ff)
    embed.set_footer(text="")
    await bot.say(embed=embed)

# <--- Love back --->
@bot.command(pass_context=True)
async def loveback(ctx):
    embed = discord.Embed(title="I Love You Too :heart:", description="", color=0x0072ff)
    embed.set_footer(text="")
    await bot.say(embed=embed)

# <--- Marry --->
@bot.command(pass_context=True)
async def marry(ctx):
    embed = discord.Embed(title="Will You Marry Me? :ring:", description="", color=0x0072ff)
    embed.set_footer(text="")
    await bot.say(embed=embed)

# <--- Ping --->
@bot.command(pass_context=True)
async def ping(ctx):
    embed = discord.Embed(title="Pong! :ping_pong:", description="", color=0x0072ff)
    embed.set_footer(text="Basic Bot by The Basic Bot Team")
    await bot.say(embed=embed)

# <--- Purge Command --->
@bot.command(pass_context=True)
async def purge(ctx, number):
    if ctx.message.author.server_permissions.manage_messages:
        mgs = []
        number = int(number)
        async for x in bot.logs_from(ctx.message.channel, limit = number):
            mgs.append(x)
        await bot.delete_messages(mgs)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff0000)
        embed.set_footer(text="Basic Bot by The Basic Bot Team")
        await bot.say(embed=embed)

# <--- Mute Command --->
@bot.command(pass_context=True)
async def mute(ctx, user: discord.Member):
    if ctx.message.author.server_permissions.kick_members:
        role = discord.utils.get(user.server.roles, name="Muted")
        embed = discord.Embed(title="{} has been muted!".format(user.name), description="When the user needs unmuting do !unmute @user!" , color=0x0072ff) # To change the color find a hex color you want and put it after 0x
        embed.set_footer(text="Basic Bot by The Basic Bot Team")
        embed.set_thumbnail(url=user.avatar_url)
        await bot.add_roles(user, role)
        await bot.say(embed=embed)
    else:
       embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff0000)
       embed.set_footer(text="Basic Bot by The Basic Bot Team")
       await bot.say(embed=embed)

# <--- Unmute Command --->
@bot.command(pass_context = True)
async def unmute(ctx, user: discord.Member):
    if ctx.message.author.server_permissions.kick_members:
        role = discord.utils.get(user.server.roles, name="Muted")
        embed = discord.Embed(title="{} has been unmuted".format(user.name), color=0x0072ff) # To change the color find a hex color you want and put it after 0x
        embed.set_footer(text="Basic Bot by The Basic Bot Team")
        embed.set_thumbnail(url=user.avatar_url)
        await bot.remove_roles(user, role)
        await bot.say(embed=embed)
    else:
       embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff0000)
       embed.set_footer(text="Basic Bot by The Basic Bot Team")
       await bot.say(embed=embed)

# <--- Kick Command --->
@bot.command(pass_context = True)
async def kick(ctx, user: discord.Member):
    if ctx.message.author.server_permissions.kick_members:
        embed = discord.Embed(title="Loading Kick System", description="Kicking {}".format(user.name), color=0x0072ff)
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text="Basic Bot by The Basic Bot Team")
        await bot.say(embed=embed)
        await bot.kick(user)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff0000)
        embed.set_footer(text="Basic Bot by The Basic Bot Team")
        await bot.say(embed=embed)

# <--- Ban Command --->
@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    if ctx.message.author.server_permissions.ban_members:
        embed = discord.Embed(title="Loading Ban System", description="Banning {}".format(user.name), color=0x0072ff)
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text="Basic Bot by The Basic Bot Team")
        await bot.say(embed=embed)
        await bot.ban(user)
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff0000)
        embed.set_footer(text="Basic Bot by The Basic Bot Team")
        await bot.say(embed=embed)

# <--- Userinfo Command --->
@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s Info".format(user.name), description="Here's What I could Find in Discord's Database!", color=0x0072ff)
    embed.add_field(name="Name", value=user.name)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Role", value=user.top_role, inline=True)
    embed.add_field(name="Joined At", value=user.joined_at, inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    embed.set_footer(text="Basic Bot by The Basic Bot Team")
    await bot.say(embed=embed)

# <--- Server Info Command --->
@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(title="{}'s Server Info".format(ctx.message.server.name), description="Here's What I could Find in Discord's Database!", color=0x0072ff)
    embed.add_field(name="Server Name", value=ctx.message.server.name)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    embed.set_footer(text="Basic Bot by The Basic Bot Team")
    await bot.say(embed=embed)

# <--- Bot Run --->
bot.run(token)
