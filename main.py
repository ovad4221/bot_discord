import discord
from discord.ext import commands
from requests import get
import asyncio

TOKEN = "ODM3MzYxNzAzNjUyOTUwMDU4.YIrb2w.OJLw5m_8JoWcKBBc7qRnHK2Ornw"


class YLBotClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            print(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
            f'Привет, {member.name}!'
        )

    async def on_message(self, message):
        if message.author == self.user:
            return
        if "кот" in message.content.lower():
            link = get('https://api.thecatapi.com/v1/images/search').json()[0]['url']
            pikch = get(link).content
            if pikch:
                with open('pick.jpg', 'wb') as f:
                    f.write(pikch)
                await message.channel.send(file=discord.File(r'pick.jpg'))
        elif 'собака' in message.content.lower() or 'пес' in message.content.lower():
            link = get('https://dog.ceo/api/breeds/image/random').json()['message']
            pikch = get(link).content
            if pikch:
                with open('pick.jpg', 'wb') as f:
                    f.write(pikch)
                await message.channel.send(file=discord.File(r'pick.jpg'))
        else:
            await message.channel.send("Спасибо за сообщение")


client = YLBotClient()
client.run(TOKEN)
