# 904287797865766913 app id
# OTA0Mjg3Nzk3ODY1NzY2OTEz.YX5Vow.T1DWmX9ZGkD8KO51h59MIoIfW14 tpken
#481036818496 permission
#https://discord.com/api/oauth2/authorize?client_id=904287797865766913&permissions=412317349952&scope=bot aut

import discord
import asyncio
import os

from discord.ext import commands
from datetime import datetime, timedelta

from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
from song import songAPI

from dotenv import load_dotenv
load_dotenv()
token=os.getenv('TOKEN')


message_lastseen = datetime.now()
message2_lastseen = datetime.now()



bot = commands.Bot(command_prefix='!', help_command = None)

aboutSong=songAPI()

#bot online
@bot.event
async def on_ready():
    print(f"Logged in as{bot.user}")

@bot.command()
async def test(ctx, *, par):
    await ctx.channel.send("Your type{0}".format(par))

@bot.command()
async def help(ctx):
    image = 'https://i.pinimg.com/originals/b8/5d/0b/b85d0b60c0283fe7fd3f34cd0df87f15.png'
    emBed = discord.Embed(title="tutorial bot help",description= 'all available bot command', color=0x42f5a7)
    emBed.add_field(name="!help", value='get help command', inline=False )
    emBed.add_field(name="!test", value='respond to message that you have sent', inline=False )
    emBed.add_field(name="!bot", value='introduce bot', inline=False )
    emBed.add_field(name="!todolist", value='list of homework or test', inline=False )
    emBed.set_thumbnail(url=image)
    emBed.set_image(url='https://thumbs.dreamstime.com/b/how-can-i-help-you-banner-assistent-how-can-i-help-you-banner-assistent-vector-150785994.jpg')
    emBed.set_author(name='bot',icon_url=image)
    

    await ctx.channel.send(embed=emBed)


@bot.command()
async def todolist(ctx):
    emBed = discord.Embed(title="Homework & test",description= 'All works that need to be done', color=0x42f5a7)
    emBed.add_field(name="python", value='homework in goedu', inline=False )
    emBed.add_field(name="work2", value='description', inline=False )
    emBed.add_field(name="work3", value='description', inline=False )
    emBed.set_image(url='https://d18lkz4dllo6v2.cloudfront.net/cumulus_uploads/entry/2018-07-30/homework.jpg')
    
    await ctx.channel.send(embed=emBed)



@bot.command()
async def link(ctx):
    image = ''
    emBed = discord.Embed(title="Class access",description= 'all the link to the class', color=0x42f5a7)
    emBed.add_field(name="Cal", value='https://zoom.us/j/5455256896', inline=False )
    emBed.add_field(name="Python", value='https://meet.google.com/bri-xukh-vfz', inline=False )
    emBed.set_author(name='Link board',icon_url=image)
    emBed.set_footer(text='click the link to get in',icon_url=image)

    await ctx.channel.send(embed=emBed)

@bot.command()
async def schedule(ctx):
    emBed=discord.Embed(title="Class schedule",color=0x42f5a7)
    emBed.set_image(url='https://cdn.discordapp.com/attachments/916686558432743444/919152540644417546/272F6CCF-0746-4BA2-9272-6C131A97781E.jpg')
    await ctx.channel.send(embed=emBed)

