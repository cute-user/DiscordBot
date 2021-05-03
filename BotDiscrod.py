import discord
from discord.ext import commands
import config

bot = commands.Bot(command_prefix = config.PREFIX)

rem_message = "rem_role"
Member = discord.Member
global message_g
@bot.event
async def on_ready():
    print ("Bot is ready")

@bot.event
async def on_message(message):
    print (message.author, " : ", message.content)
    await bot.process_commands(message)


@bot.command(pass_context=True)
async def rem_role (ctx, user: discord.Member, role: discord.Role):
        if rem_message in str(message_g.content):
            await message.delete()
            print ("Message: ", message.content, "Author: ", message.author, "Has been removed")
            return
        await Member.remove_roles(user, role)


@bot.command(pass_context=True)  
async def test(ctx, arg):  
    await ctx.send(arg)  

bot.run(config.TOKEN)