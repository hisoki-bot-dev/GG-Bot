import discord
import random
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle

#Command Prefix

client = commands.Bot(command_prefix = 'gg ')

#Client Events

#Status - RickRoll (Bass Version by Davie504)
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name="TenZ", url=f"https://www.youtube.com/watch?v=uv69KSmLhic"))
    print('GG Bot is online!')

@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left the server.')

#Fun Commands

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                 "It is decidely so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "Outlook not so good.",
                 "Very doubtful."]
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

@client.command()
async def dadjoke(ctx):
    responses = ["What do you call a dad joke that falls on its head? A dud pun!",
                 "On Thanksgiving, why did the turkey cross the table? To get to the other sides!",
                 "A ham sandwich walks into a bar and the bartender says... Sorry, we don't serve food here!",
                 "What do you call a mermaid on a roof? Aerial!",
                 "What does a highlighter say when it answers the phone? Yello!!",
                 "I am wrapping Christmas presents. Let's put on some rap music.",
                 "What's Irish and comes out in the spring? Paddy O'Furniture.",
                 "What do you call an  orange parrot? A carrot.",
                 "What's the opposite of water? Yellow snow.",
                 "I'll call you later. Don't call me later, call me Dad!",
                 "How do celebrities stay cool? They have many fans.",
                 "What's Forrest Gump's Facebook password? 1forest1.",
                 "What do you call it when Batman skips church? Christian Bale.",
                 "What time did the man go to the dentist? Tooth hurt-y.",
                 "Did you hear about the man who fell into an upholstery machine? He's fully recovered.",
                 "Why didn't the melons get married? Because they cantaloupe.",
                 "What kind of egg did the evil chicken lay? A deviled egg.",
                 "Why did the coach go to the bank? To get his quarter back.",
                 "Why does Snoop Dogg always carry an umbrella? Fo' Drizzle.",
                 "What did the fisherman say to the magician? Pick a cod, any cod.",
                 "What do you call a fake noodle? An impasta.",
                 "Which is faster, hot or cold? Hot, because you can catch a cold.",
                 "How do you organize a space party? You planet.",
                 "Did you know that milk is the fastest liquid on earth? It's pasteurized before you even see it.",
                 "Why are skeletons so calm? Because nothing gets under their skin.",
                 "What did one ocean say to the other ocean? Nothing, they just waved.",
                 "What does a baby computer call his father? Data.",
                 "Did you hear about the power outlet who got into a fight with a power cord? He thought he could socket to him.",
                 "Why are elevator jokes so good? They work on so many levels.",
                 "Why can't a leopard hide? Because he's always spotted.",
                 "How do moths swim? Using the butterfly stroke.",
                 "How many tickles does it take to make an octopus laugh? 10 tickles.",
                 "Do you know the story about the chicken that crossed the border? Me neither, I couldn't follow it.",
                 "I made a pencil with two erasers. It was pointless.",
                 "How do you make a Kleenex dance? Put a little boogie in it!",
                 "What do you get from a pampered cow? Spoiled milk!",
                 "What do you call an illegally parked frog? Toad.",
                 "Where do baby cats learn to swim? The kitty pool.",
                 "Why are spiders so smart? They can find everything on the web.",
                 "How can a leopard change his spots? By moving."]
    await ctx.send(f'{random.choice(responses)}')

@client.command()
async def rickroll(ctx):
    await ctx.send("Wanna RickRoll your friends? Grab this link: https://www.tomorrowtides.com/discord-music-bot-rythm-shuts-down1.html")

@client.command(aliases=['rs', 'randServ'])
async def randomServer(ctx):
    responses = ["https://discord.gg/programming",
                 "https://discord.gg/apex-legends",
                 "https://discord.gg/discord-townhall",
                 "https://discord.gg/valorant",
                 "https://discord.gg/QdMCFzyu6C",
                 "https://discord.gg/clashroyale",
                 "https://discord.gg/asphalt9",
                 "https://discord.gg/rocketleague",
                 "https://discord.gg/djs",
                 "https://discord.gg/minecraft",
                 "https://discord.gg/roblox",
                 "https://discord.gg/microsoft",
                 "https://discord.gg/fortnite",
                 "https://discord.gg/lofigirl",
                 "https://discord.gg/genshinimpact",
                 "https://discord.gg/cookie",
                 "https://discord.gg/lgbt"]
    await ctx.send(f'{random.choice(responses)}')

