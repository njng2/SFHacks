# Leonardo Matone
# Discord Bot interface

import discord
import os
from dotenv import load_dotenv
from stay_awake import stay_awake
import requests
import json

load_dotenv()
token = os.getenv('TOKEN')

# client
client = discord.Client()

# gimmick
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  jsonData = json.loads(response.text)
  quote = '"' + jsonData[0]['q'] + '" -' + jsonData[0]['a']
  return quote

@client.event # When bot establishes connection to Discord:
async def on_ready():
  print("We have logged on as {0.user}".format(client))

@client.event # When a new message is detected:
async def on_message(message):
  print("Received message")
  # if the message autor is the user, return.
  if message.author == client.user:
    return



  # gimmicks:
  if "inspiration" in message.content:
    quote = get_quote()
    await message.channel.send(quote)
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
client.run(token)