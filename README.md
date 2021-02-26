# Levi-Discord-Bot

A Discord Bot based on the 'Attack On Titan' anime character Levi.


## How to install:

Go to your terminal and switch to a desired directory. Then,
'''bash

	git clone https://github.com/hrithik20007/Levi-Discord-Bot.git
	python3 bot.py
'''
### Other Requirements:

* First go to- (https://discord.com/developers/applications/)
* Click on 'New Application'
* Give a desired name for your Levi bot.
* You will be redirected to the developers portal. Go to 'Bot' tab. 
* 'Add Bot'
* Enable Gateway Intents.
* Enable the necessary scopes and permissions in the 'OAuth2' tab.
* Copy the URL provided under the scopes.
* Open a new browser tab and paste the URL.
* Select the server you want to add the bot to and authorize.
* Copy the bot token for the next step. 
 
Make a .env file within the directory and define a 'TOKEN' environment variable by copying your bot token from - (https://discord.com/developers/applications/)
It will go something like this-
'''bash

	TOKEN="<bot token>"
'''
You may also directly just copy the token into the client.run() parameter as a string.

You have to redefine the ID variable in the program, to your server ID. To do that-
* Go to 'User Settings'.
* Go to 'Appearence' tab.
* Enable Developer Mode.
* Right click on the server name and you'll get an option to copy the server ID.

Install the necessary python packages or libraries with-
'''bash

	pip install <library name>
'''

## Commands available:

* !hello - It will display a hello message
* !rules - Displays all the rules of the server
* !rule<Number> - Displays that particular rule
* !play <URL of video> - Plays a particular Youtube video's audio
* !pause - Pause an audio
* !resume - Resumes audio
* !stop - Stops audio
* !leave - Bot leaves the voice channel
* !inspire - Will give you a random quote and it's author/speaker.


## Other Functionalities - 
1) Levi will recommend youtube videos to watch when you type a sad message.
2) Gives welcome messages to new members.
3) Bans members for use of profanity and gives them an embedded message.
