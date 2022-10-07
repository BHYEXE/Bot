import discord
from discord.ext import commands




TOKEN = 'MTAyNjg1MDQwMzkzNTA4MDUxMA.GqZDNj.QyYC6Q3J49JtqSR1XKdeh7GWIxXUM2Pvcmj7n0'
client = commands.Bot(command_prefix='!', intents = discord.Intents.all())





class Menu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    @discord.ui.button(label="Ip", style=discord.ButtonStyle.green)
    async def menu1(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Here are the IP files", file=discord.File('Login_files.txt'))
        print('')
        print('Ip files send!')
        print('')


    @discord.ui.button(label="Quit", style=discord.ButtonStyle.red)
    async def menu2(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.edit_message(content="thanks for using!")
        self.value = False
        self.stop()



@client.command()
async def menu(ctx):
    view = Menu()
    await ctx.reply('hello welcome to the B.H.Y menu', view=view)
    print('')
    print('Bot is Activated!')
    print('')


@client.command()
async def about(ctx):
    await ctx.reply('this is the B.H.Y discord bot, we are currently in a (Testing phase) i make hacks for you easy/simple to use on Friends, A Enemy and more!')
    await ctx.send('-the current version is 1.0 more hacks are comming later')
    print('')
    print('Bot is Activated!')
    print('')


            




@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))


    
client.run(TOKEN)
