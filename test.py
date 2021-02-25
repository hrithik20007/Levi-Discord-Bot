import discord
import requests
import json
import random
#from discord.ext import commands
from better_profanity import profanity
from decouple import config
import os
import youtube_dl
import time

#try add this 
#intents=discord.Intents.all()
#if the above don't work, try with this
intents = discord.Intents.default()
intents.members=True

client=discord.Client(intents=intents)

ID=int(811629751361077301)

#To make the required strings, lists, dictionaries
string ="1) You are not special and you'll probably die without doing anything remarkable or significant. 2) You are alive, have a brain and two hands. Use them. 3) If you don't take a bath regularly, please be kind enough to not show your face here again. 4) You cannot take too long to decide on anything. 5) Don't get too cocky bitch. If you go haywire, I will personally put you down without hesitation. 6) Give up on your dreams and die. If you don't want to, then think. 7) If you dare think you are a better weeb than anyone else here, leave. 8) If you find the bastard Zeke, you are to bring him to me, alive. 9) No profanity! 10) From today, you are in the Survey Corps headed by the Commander. Welcome to AOT Discord Server!"
vids ={"Counter Attack Mankind":"https://www.youtube.com/watch?v=ikmBtnYCvaA","T-KT":"https://www.youtube.com/watch?v=0JWvS7w3-zY","EMA":"https://www.youtube.com/watch?v=J0RH_xdu8JM","Erwin's Charge Theme":"https://www.youtube.com/watch?v=Hs3AaiiCSJ0","Bodymotion":"https://www.youtube.com/watch?v=XqWknWbIWCE","Eren's Berserk Theme":"https://www.youtube.com/watch?v=LmPH8BTwPKU","My Theme":"https://www.youtube.com/watch?v=eFah8TCWOro","Sasegayo!":"https://www.youtube.com/watch?v=CID-sYQNCew","You See Big Girl":"https://www.youtube.com/watch?v=lO3jCpoTyIg","A JoJo reference":"https://www.youtube.com/watch?v=jXYN_M2RDLQ"}
words=["fail","failed","was eaten","simp","died","weak","sad","helpless","unhappy","miserable","depressed","angry","feel empty","hopeless","cry","crying","depression","alone","die","kill myself","shoot myself","hang myself","devastated","im so stupid","empty shell","feel right"]

#To make the rules list. Just honing some skills here :3. Ofc you can custom create your list.                                                                              
rules1= string.split("1) ",1)[1]
rules2=''.join(i for i in rules1 if not i.isdigit())
rules=rules2.split(") ",9)

#For Music Bot Settings later on
queue=[]
k=int(0)
j=int(0)

#For inspirational quotes API
def get_quote():
    response=requests.get("https://zenquotes.io/api/random")
    json_data=json.loads(response.text)
    print(json_data)
    quote=json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)

'''
#To wait till the song has stopped for the Music settings
def wait(somepredictate,timeout,period):
    mustend = int(time.time()) + int(timeout)
    global somepredicate
    while time.time()<mustend:
        if somepredicate.is_playing()==False:
            return True
        else:
            time.sleep(int(period))
            print("Audio is still playing")
'''

@client.event
async def on_ready():
     print("You have logged in as {0.user}".format(client)) #You can also do {0}.format(client.user)
     channel=client.get_channel(ID)
     await channel.send("Lance Corporal Levi is here!")

@client.event
async def on_member_join(member):
     print(f"{member.mention} has joined the server")
     channel=client.get_channel(ID)
     await member.send("So, another recruit huh? Take a look at the general group.")
     text = "Oi {0}, where's your manners? Say !hello.".format(member.mention)
     await channel.send(text)

@client.event
async def on_message(message):
    
  if message.author==client.user:
    return
#Banning member for use of profanity
  elif(profanity.contains_profanity(message.content)):
        if message.author.id!=684767817148530723:
            await message.delete()
            embed_mine=discord.Embed(title="YOU ARE BANNED!", color=15158332)
            embed_mine.add_field(name="Reason: ", value="You had been warned not to use profanity.", inline=True)
            embed_mine.add_field(name="\u200B", value="\u200B")        
            embed_mine.set_footer(text="Contact the Commander!")
            await message.author.send(embed=embed_mine)
            await message.channel.send(f"You should have read the rules {message.author.mention}")
            await message.guild.ban(message.author)
            
  else:
    msg=message.content.split()
    for i in range(len(msg)):
        msg[i]=msg[i].lower()
    
    if message.content.startswith("!hello"):
        await message.channel.send("Tsk! What a pain.")