@client.command(aliases=['rw', 'randWeb', 'randSite'])
async def randomWebsite(ctx):
    responses = ["https://atom.io",
                 "https://discord.gg",
                 "https://visualstudio.microsoft.com",
                 "https://code.visualstudio.com",
                 "https://startpage.com",
                 "https://duckduckgo.com",
                 "https://brave.com",
                 "https://raspberrypi.org",
                 "https://magpi.cc",
                 "https://theprogrammershangout.com",
                 "https://manjaro.org",
                 "https://youtube.com",
                 "https://rumble.com",
                 "https://bitchute.com",
                 "https://microsoft.com",
                 "https://spotify.com",
                 "https://github.com/hisoki-bot-dev",
                 "https://qwertykids.com"]
    await ctx.send(f'{random.choice(responses)}')

@client.command()
async def fortuneCookie(ctx):
    responses = ["You will buy jeans.",
                 "You will read this message.",
                 "You will die one day.",
                 "You will breathe fresh air (probably. Can't tell with lockdown.)",
                 "You will be stuck in lockdown for one more day.",
                 "You will invite me to your server: https://discord.com/api/oauth2/authorize?client_id=883577201289736202&permissions=8&scope=bot",
                 "You will go to my Github repo: https://github.com/hisoki-bot-dev/GG-Bot",
                 "You will add my creator on VALORANT: royalety#6969",
                 "You will add my creator on Discord: Homer Not-a-SIMPson#6562",
                 "You will download Manjaro and stop using Microsoft products: https://manjaro.org",
                 "You will not eat this fortune cookie.",
                 "Bruh. I am not a psychic. Why you coming to me for advice? Idiot!"]

#Moderation Commands

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

#Setup Commands

@client.command()
async def setup(ctx):
    await ctx.send("Thank you for using **GG Bot - The Multipurpose Gamer Bot**. Here is a list of commands => ping; 8ball; dadjoke; rickroll; clear (Admin only); kick (Admin only); ban (Admin Only); unban (Admin Only); setup (Admin Only). For help on these commands use `gg helpMe_[command]`. Please pin this message to the channel. My prefix is `gg`. Invite me: https://discord.com/api/oauth2/authorize?client_id=883577201289736202&permissions=8&scope=bot Thank you!")


#Help Commands - helpMe

@client.command()
async def helpMe(ctx):
    await ctx.send("Use `gg helpMe_command` to grab help on a command. Permissions Needed: `Send Messages`")

@client.command()
async def helpMe_ping(ctx):
    await ctx.send("Replies with the latency of our bot! Permissions Needed: `Send Messages`")

@client.command()
async def helpMe_8ball(ctx):
    await ctx.send("Ask a question to the Magic 8ball - Get an answer. You may like it, you may not! Permissions Needed: `Send Messages`")

@client.command()
async def helpMe_dadjoke(ctx):
    await ctx.send("Sends a random dadjoke to the chat! Permissions Needed: `Send Messages`")

@client.command()
async def helpMe_rickroll(ctx):
    await ctx.send("Sends a link to a RickRoll. RickRoll your friends with this, but make sure they didn't see this message! Permissions Needed: `Send Messages`")

@client.command()
async def helpMe_clear(ctx):
    await ctx.send("Clears a certain amount of messages in the channel. Default amount is 5. Permissions Needed: `Administrator`")

@client.command()
async def helpMe_kick(ctx):
    await ctx.send("Kicks a member from this server. Permissions Needed: `Administrator`")

@client.command()
async def helpMe_ban(ctx):
    await ctx.send("Bans a member from this server. Permissions Needed: `Administrator`")

@client.command()
async def helpMe_unban(ctx):
    await ctx.send("Unbans a member from this server. Only if the Admins/Mods are feeling nice! Permissions Needed: `Administrator`")

@client.command()
async def helpMe_setup(ctx):
    await ctx.send("Set up your bot with this function. Permissions Needed: `Administrator`")


client.run('Token Goes Here')
