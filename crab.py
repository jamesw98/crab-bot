#!/usr/bin/env python3
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print("Time for crab!")

@client.event
async def on_message(message):
    if (message.author == client.user):
        return
    
    # whether or not it is time for crab or not
    tfc = random.randint(1,1000) % 100 == 0
    
    # if the message has
    if "crab" in (message.content.lower()) and tfc:
        await message.add_reaction("🦀")
        
client.run(TOKEN)