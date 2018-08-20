# Works with Python 3.6
import discord

TOKEN = 'TOKEN GOES HERE'

client = discord.Client()


@client.event
async def on_message(message):
    # We do not want the bot to reply to itself
    if message.author == client.user:
        return
    file = "bad words"
    archivo = open(file + ".txt", mode = 'r', encoding = 'utf-8') 
    lines = archivo.read() #List is stored in variable lines
    list = lines.split() #List is split to create a list of words
    archivo.close()
    if message.content.lower() in list: #Content of the message made lowercase to make detection non case-sensitive
        msg = 'Bad word detected! in '.format(message)
        await client.send_message(message.channel, msg) #Send the message to notify word has been detected
        
async def on_ready(): #Lets you know when the bot is running
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)











