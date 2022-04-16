from multiprocessing import context
from time import sleep
import discord
from discord.ext import commands
import os
import random
import asyncio
import datetime
from urllib import response
from bs4 import BeautifulSoup
import requests
from pprint import pprint

TOKEN = os.environ['TOKEN']
SRCLanguage=os.environ['SRC']
DSTLanguage=os.environ['DST']

intents =discord.Intents.default()
intents.members = True

client=commands.Bot(command_prefix='+',intents=intents)


@client.event
async def on_ready():
    print('成功登入')

@client.event
async def on_member_join(member):
    mention = member.mention
    channel = client.get_channel(859699464569749535)
    await channel.send(f'{mention} 歡迎光臨')

@client.event
async def on_member_remove(member):
    mention = member.mention
    channel = client.get_channel(859699464569749535)
    await channel.send(f'{mention}高歌離席了 有緣再見')

@client.event
async def on_message(message):

    if message.author.bot:
        return

    if '早安' in message.content:
        await message.channel.send('Good morning 祝你今天順利')

    if '午安' in message.content:
        await message.channel.send('甲霸沒')

    if '晚安' in message.content:
        await message.channel.send('Good night 祝你有個好夢')

    if '裸男' and '請客' in message.content:
        await message.channel.send('yabe 裸男請客')

    if message.content.startswith('+神奇bot'):
        mention = message.author.mention
        meg = ["Yes!","No!","窩才不告訴你勒","阿這"]
        random_word = random.choice(meg)
        await message.channel.send(f'{mention} {random_word}')


    if message.content == '+歐氣測試':
        mention = message.author.mention
        e = random.randrange(101)
        if e == 0:
            emoji = client.get_emoji(854750834025037845)
            w = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDSpeRTmtZEDWnqtjD0f4-JZyQZDAd4qHwnSRXi1JAGGb5SCJxTx6kLiICPc3VRv6_-t0&usqp=CAU"
        elif  0 < e < 20:
            emoji = client.get_emoji(854750834025037845)
            w = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXel6hTStrB9vY_VH4sLb-21UP0OSvpNWL5w&usqp=CAU"
        elif 20 <= e < 40:
            emoji = client.get_emoji(919555859950997554)
            w = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAxyUcVB1-OoSSDbxNRFW9kGcFHsEYBDNgkQ&usqp=CAU"
        elif 40 <= e < 60:
            emoji = client.get_emoji(919555859950997554)
            w = "https://api.jikipedia.com/upload/8d472d1104ae8bafbff376c758b3b5e4_75.jpg"
        elif 60 <= e <80:
            emoji = client.get_emoji(902956721142628443)
            w = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS5OSGpk-M0fsFYfpVl0dZUH9Y06TLCz9tT0w&usqp=CAU"
        elif 80 <= e <100:
            emoji = client.get_emoji(915656063326511184)
            w = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1cLHv_rtBRJonm94PepkgDhV3eZNTG4cerA&usqp=CAU"
        elif e == 100:
            emoji = client.get_emoji(894245845912932392)
            w = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQaQmyYAyp_0RMIGlTminHKZicqeVzz8jLEXu3fGHEa7T4lL6YBwnmWrSJBRqC4YqLzRSA&usqp=CAU"
        await message.channel.send('{0} 歐氣指數:{1:3d}{2}'.format(mention,e,emoji))
        await message.channel.send(w)

    if message.content == "+日期":
        await message.channel.send(f'今天日期:{datetime.date.today()}')
                            
    id = 857862909446193152
    if message.author.id == id:
        
        if message.content.startswith('+圖片'):
            mention = message.author.mention
            tmp = message.content.split(" ",2)
            if len(tmp) == 1:
                await message.channel.send(f'{mention}你的tag去哪了?')
            elif tmp[1] == 'loli':
                await message.channel.send(f'{mention}你這個ㄌㄌㄎ')
            else:
                input_image = tmp[1]
                img_file = []
                response = requests.get(f"https://yande.re/post?tags={input_image}")
                soup = BeautifulSoup(response.text, 'html.parser')
                result = soup.find_all("span",class_ = "plid",limit = 20)
                if len(result) == 0 :
                    await message.channel.send(f'{mention} 搜尋結果不存在')
                else:
                    await message.channel.send(mention)
                    for n in range(5):
                        item = random.choice(result)
                        img_file.append(item)
                        result.remove(item)
                    for title in img_file:
                        title = title.text[4:]
                        response = requests.get(title)
                        soup = BeautifulSoup(response.text, 'html.parser')
                        item = soup.find("img",id = "image")
                        await message.channel.send(item.get("src"))
                        await asyncio.sleep(1)
            
        if message.content.startswith('+車車'):
            tmp = message.content.split(" ",2)
            if len(tmp) == 1:
                await message.channel.send("不給車號怎麼開")
            else:
                input_image = tmp[1]
                response = requests.get(f"https://nhentai.net/g/{input_image}/")
                soup = BeautifulSoup(response.text, 'html.parser')
                result = soup.find_all("img",class_="lazyload")
                for title in result:
                    await message.channel.send(title.get("data-src"))
                    await asyncio.sleep(1)

        if message.content == "bot狐你不乖":
            await message.channel.send('https://memeprod.sgp1.digitaloceanspaces.com/user-wtf/1580208626048.jpg')


        if message.content.startswith('更改狀態online'):
            tmp = message.content.split(" ",2)
            if len(tmp) == 1:
                await message.channel.send("想改成什麼")
            else:
                game = discord.Game(tmp[1])
                await message.channel.send(f'已改成狀態{tmp[1]}')
                await client.change_presence(status = discord.Status.online , activity = game)

        if message.content.startswith('更改狀態idle'):
            tmp = message.content.split(" ",2)
            if len(tmp) == 1:
                await message.channel.send("想改成什麼")
            else:
                game = discord.Game(tmp[1])
                await message.channel.send(f'已改成狀態{tmp[1]}')
                await client.change_presence(status = discord.Status.idle , activity = game)

client.run(TOKEN)
