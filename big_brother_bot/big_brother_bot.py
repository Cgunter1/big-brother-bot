import discord
import json

with open("./discord_key.json") as fs:
    json_buff = fs.read()

token = json.loads(json_buff)["token"]


client = discord.Client()


@client.event
async def on_ready():
    print("{0.user} is running now...".format(client))


@client.event
async def on_message(message):
    print(message.content)

client.run(token)
