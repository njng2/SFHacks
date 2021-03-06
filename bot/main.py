# Leonardo Matone
# Discord Bot interface

import discord
import os
from dotenv import load_dotenv
from stay_awake import stay_awake

load_dotenv()
token = os.getenv('TOKEN')

# client
bot = discord.Client()

@bot.event # When bot establishes connection to Discord:
async def on_ready():
  print("We have logged on as {0.user}".format(bot))

@bot.event # When a new message is detected:
async def on_message(message):
  print("Received message")
  if message.author == bot.user:
    return
  
  if message.content.startswith("hi"):
    await message.channel.send("hi")
  if message.content.startswith("ping"):
    await message.channel.send("pong")
  if message.content.startswith("bipitty"):
    await message.channel.send("bopitty")
  if "piss cum shit fart" in message.content or "bitch" in message.content:
    await message.channel.send("No foul language please.")
  if "NICE" in message.content:
    await message.channel.send("I know, right?")

stay_awake()
bot.run(token)