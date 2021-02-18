import discord
import requests
import json
import os

client=discord.Client()

def get_quote():
    response=requests.get("https://zenquotes.io/api/random")
    json_data=json.loads(response.text)
    print(json_data)
    quote=json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

@client.event
async def on_ready():
  print("You have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author==client.user:
    return
  else:
    if message.content.startswith("!hello"):
      await message.channel.send("Tsk! What a pain.")
      
    if message.content.startswith("!inspire"):
        quote1 = get_quote()
        await message.channel.send(quote1)

client.run(os.getenv("TOKEN"))
