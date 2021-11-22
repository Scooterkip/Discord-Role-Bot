from discord.ext import commands
from dislash import InteractionClient, ActionRow, Button, ButtonStyle
from discord.utils import get
import math
import discord

bot = commands.Bot(command_prefix="!")
slash = InteractionClient(bot)

configs = open("config.txt").read().splitlines()

magicWord = configs[0]
modName = configs[1]
gameCharacters = open("roles.txt").read().splitlines()
#print(gameCharacters)


@bot.command(pass_context = True)
async def mains(ctx):
    
    sender = ctx.message.author
    modRole = get(sender.guild.roles, name = modName)
    if modRole in sender.roles:
        return


    listsNeeded = math.ceil(len(gameCharacters) / 5)

    

    charButtons = []

    
    buttons = []
    for num, i in enumerate(gameCharacters):
        buttons.append(Button(style = ButtonStyle.primary, label = i))

    allLists = [buttons[i:i + 5] for i in range(0, len(buttons),5)]
    for num, i in enumerate(allLists):
        charButtons.append(ActionRow(*i))


    sentMsg = await ctx.send("Click a button to choose your main fighter!".format(ctx.message.author), components = charButtons)
    await ctx.message.delete()
   
    while True:
        def check(inter):
            return inter.message.id == sentMsg.id
        inter = await ctx.wait_for_button_click(check)
    
        roleName = inter.clicked_button.label
        requester = inter.author
        role = get(requester.guild.roles, name = roleName)
        await requester.add_roles(role)
        #await sentMsg.delete()


@bot.command(pass_context = True)
async def wdwdssw(ctx):
    await ctx.send("Nukes armed")
    await ctx.message.delete()

bot.run(magicWord)
