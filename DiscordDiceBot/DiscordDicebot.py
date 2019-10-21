from discord.ext import commands
import discord
import random
import itertools

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def d(ctx, *args):
    con = 0
    end = 0
    rolls = []
    lessthen = False
    morethen = False
    sim = False
    raw_roll = "".join(args)
    #raw_roll = "2d6"
    raw_len = len(raw_roll)

    x = raw_roll.find(">")
    y = raw_roll.find("<")
    if x != -1:
        morethen = True
        con = raw_roll[x + 1:raw_len]
        con = int(con.strip())
        z = x
    elif y != -1:
        lessthen = True
        con = raw_roll[y + 1:raw_len]
        con = int(con.strip())
        z = x

    if raw_roll[0] == "(":
        endofroll = raw_roll.find(")")
        roll = raw_roll[1:endofroll]
        add = True
    else:
        add = False
        if morethen or lessthen == True:
            roll = raw_roll[0:z]
        else:
            roll = raw_roll

    #print(roll)
    length = len(roll)
    result = roll.find('d') + 1
    print(length)
    print(result)
    print("")
    print(morethen)
    print("")
    num1 = int(roll[0:result - 1])
    num2 = int(roll[result:length + 1])
    print("Seperation:")
    print("")
    print("How many die: ", num1)
    print("")
    print("How many sides on each die:", num2)
    print("")

    for i in range(num1):
        result = random.randint(1, num2)
        if add == True:
            end += result
            rolls.append(result)
        else:
            rolls.append(result)

    ########################################
    #if morethen == True and add == False:
    #        sim = True
    #        for x in range(num1):
    #            if con > x:
    #                print(con)
    #                print(x)
    #                print("Success in total")
    #            else:
    #                print("Fail in total")

    #if lessthen == True and add == False:
    #        sim = True
    #        for x in range(num1):
    #            if con < x:
    #                print(con)
    #                print(x)
    #                print("Success in total")
    #            else:
    #                print("Fail in total
    await ctx.send(ctx.message.author.mention)
    await ctx.send('Results of roll: ' + ', '.join(str(x) for x in rolls))
    if end != 0:
        await ctx.send("In total: " + str(end))

    if morethen == True and sim == False:
        if con <= end:
            await ctx.send("Success")
            print("1")
        else:
            await ctx.send("Fail!")
            print("2")
    if lessthen == True and sim == False:
        if con >= end:
            await ctx.send("Success")
            print("3")
        else:
            await ctx.send("Fail!")



@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="nice bot", description="Nicest bot there is ever.", color=0xeee657)

    # give info about you here
    embed.add_field(name="Author", value="Nerve_Corrosion")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite link](<insert your OAuth invitation link here>)")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="nice bot", description="A Very Nice bot. List of commands are:", color=0xeee657)
    embed.add_field(name="$add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="$multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="$greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="$cat", value="Gives a cute cat gif to lighten up the mood.", inline=False)
    embed.add_field(name="$info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="$help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

bot.run('Token here')
