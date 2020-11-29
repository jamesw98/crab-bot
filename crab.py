#!/usr/bin/env python3
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('SERVER_ID')

client = discord.Client()

@client.event
async def on_ready():
    for server in client.guilds:
        if server.name == SERVER:
            break

    print(
        f'{client.user} is connected to the following server:\n'
        f'{server.name}(id: {server.id})'
    )

client.run(TOKEN)