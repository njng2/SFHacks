# -*- coding: utf-8 -*-

import os
import discord

from dotenv import load_dotenv

load_dotenv()
token = os.genenv('TOKEN')

client = discord.Client()
#-----------------------------------------------------------------#

# returns integer number of assignments currently assigned
def get_num_assignmnents():
  return get_assignments().size() + 1

# returns array of assignments currently assigned (plus due date? 
# otherwise we will establish a second function to retrive due 
# dates for use in assignmentSchedule())
def get_assignments():
  result = []
  # retrieve assignments and add to result
  
  return result

#-----------------------------------------------------------------#

# inside of message testing:

# otherwise, test input for proper response
  if "checkDeadlines" in message.content:
    # output is type array
    output = get_assignments()

    i = 0
    while (i < output.size()):
      await message.channel.send()

#-----------------------------------------------------------------#

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord.')
    
client.run(token)