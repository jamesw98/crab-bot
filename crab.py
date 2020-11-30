#!/usr/bin/env python3
import os
import random

from helper_functions import parse_cmd

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
    tfc = random.randint(1,1000) % 3 == 0
    
    # if the message has "crab" in it, there is a chance the bot 
    # will react with a crab emoji
    if "crab" in (message.content.lower()) and tfc:
        await message.add_reaction("🦀")

    # parses a crab command
    if (message.content[0:6] == "!crab "):
        cmd = message.content[6:]
        await message.channel.send(parse_cmd(cmd))
    
    if ("<@!598693241134645267>" in message.content):
        await message.channel.send("🦀How dare you ping your crab overlord!🦀")

client.run(TOKEN)