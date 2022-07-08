import { Client, Guild } from 'discord.js';
import { deleteGuild } from '../lib/database';

export default (client:Client) : void => {
  client.on('guildDelete', async (guild:Guild) => {
    deleteGuild(guild.id);
  });
};
