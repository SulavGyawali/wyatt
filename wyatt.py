import discord
from discord.ext import commands
import random


client = commands.Bot(command_prefix='"')
client.remove_command('help')
link=["https://i.redd.it/2ioociazg5o61.jpg","https://i.redd.it/l9cp8y6wa7o61.jpg","https://i.redd.it/y8cp17tdq6o61.png",
      "https://i.redd.it/ke27ae2557o61.gif","https://i.redd.it/2o2ukyhpeao61.png","https://i.redd.it/x53jf37fl5o61.gif"
    "https://i.redd.it/xdp6moof69o61.jpg","https://i.redd.it/05vpmyt179o61.jpg","https://i.redd.it/lgnzkihaw5o61.jpg",
    "https://i.redd.it/aenjl4s2b8o61.jpg","https://i.redd.it/0m3xlw4167o61.jpg"
    ]


filtered_words = ['porn']
client.owner_id = 709314105126682716

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Wyatt.gg'))
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(msg):
    for word in filtered_words:
        if word in msg.content:
            await msg.delete()

    await client.process_commands(msg)

@client.command()
async def meme(cxt):
    embed = discord.Embed(title="Meme")
    embed.set_image(url= random.choice(link))
    await cxt.send(embed=embed)

@client.command()
async def ping(cxt):
    embed = discord.Embed(title=f'Pong! {round(client.latency * 1000)} ms')
    await cxt.send(embed=embed)


@client.command(aliases=['8ball'])
async def _8ball(cxt, *, message):
    response = [
        "without a doubt",
        "ofcourse",
        "nope",
        "hmm...",
        "let me think about that",
        "no",
        "as i see it,yes",
        "cannot predict now",
        "very doubtful"]
    embed = discord.Embed(title =f"Question: {message}", description= f"**Answer:  {random.choice(response)}**")
    await cxt.send(embed=embed)

@client.event
async def on_command_error(cxt, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed= discord.Embed(title='<:error:824273757786865665>Type all required anrguments')
        await cxt.send(embed=embed)
    elif isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(title=('<:error:824273757786865665>You dont have the permission '))
        await cxt.send(embed=embed)
    elif isinstance(error, commands.NotOwner):
        embed= discord.Embed(title='<:error:824273757786865665>You are not the owner  ')
        await cxt.send(embed=embed)
    elif isinstance(error, commands.BotMissingPermissions):
        embed = discord.Embed(title='<:error:824273757786865665>The user is mod/admin')
        await cxt.send(embed=embed)
    elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title='<:error:824273757786865665>User not found')
        await cxt.send(embed=embed)
    elif isinstance(error, commands.CommandInvokeError
                ):
        embed = discord.Embed(title='<:error:824273757786865665>Missing permission')
        await cxt.send(embed=embed)
    elif isinstance(error, commands.CommandNotFound):
        print("a")
    else:
        raise error


@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(cxt, amount: int):
    await cxt.channel.purge(limit=amount)
    embed = discord.Embed(title=f'<:done:824650780182970460> Purged {amount} messages')
    await cxt.send(embed=embed)


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(cxt, member: discord.Member, *, reason=None):
    id = 679677267164921866
    if client.owner_id == member.id:
        embed = discord.Embed(title="<:error:824273757786865665>He is the owner")
        await cxt.send(embed=embed)
    elif member.id == id:
        embed = discord.Embed(title="<:error:824273757786865665>He is the owner")
        await cxt.send(embed=embed)
    else:
        await member.kick(reason=reason)
        embed = discord.Embed(title=f'<:done:824650780182970460> User has been kicked  ')
        await cxt.send(embed =embed)
        await member.send(f'You have been kicked from yhe server ,reason: {reason}')



@client.command()
@commands.has_permissions(ban_members=True)
async def ban(cxt, member: discord.Member, *, reason=None):
    id= 679677267164921866
    if client.owner_id == member.id:
        embed = discord.Embed(title="<:error:824273757786865665>He is the owner")
        await cxt.send(embed=embed)
    elif member.id == id:
        embed = discord.Embed(title="<:error:824273757786865665>He is the owner")
        await cxt.send(embed=embed)
    else:
        await member.ban(reason=reason)
        embed = discord.Embed(title=f'<:done:824650780182970460> User has been banned ')
        await cxt.send(embed=embed)
        await member.send(f'you have been banned from the server , resaon:{reason}')


@client.command()
@commands.has_permissions(ban_members=True)
async def unban(cxt, member):
    banned_users = await cxt.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await cxt.guild.unban(user)
            embed = discord.Embed(title=f'<:done:824650780182970460> unbanned {user}')
            await cxt.send(embed=embed)
            return


@client.command()
@commands.has_permissions(kick_members=True)
async def warn(cxt, member: discord.Member, *, reason):
    id = 679677267164921866
    if client.owner_id == member.id:
        embed = discord.Embed(title="<:error:824273757786865665>He is the owner")
        await cxt.send(embed=embed)
    elif member.id == id:
        embed = discord.Embed(title="<:error:824273757786865665>He is the owner")
        await cxt.send(embed=embed)
    else:
        embed = discord.Embed(title=f'<:done:824650780182970460> User was warned')
        await cxt.send(embed=embed)



@client.command()
async def whois(cxt, member : discord.Member = None):
    if not member:
        member = cxt.author

    roles = [role for role in member.roles]
    roles = roles[::-1]
    embed = discord.Embed(title=member.nick)
    embed.set_thumbnail(url=member.avatar_url)
    embed.add_field(name="Joined", value=member.joined_at.strftime("%a, %d, %B, %Y, %I:%M  %p"),inline=True)
    embed.add_field(name="Registered", value=member.created_at.strftime("%a, %d, %B, %Y, %I:%M  %p"))
    embed.add_field(name=f"Roles [{len(roles)}]", value=" ".join(role.mention for role in roles), inline=False)
    await cxt.send(embed=embed)

@client.command()
async def av(cxt, member: discord.Member = None):
    if not member:
        member = cxt.author

    embed = discord.Embed(title=member.name, description='**Avatar**', color=discord.Color.darker_grey())
    embed.set_image(url=member.avatar_url)
    embed.set_footer(icon_url=cxt.author.avatar_url, text=f'Requested by {cxt.author.name} ')
    await cxt.send(embed=embed)


@client.command()
@commands.is_owner()
async def device(cxt, member: discord.Member):
    if member.is_on_mobile():
        await cxt.send('mobile')
        await cxt.send(member.mobile_status)
    else:
        await cxt.send(member.status)
        await cxt.send(member.web_status)


@client.command()
async def id(cxt):
    await cxt.send(client.owner_id)


@client.command()
async def help(cxt):
    await cxt.send('<:pepeno:815218820611440680>')


@client.command()
async def membercount(cxt, member : discord.Member = None):
    if not member:
        member = cxt.author

    embed= discord.Embed(title= 'Members', description= member.guild.member_count)
    await cxt.send(embed=embed)

client.run('NzEwMDE4MjUwMTI5Mjc2OTc5.XruWBg.FjkespfusxNv8njGMTexn5Kr6B0')

