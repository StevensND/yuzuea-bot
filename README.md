# Yuzu Early Acess (Pineapple) Discord Bot
A Discord Bot that notifies the latest updates from [Yuzu EA (Pineapple)](https://github.com/pineappleEA/pineapple-src/releases). Developed in Python by me (Stevens#5210).

Invite me to your server by clicking [here](https://discord.com/api/oauth2/authorize?client_id=1114600548499476590&permissions=8&scope=bot). Do you want to support me?. Here is my [Ko-fi](https://ko-fi.com/stevenss)

If you also want a changelog channel, join the [Yuzu Discord Server](https://discord.gg/yuzu-emu), go to the yuzu-updates section and click Follow. Then select the channel where you want the changelogs to be published and you're done.

## How to set up the bot on your Discord server

1. Invite the bot.
2. Once the bot is invited, make sure it has the necessary permissions to be able to publish in a channel (by default and to avoid annoyances, I have set the bot to have administrator permissions). This way it will be able to publish in the channel without problems.
3. Go to Discord Settings. Then go to Advanced and enable "Developer Mode" (Make sure the option is green) . This will allow us to get the channel ID, which we will use next.
4. Find the channel where you want the bot to publish the notifications, right click on it and then click on "Copy channel ID". This will give us the channel ID (example: 1113061947621986138).
5. In the channel type the following command: !setnotificationchannel + the ID of the channel you copied earlier (don't include the +). Example: !setnotificationchannel 1113061947621986138
6. Done. The bot will publish when an update is released.

## How to set up your bot in the cloud

Would you like to have your bot hosted by yourself in the cloud and not depend on my host?. If you are interested, read on. To do so, we will need a host that allows us to host our bot in the cloud. In my case I will use [Discloud](https://discloudbot.com/).

1. Download the zip file from [releases](https://github.com/StevensND/yuzuea-bot/releases) and register in Discloud. Once registered and on the dashboard, click on +Add App. From here, we will drag the .zip file that you can download in the Releases section, but WARNING: For make it work properly, you will have to make some changes.

2. Extract the .zip file. Edit the "github.py" file with Notepad or Notepad++. From here, you will edit the TOKEN = field and enter your personal TOKEN. To get one, we will access the [Discord developer portal](https://discord.com/developers/applications).

3. We will create a new application. Enter the name, accept the terms and then click Create. Go to the Bot section and click on Reset Token. The token that you need will appear. Copy and paste it into the field mentioned previously.

4. Then you will go to OAuth2, General. In the Default Authorization Link, Authorization Method section click and select In-app Authorization. In scopes select: bot. Add the permissions that you want and save the changes. Then go to URL Generator, in scopes choose bot and in permissions the same as you chose before. Now you will get a URL, copy it and save it. This URL will be the one you will need to invite the bot to your server.

5. Check again the "github.py" file, check that you have placed the TOKEN and you are done. Also, you will need to edit the "discloud.config" file. Here you will only have to add a name to the bot for Discloud to identify it.

You can also edit the frequency at which the bot checks for new updates (right now it is set to every 10 minutes) on the "github.py" file.

Once these steps are done, make a .zip file and make sure that the zip has all the necessary files. Then go back to Discloud and drag the .zip file. Discloud will do the rest for you. If you have done everything correctly, you will see a green light in Discloud indicating that the bot is working. Check it also in Discord.

## Bot commands

Here are the commands available in the bot along with their functions:

1. `!eastatus`: Displays a message indicating that the bot is running and operational.

2. `!ealatest`: Checks the latest version available from the repository on GitHub and displays the version number.

3. `!eareleases`: Displays a message with a link to all the versions available in the GitHub repository.

4. `!setnotificationchannel <Channel_ID>`: Sets the notification channel where new version notifications will be sent. You must provide the channel ID as an argument.

In addition to these commands, the bot has the following functions:

- Periodically checks for new versions of the repository on GitHub every 10 minutes.
- Detects if an Internet connection is available before checking.
- Sends a message to the notification channel if a new version is found available.
- Print messages to the console when the bot connects or disconnects from Discord.

Remember that the bot needs the authentication token to function properly.

You can edit them by just changing the command name on the "github.py" file. Ex: for ealatest, search @client.command() async def ealatest(ctx): line and change ealatest to whatever you want.

## How to run the bot on local (your PC)

Download the .zip file from the releases section. Extract the files and place them inside a new folder (we do this for more organization and ease of work). Click on the path bar where you have the folder, delete the path and type cmd. 

This will open cmd directly with the path already set up.  Then type yuzuea-env\Scripts\activate.bat 

Once typed, press Enter. The .bat will then be activated. To get the bot working, type python github.py and press Enter again. That's it, now your bot will run locally on your PC.

If you have any questions or problems, please contact me ;).