#Send random inspiring quotes using the API
    if message.content.startswith("!inspire"):
        quote1 = get_quote()
        await message.channel.send(quote1)

#To suggest AOT videos based on random sad messages
    if any(word in msg for word in words):
        #key=random.choice(vids.keys())
        #value=vids.get(link)
        pair=a,b=random.choice(list(vids.items()))
        key= pair[0]
        value= pair[1] 
        await message.channel.send(f"We cannot afford to be weak {message.author.mention}. Here, listen to '{key}' to strengthen your mind."+ " "+ value) 

#To display rules
    if message.content == "!rules":
        for i in range(len(rules)):
            await message.channel.send(f"Rule{i+1} : {rules[i]}\n")

    if message.content[:5]=="!rule":
        id=int(message.content[5:])
        try:
            if id>0 and id<10:
                await message.channel.send(f"Rule{id}: {rules[id-1]}")
        except ValueError:
            pass

#To unban members as per their ID
    if message.content.startswith("!unban"):
        id=message.content[7:]
        user=await client.fetch_user(id)
        await message.guild.unban(user)
        await message.channel.send(f"Unbanned {user.mention}!")
        await user.send(f"Don't do that again.")

#--------------------------------------Bot Music Player Commands---------------------------------------
    
    if message.content.startswith("!play"):
        voice=discord.utils.get(message.guild.voice_channels, guild=message.guild)
        if message.author.voice == None:
            await message.channel.send("Join a voice first, baka!")
        else:
            global k
            if k==0:
                #Returns a boolean based on whether the provided path has a file at the end or not. The parameter is the provided path.
                song_there=os.path.isfile("song.mp3")
                try:
                    if song_there:
                            os.remove("song.mp3")
                except PermissionError:
                    await message.channel.send("Wait for the current playing music to end or use the '!stop' command")
                    return
                        
                #utils.get() returns the first element from the first iterable attribute, which satisfies the second attribute
                #voiceChannel=discord.utils.get(message.guild.voice_channels, name="General")
                voiceChannel=message.author.voice.channel
                #voice_clients gives a list of voice connections and is a VoiceClient instance
                voice=discord.utils.get(client.voice_clients, guild=message.guild)
                #voice=discord.VoiceClient.connect(self,timeout=60.0,reconnect=True)

                song=message.content[6:]
                queue.append(song)
                global ydl_opts1
                ydl_opts1={
                        'format':'bestaudio/best',
                        'postprocessors':[{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192'
                    }],
                }

                global j
                k=k+1
                j=k

                with youtube_dl.YoutubeDL(ydl_opts1) as ydl:
                    ydl.download([queue[0]])
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, "song.mp3")
                        voice.play(discord.FFmpegPCMAudio("song.mp3"))
            else:
                song=message.content[6:]
                queue.append(song)
                await message.channel.send("The song is queued!")
                for p in range(len(queue[j:])):            
                   # while not voice.is_playing():
                    mustend = int(time.time()) + int(10800)
                    while time.time()<mustend:
                        if voice.is_playing():
                            time.sleep(int(5))
                        else:
                            with youtube_dl.YoutubeDL(ydl_opts1) as ydl:
                                ydl.download([queue[p]])
                            for file in os.listdir("./"):
                                if file.endswith(".mp3"):
                                    os.rename(file, "song.mp3")
                                    voice.play(discord.FFmpegPCMAudio("song.mp3"))
                            break
                k=k+1
                j=k

    if message.content == "!queue":
        for i in range(len(queue)):
            await message.channel.send(f"Song {i+1}: {queue[i]}\n")

    if message.content == "!skip":
        voice=discord.utils.get(client.voice_clients, guild=message.guild)
        if voice.is_playing() and len(queue)<=j:
            ydl_opts1={
                        'format':'bestaudio/best',
                        'postprocessors':[{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192'
                 }],
               }
            with youtube_dl.YoutubeDL(ydl_opts1) as ydl:
                ydl.download([queue[j]])
            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    os.rename(file, "song.mp3")
                    voice.play(discord.FFmpegPCMAudio("song.mp3"))
        k=k+1
        j=k
        else:
           await message.channel.send("There is no music to skip to, baka.")
       
    if message.content == "!leave":
        voice=discord.utils.get(client.voice_clients, guild=message.guild)
        if voice.is_connected():
            await voice.disconnect()
        else:
            await message.channel.send("The bot is not connected to a voice channel, baka.")
    
    if message.content == "!pause":
        voice=discord.utils.get(client.voice_clients, guild=message.guild)
        if voice.is_playing():
            voice.pause()
        else:
            await message.channel.send("No audio playing currently, baka.")
    
    if message.content == "!resume":
        voice=discord.utils.get(client.voice_clients, guild=message.guild)
        if voice.is_paused():
            voice.resume()
        else:
            await message.channel.send("The audio is not paused, baka.")
    
    if message.content == "!stop":
        voice=discord.utils.get(client.voice_clients, guild=message.guild)
        if voice.is_playing():
            voice.stop()
        else:
            await message.channel.send("There's no audio playing, baka.")
    

