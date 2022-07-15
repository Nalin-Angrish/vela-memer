import { Client, Guild } from 'discord.js';
import { deleteGuild } from '../lib/database';

export default (client:Client) : void => {
  client.on('guildDelete', async (guild:Guild) => {
    await deleteGuild(guild.id);
  });
};
