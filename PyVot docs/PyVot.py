# Work with Python 3.6
import discord

TOKEN = 'NDgwODkyOTY1NTkwNDAxMDM0.Dlubag.D0WuDj2P5sgClMhQyro5DU44eoA'

client = discord.Client()


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    file = "bad words"
    archivo = open(file + ".txt", mode = 'r', encoding = 'utf-8') #Solo archivos codificados en utf-8
    lines = archivo.read()
    list = lines.split()
    archivo.close()
    if message.content.lower() in list:
        msg = 'Bad word detected! in '.format(message)
        await client.send_message(message.channel, msg)
        
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)











