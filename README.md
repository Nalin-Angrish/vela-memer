# Vela Memer
Need memes? Just add me in your server. I'm free and have an unlimited meme supply!

## Invite
To invite the bot to your server, click [here](https://discord.com/api/oauth2/authorize?client_id=994950920163049502&permissions=0&scope=applications.commands%20bot). The bot does not have any official server, but you can join [this](https://dsc.gg/summersun) server or chat me personally if you have any queries. 

## Setting up
To get the code running, follow the given steps:
1. Install Node.js (https://nodejs.org) and optionally yarn (https://yarnpkg.com).
2. Clone the repo and open a terminal in the cloned directory. 
  `git clone https://github.com/Nalin-Angrish/vela-memer.git`
3. Install project dependencies.
  `npm install` 
  OR 
  `yarn`
4. Setup environment variables using a `.env` file. The file should contain the following variables:
  - BOT_TOKEN: The token used by the discord bot (can be obtained from the discord developer dashboard).
  - CLIENTID: The client id (can be obtained from the discord developer dashboard).
  - MONGO_URI: The URI to connect to your mongodb instance.
5. Run `npm run dev-cmd` / `yarn dev-cmd` to register application commands. Run `npm run dev` / `yarn dev` to run the bot in development mode.
6. Run `npm run build` / `yarn build` to compile all typescript code into js, and run `npm run start` / `yarn start` to register all new commands and start the bot.