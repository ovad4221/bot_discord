import random

import discord
from discord.ext import commands
from requests import get
import asyncio

TOKEN = "ODM3MzYxNzAzNjUyOTUwMDU4.YIrb2w.lUBFf41MluUhL9fxqjepIW6JCpw"
emoji = [i for i in range(128513, 128591)]
user_balls = bot_balls = 0


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
        if any(i.isdigit() for i in message.content.split()) or message.content == '/stop':
            global emoji, bot_balls, user_balls

            if not emoji or message.content == '/stop':
                if not emoji:
                    await message.channel.send("Вроде как смайлики закончились): Заново?")
                await message.channel.send(f"Score: You - {user_balls}; bot - {bot_balls}")
                if bot_balls > user_balls:
                    await message.channel.send("Победитель - бот!")
                else:
                    await message.channel.send("Так и быть, победа твоя!")
                emoji = [i for i in range(128513, 128591)]
                user_balls = bot_balls = 0
                return

            user_choice = -1
            for i in message.content.split():
                if i.isdigit():
                    user_choice = int(i) % len(emoji)
                    break
            bot_choice = random.choice(range(len(emoji)))
            while bot_choice == user_choice:
                bot_choice = random.choice(range(len(emoji)))
            if bot_choice > user_choice:
                bot_balls += 1
            else:
                user_balls += 1
            await message.channel.send(f"Your emoji: {chr(emoji[user_choice])}")
            await message.channel.send(f"Bot emoji: {chr(emoji[bot_choice])}")
            await message.channel.send(f"Score: You - {user_balls}; bot - {bot_balls}")
            emoji.pop(bot_choice)
            emoji.pop(user_choice)
            return
        else:
            await message.channel.send("Давай все же с числом, а то игра не получится")
            return


client = YLBotClient()
client.run(TOKEN)
