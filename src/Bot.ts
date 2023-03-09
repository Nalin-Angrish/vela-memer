import { config } from 'dotenv';

import { Client, Intents } from 'discord.js';

import bot_joined from './listeners/bot_joined';
import bot_leave from './listeners/bot_leave';
import interactions from './listeners/interactions';
import ready from './listeners/ready';

import initAutoMemeSender from './AutoMemeSender';
import { initDatabase } from './lib/database';
// setup environment variables for development.
// on production, the variables are provided by
// the kubernetes configuration.
config();

const client = new Client({
  intents: [Intents.FLAGS.GUILDS],
});

// set up listeners
bot_joined(client);
bot_leave(client);
interactions(client);
ready(client);

initDatabase().then(() => {
  client.login(process.env.BOT_TOKEN);
  initAutoMemeSender(client);
});
