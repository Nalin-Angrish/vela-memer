# Vela Memer
Need memes? Just add me in your server. I'm free and have an unlimited meme supply!

## Invite
To invite the bot to your server, click [here](https://discord.com/api/oauth2/authorize?client_id=994950920163049502&permissions=18432&scope=applications.commands%20bot). The bot does not have any official server, but you can join [this](https://dsc.gg/summersun) server or chat me personally if you have any queries. 

## Setting up
To get the code running, follow the given steps:
1. Install Python (https://python.org).
2. Clone the repo and open a terminal in the cloned directory. 
  `git clone https://github.com/Nalin-Angrish/vela-memer.git`
3. Install project dependencies.
  `pip install -r requirements.txt`
4. Setup environment variables using a `.env` file. The file should contain the following variables:
  - BOT_TOKEN: The token used by the discord bot (can be obtained from the discord developer dashboard).
  - CLIENTID: The client id (can be obtained from the discord developer dashboard).
  - DB_URI: The URI to connect to your sql database instance. The database must be supported by SQLAlchemy.
5. Run `python -m bot run` to register all bot commands and start the bot.