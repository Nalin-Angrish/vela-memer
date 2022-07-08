import assert from 'assert';
import { REST } from '@discordjs/rest';
import { Routes } from 'discord-api-types/v9';
import { config } from 'dotenv';
import { Command } from './lib/types';
import Commands from './Commands';

// setup environment variables for development.
// on production, the variables are provided by
// the kubernetes configuration.
config();

const commands = Commands.map((cmd:Command) => (cmd.data));

assert(process.env.BOT_TOKEN);
assert(process.env.CLIENTID);

const rest = new REST({ version: '9' }).setToken(process.env.BOT_TOKEN);

rest.put(Routes.applicationCommands(process.env.CLIENTID), { body: commands })
  .then(() => console.log('Successfully registered application commands.'))
  .catch(console.error);