client.run(config("TOKEN"))


'''        
<---------------- ALONG LINE 117 ------------------> (Before Music Bot Settings)    
        user= message.guild.bans()
        for i in user:
            print(i+ "\n")
            member_name, member_discriminator=i.member, i.discriminator
            if(member_discriminator is discriminator and member_name is name):
                await ctx.guild.unban(member)
                await ctx.channel.send(f"Unbanned {member.mention}!")
'''
'''
    await bot.process_commands(message)
#Making a Bot object(more functionality than Client object) for commands specific purpose only. In message_only, it is not really used for making commands, but to respond to a message event.
bot=commands.Bot(command_prefix="!")

@bot.command()
async def brofist(ctx):
    await ctx.channel.send(f"Yo! {ctx.message.author.mention}")

#Command to unban a member
@bot.command()
async def unban(ctx, *, member):
    banned_users=ctx.guild.bans()
    member_name, member_discriminator=member.split("#",1)
    if(member_discriminator is i.discriminator for i in banned_users):
        await ctx.guild.unban(member)
        await ctx.channel.send(f"Unbanned {member.mention}!")
'''
'''
We may also do- (ignoring the if block and using these instead. To put the member name to use as well)

    for i in banned_users:
        user=banned_users[i]
        if (user.name,user.discriminator)==(member.name,member.discriminator):
            await ctx.guild.unban(user)
''' 
'''
-----OR-----
@bot.command()
@guild_only #Might not need
async def unban(ctx,id:int):
    user=await bot.fetch_user(id)
    await ctx.guild.unban(user)
'''           






'''    
    if message.content.startswith("!play"):
        
        #Returns a boolean based on whether the provided path has a file at the end or not. The parameter is the provided path.
        song_there=os.path.isfile("song.mp3")
        try:
            if song_there:
                    os.remove("song.mp3")
        except PermissionError:
            await message.channel.send("Wait for the current playing music to end or use the '!stop' command")
            return
                
        #utils.get() returns the first element from the first iterable attribute, which satisfies the second attribute
        voiceChannel=discord.utils.get(message.guild.voice_channels, name="General")
        await voiceChannel.connect()
        #voice_clients gives a list of voice connections and is a VoiceClient instance
        voice=discord.utils.get(client.voice_clients, guild=message.guild)
        #voice=discord.VoiceClient(client.voice_clients, guild=message.guild)
        
        ydl_opts={
                'format':'bestaudio/best',
                'postprocessors':[{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }],
        }
        
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([message.content[6:]])
        for file in os.listdir("./"):
            if file.endswith(".mp3"):
                os.rename(file, "song.mp3")
        voice.play(discord.FFmpegPCMAudio("song.mp3"))
'''








'''
    if message.content.startswith("!queue"):
            voice=discord.utils.get(client.voice_clients, guild=message.guild)
           # if not voice.is_playing():
                #await message.channel.send("No audio is playing. Just use !play, baka.")
            #else:
            song=message.content[7:]
            queue.append(song)
            k=k+1
    if not discord.utils.get(client.voice_clients, guild=message.guild).is_playing():
        p=0
        ydl_opts1={
            'format':'bestaudio/best',
            'postprocessors':[{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192'
     }],
 }
        for p in range(len(queue())):
            with youtube_dl.YoutubeDL(ydl_opts1) as ydl:
                ydl.download([queue[p]])
            while not voice.is_playing():
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, "song.mp3")
                        voice.play(discord.FFmpegPCMAudio("song.mp3"))
'''      