@bot.command()
async def remind(ctx,time,*,task):
    def convert(time):
        pos=['s','m','h','d']
        time_dict = {"s":1,"m":60,"h":3600,"d":3600*24}
        unit=time[-1]

        if unit not in pos:
            return -1
        try:
            val = int(time[:-1])
        except:
            return -2

        return val * time_dict[unit]

    convert_time = convert(time)
    time=convert_time
    half_time=convert_time/2
    quater_time=half_time/2

    qday=quater_time//(24*3600)

    quater_time=quater_time%(24*3600)
    qhour=quater_time//3600

    quater_time%=3600
    qminutes=quater_time//60
    quater_time%=60
    qseconds=quater_time


    hday=half_time//(24*3600)

    half_time=half_time%(24*3600)
    hhour=half_time//3600

    half_time%=3600
    hminutes=half_time//60
    half_time%=60
    hseconds=half_time

    day=convert_time//(24*3600)

    convert_time=convert_time%(24*3600)
    hour=convert_time//3600

    convert_time%=3600
    minutes=convert_time//60
    convert_time%=60
    seconds=convert_time


    if convert_time== -1:
        await ctx.send("your input is not correct")
        return

    if convert_time == -2:
        await ctx.send("It must be aN InTeGEr U DumB BItCh")
        return

    emBed = discord.Embed(title="Reminder started",color=0x42f5a7)
    emBed.add_field(name="Reminder",value=task,inline=False)
    emBed.add_field(name="From",value=ctx.author.mention,inline=False)
    emBed.add_field(name="Time left",value=f'{day} days {hour} hours {minutes} minutes {seconds} seconds', inline=False)
    await ctx.channel.send(embed=emBed)
    

    await asyncio.sleep(time/2)
    emBed = discord.Embed(title="Reminder",color=0x42f5a7)
    emBed.add_field(name="Reminder",value=task,inline=False)
    emBed.add_field(name="From",value=ctx.author.mention,inline=False)
    if hday == 0.0:
        hday = int(hday)
    if hhour == 0.0:
        hhour=int(hhour)
    if hminutes== 0.0:
        hminutes=int(hminutes)
    if hseconds== 0.0:
        hseconds==int(hseconds)
    emBed.add_field(name='Time Left',value=f'{hday} days {hhour} hours {hminutes} minutes {hseconds} seconds',inline=False)

    await ctx.channel.send(embed=emBed)

    await asyncio.sleep(time/4)
    emBed = discord.Embed(title="Reminder to slap the shit out of your lazy ass",color=0x42f5a7)
    emBed.add_field(name="Reminder",value=task,inline=False)
    emBed.add_field(name="From",value=ctx.author.mention,inline=False)
    if qday == 0.0:
        qday = int(qday)
    if qhour == 0.0:
        qhour=int(qhour)
    if qminutes== 0.0:
        qminutes=int(qminutes)
    if qseconds== 0.0:
        qseconds==int(qseconds)
    emBed.add_field(name="Time left",value=f'{qday} days {qhour} hours {qminutes} minutes {qseconds} seconds',inline=False)
    await ctx.channel.send(embed=emBed)

    await asyncio.sleep(half_time)
    emBed = discord.Embed(title="Reminder finished",color=0x42f5a7)
    emBed.add_field(name="Reminder",value=task,inline=False)
    emBed.add_field(name="From",value=ctx.author.mention,inline=False)
    emBed.add_field(name="Time left",value=f'0 days 0 hours 0 minutes 0 seconds',inline=False)
    await ctx.channel.send(embed=emBed)

@bot.command()
async def poll(ctx,*,message):
    emBed = discord.Embed(title="Poll",description=f"{message}", color=0x42f5a7)
    msg=await ctx.channel.send(embed=emBed)
    await msg.add_reactiion('👍🏻')
    await msg.add_reactiion('👎🏻')


#bot interact message
@bot.event
async def on_message(message):
    global message_lastseen,message2_lastseen
    if message.content == "!Hello":
        print(message.channel)
        await  message.channel.send('Hello ' + str(message.author.name))

    elif message.content == '!bye':
        print(message.channel)
        await message.channel.send('Good bye')
    elif message.content == '!bot' and datetime.now() >= message_lastseen:
        message_lastseen = datetime.now() +timedelta(seconds=5)
        print(message.channel)
        await message.channel.send('I am '+str(bot.user.name))
        print('{0} calling user when {1} and you can use {2}'.format(message.author.name,datetime.now(),message_lastseen))
    elif message.content =="!user" and datetime.now() >= message2_lastseen:
        message2_lastseen = datetime.now() +timedelta(seconds=5)
        await message.channel.send('You are ' + str(message.author.name))

    elif message.content == '!logout':
        await bot.logout()

    await bot.process_commands(message)



@bot.command()
async def play(ctx, *, search:str):
    await aboutSong.play(ctx,search)

@bot.command()
async def stop(ctx):
    await aboutSong.stop(ctx)

@bot.command()
async def pause(ctx):
    await aboutSong.pause(ctx)
    

@bot.command()
async def resume(ctx):
    await aboutSong.resume(ctx)
    
@bot.command()
async def leave(ctx):
    await aboutSong.leave(ctx)

@bot.command()
async def skip(ctx):
    await aboutSong.skip(ctx)

@bot.command()
async def queueList(ctx):
    await aboutSong.queueList(ctx)









bot.run(token)