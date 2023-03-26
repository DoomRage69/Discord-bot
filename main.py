import os
import discord
from dotenv import load_dotenv

load_dotenv()  # Load the .env file that contains the bot token
TOKEN = os.getenv('DISCORD_TOKEN')  # Retrieve the bot token from the .env file
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.send(f'Welcome to the server, {member.name}!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!kick'):
        if message.author.guild_permissions.kick_members:
            member = message.mentions[0]
            await member.kick(reason='Kicked by bot.')
            await message.channel.send(f'{member.mention} has been kicked from the server.')
        else:
            await message.channel.send("You don't have permission to use that command.")

    elif message.content.startswith('!ban'):
        if message.author.guild_permissions.ban_members:
            member = message.mentions[0]
            await member.ban(reason='Banned by bot.')
            await message.channel.send(f'{member.mention} has been banned from the server.')
        else:
            await message.channel.send("You don't have permission to use that command.")

    elif message.content.startswith('!mute'):
        if message.author.guild_permissions.manage_roles:
            role = discord.utils.get(message.guild.roles, name='Muted')
            member = message.mentions[0]
            await member.add_roles(role)
            await message.channel.send(f'{member.mention} has been muted.')
        else:
            await message.channel.send("You don't have permission to use that command.")

    elif message.content.startswith('!unmute'):
        if message.author.guild_permissions.manage_roles:
            role = discord.utils.get(message.guild.roles, name='Muted')
            member = message.mentions[0]
            await member.remove_roles(role)
            await message.channel.send(f'{member.mention} has been unmuted.')
        else:
            await message.channel.send("You don't have permission to use that command.")

client.run(TOKEN)
