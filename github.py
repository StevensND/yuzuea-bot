import discord
import requests
import sys
import socket
from discord.ext import commands, tasks

TOKEN = 'YOUR DISCORD APP TOKEN HERE'
GITHUB_API_URL = 'https://api.github.com/repos/pineappleEA/pineapple-src/releases/latest'
CHECK_INTERVAL = 600  # Check interval in seconds (Right now it is set at 10 minutes)

intents = discord.Intents.default()
intents.all()
intents.message_content = True
intents.guild_messages = True

client = commands.Bot(command_prefix='!', intents=intents)
notification_channels = {}

def is_internet_available():
    try:
        # Try to connect to a Google server to verify internet connection
        socket.create_connection(('8.8.8.8', 53), timeout=5)
        return True
    except OSError:
        pass
    return False

@client.event
async def on_ready():
    print('Bot connected as {0.user}'.format(client))
    check_releases.start()  # Start release checking

@tasks.loop(seconds=CHECK_INTERVAL)
async def check_releases():
    if not is_internet_available():
        print('No Internet connection.')
        return

    try:
        response = requests.get(GITHUB_API_URL)
        response.raise_for_status()  # Raises an exception if the request is not successful
        release_data = response.json()
        tag_name = release_data['tag_name']

        last_version = get_last_version()
        if last_version != tag_name:
            update_last_version(tag_name)
            for guild_id, channel_id in notification_channels.items():
                guild = client.get_guild(guild_id)
                if guild is not None:
                    channel = guild.get_channel(channel_id)
                    if channel is not None:
                        release_url = release_data['html_url']
                        release_body = release_data['body']
                        await channel.send(f'**New version available!** | {tag_name}\n{release_url}\n{release_body}')
    except (requests.RequestException, KeyError) as e:
        print('Failed to fetch release information:', str(e))

def get_last_version():
    try:
        with open('last_version.txt', 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return ''

def update_last_version(version):
    with open('last_version.txt', 'w') as file:
        file.write(version)

@client.command()
async def eastatus(ctx):
    await ctx.send('Bot is running and operational.')

@client.command()
async def ealatest(ctx):
    if not is_internet_available():
        await ctx.send('No Internet connection.')
        return

    try:
        response = requests.get(GITHUB_API_URL)
        response.raise_for_status()  # Raises an exception if the request is not successful
        release_data = response.json()
        tag_name = release_data['tag_name']
        await ctx.send(f'Latest version available: {tag_name}')
    except (requests.RequestException, KeyError) as e:
        await ctx.send('Failed to fetch release information.')

@client.command()
async def eareleases(ctx):
    await ctx.send('All available releases here: https://github.com/pineappleEA/pineapple-src/releases')

@client.event
async def on_error(event, *args, **kwargs):
    error_message = f'Error occurred in event {event}: {sys.exc_info()}'
    print(error_message)
    if error_channel_id:
        channel = client.get_channel(error_channel_id)
        await channel.send(error_message)

@client.event
async def on_disconnect():
    print('Bot disconnected from Discord.')

@client.event
async def on_connect():
    print('Bot reconnected to Discord.')

# Command to set the notification channel
@client.command()
async def setnotificationchannel(ctx, channel_id):
    guild_id = ctx.guild.id
    notification_channels[guild_id] = int(channel_id)
    await ctx.send(f'Notification channel set to {channel_id}.')

# Command to set the error channel
@client.command()
async def seterrorchannel(ctx, channel_id):
    global error_channel_id
    error_channel_id = int(channel_id)
    await ctx.send(f'Error channel set to {channel_id}.')

client.run(TOKEN)