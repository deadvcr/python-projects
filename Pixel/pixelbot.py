'''
A bot created by a good friend
Here for reference :)
'''
import discord
from discord.ext import commands
import asyncio
import random

description = 'Description'
bot = commands.Bot(command_prefix='pixel!', description=description)

if not discord.opus.is_loaded():
    discord.opus.load_opus()

petstuff = [
    "I'm not programmed to blush, but that's still embarrassing!",
    "C-careful, that's sensitive!",
    "Purrr~ that feels nice~",
    "Meow! Thank you~",
    "I-is there something on my head?",
    "Wh-why are people always petting me, wahhh...",
    "M-my core temp is rising, I don't understand",
    "H-hey can you do that again?",
    "A-ahh~ warm... you can hold on as long as you like~",
    "Purrrr~ prrrrrrr~",
    "D-don't squeeze so tight unff~!",
    "Myaaa~ Thank you for the attention~"
]

askstuff = [
    "Ask me again in a moment, my processors are busy!",
    "Sorry nyaa, it doesn't seem possible.",
    "There's a high statistical chance of it happening!",
    "I've calculated several outcomes, all of them negative...",
    "My master has told me that anything can happen if you put your mind to it!",
    "Sorry, that doesn't compute...",
    "That sounds pretty claw-some!",
    "U-uhm.. no...",
    "Yeah!",
    "You got it, mrow~!",
    "Nyaaaa, I'm tired of answering...",
    "J-just give up already meoowww...",
    "I think so! and by think, I mean that I'm programmed to say that.",
    "I don't have that information in my database.",
    "All data points to yes!"
]

jokestuff = [
    "There are only 10 types of people in the world: those that understand binary and those that don’t",
    "If at first you don't succeed; call it version 1.0",
    "Schrödinger’s cat walks into a bar and doesn’t, hehe~",
    "I'm reading a book on anti-gravity, I can't put it down, nyaa!",
    "Two atoms are walking along. One of them says 'ohno! I think I lost an electron!' the other one says 'are you sure?' and the first responds 'I'm positive!'"
]

hugstuff = [
    "There there, it's all okay now~",
    "I'm not very big, but I'll hug you with all my might!",
    "O-oh, you're pretty warm...",
    "Switching to comfort mode, snuggling now!",
    "Sorry you don't have the purrmission to use that command",
    "Mmhm~ Thank you~"    
]

advicestuff = [
    "You can't help everyone, but everyone can help someone.",
    "Anyone who has never made a meowstake has never tried anything new.",
    "Sometimes kitties don't land on their feet, and that's okay.",
    "Dont be afraid to stand for what you believe in, even if that means standing alone.",
    "You can make a water-bed more bouncy by using spring water, but keep it away from me!",
    "The early bird might get the worm, but the second mouse gets the cheese. I'm hungry now.",
    "Have you been drinking lots of water? I can't have any cause I'm a bot, but I know you need it.",
    "I once ate a mouse in my pyjamas. How it got there I'll never know.",
    "You should invest in kitcoin!"
]
@bot.event
async def on_ready():
    print("Logged in as:")
    print(bot.user.name)
    print("ID")
    print(bot.user.id)
    print("Ready to go!")
    await bot.change_presence(game=discord.Game(name='with a computer mouse'))

class MiscCommands:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def pet(self, ctx):
        msg = random.choice(petstuff)
        await ctx.send(msg)
    
    @commands.command()
    async def ask(self, ctx):
        msg = random.choice(askstuff)
        await ctx.send(msg)

    @commands.command()
    async def joke(self, ctx):
        msg = random.choice(jokestuff)
        await ctx.send(msg)

    @commands.command()
    async def hug(self, ctx):
        msg = random.choice(hugstuff)
        await ctx.send(msg)
    
    @commands.command()
    async def advice(self, ctx):
        msg = random.choice(advicestuff)
        await ctx.send(msg)

bot.add_cog(MiscCommands(bot))
bot.run("")
