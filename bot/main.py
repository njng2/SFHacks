# Authors: Leonardo Matone, Nancy Ng
# Date: 3.5.21
# Title: Discord Bot interface

import discord
import os
import requests
import json
import quickstart
from dotenv import load_dotenv
from discord.ext import commands
from SFHacks.calendar.quickstart import addEvent, removeEvent, viewCalendar

load_dotenv()
token = os.getenv('TOKEN')

# setup the client
client = discord.Client()

@client.event # When bot establishes connection to Discord:
async def on_ready():
  print("We have logged on as {0.user}".format(client))

# inspiration gimmick
inspirational = ["inspiration", "inspirational", "inspire", "inspired"]
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  jsonData = json.loads(response.text)
  quote = '"' + jsonData[0]['q'] + '" -' + jsonData[0]['a']
  return quote

@client.event # When a new message is detected:
async def on_message(message):
  print(message.author)
  # if the message author is the user, return.
  if message.author == client.user:
    return

  # actions:
  if message.content.startswith("#"):
    if "add" in message.content:
      newAssignment = message.content[4:]
      await message.channel.send("New assignment added to calendar: " + newAssignment)

  # gimmicks:
  for word in inspirational:
    if word in message.content:
      quote = get_quote()
      await message.channel.send(quote)
      break
  if message.content == '$remindme':
    await message.channel.send('Hello {}'.format(message.author.mention))

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

@client.event
async def remind

# client = MyClient()
client.run(token)