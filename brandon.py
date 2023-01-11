import discord

with open('key.txt') as f:
    key = f.readline()

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Initialized')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('brandon'):
        await message.channel.send('bruh')

client.run(key)
