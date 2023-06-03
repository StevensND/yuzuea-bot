# Yuzu Early Acess (Pineapple) Discord Bot
A Discord Bot that notifies the latest updates from [Yuzu EA (Pineapple)](https://github.com/pineappleEA/pineapple-src/releases). Developed in Python.

Invite me to your server by clicking [here](https://discord.com/api/oauth2/authorize?client_id=1114600548499476590&permissions=8&scope=bot).

## How to set up the bot on your Discord server

1. Invite the bot.
2. Once the bot is invited, make sure it has the necessary permissions to be able to publish in a channel (by default and to avoid annoyances, I have set the bot to have administrator permissions). This way it will be able to publish in the channel without problems.
3. Go to Discord Settings. Then go to Advanced and enable "Developer Mode" (Make sure the option is green) . This will allow us to get the channel ID, which we will use next.
4. Find the channel where you want the bot to publish the notifications, right click on it and then click on "Copy channel ID". This will give us the channel ID (example: 1113061947621986138).
5. In the channel type the following command: !setnotificationchannel + the ID of the channel you copied earlier (don't include the +). Example: !setnotificationchannel 1113061947621986138
6. Done. The bot will publish when an update is released.
