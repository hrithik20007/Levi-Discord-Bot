import discord
import os

client=discord.Client()

@client.event
async def on_ready():
  print("You have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author==client.user:
    return
  else:
    if(message.content.startswith("!hello"):
      await message.channel.send("Tsk! What a pain.")

client.run(os.getenv("TOKEN"))
