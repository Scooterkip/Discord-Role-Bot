This should be simple enough to work, and I've made it so that it can be set up with customized roles without opening up the code.

Setting up python:
1) Install python
2) Run command 'pip install discord.py'
3) Run command 'pip install discord-ext-bot'
3) Run command 'pip install dislash.py'
4) Run command 'pip install --upgrade discord_buttons'

You should have everything installed now

Setting up userbot: (skip this if you know how to make a userbot)
1) Go to https://discord.com/developers/applications
2) click 'New Application'
3) give you bot a pretty name
4) click on that newly made bot
5) go down to the 'OAuth2' menu
6) go down to the 'URL Generator' submenu
7) Select 'bot' in the 'scopes' menu
8) Select 'Administrator' under the 'bot permissions' menu (I don't really know all the permissions it needs, reading/sending/deleting messages and adding roles?)
9) Copy the link under 'generated url'
10) copy paste that url into your browser and select your desired server

Configuring the bot:
1) Go into roles.txt, each line is a role in your server (can be up to 25 at the moment)
2) The text line for the role HAS to be the role's name exactly, otherwise you'll get errors
3) Go into config.txt
4) The first line is the bot's token
5) The second line is the moderator role that can send the menu
4) Run BotStart.exe

In server:
1) Go into whichever channel you want the menu in
2) Have someone with your mod role write '!mains'
3) The message from the mod will auto delete and the bot will send the menu, allowing anyone to set their main character roles!

If there are any issues you can mention them in the github or email me at scootakip@gmail.com
If you're rep and you have any issues you know my discord handle

If you want you can modify the code to your liking I don't give a shit