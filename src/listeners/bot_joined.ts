import {
  Client, Guild, GuildBasedChannel, MessageEmbed,
} from 'discord.js';
import { addGuild } from '../lib/database';

// TODO: Make this message meaningful
const message:MessageEmbed = new MessageEmbed({
  title: 'Hello World!',
  // eslint-disable-next-line no-multi-str
  description: 'Thanks for inviting me to this server.\n\
  To start getting memes from my awesome meme collection, you\'ll need to run some commands.\n\
  To know more about those commands and me, run `/help`',
});

const channelFilter = (guild:Guild) => {
  const channelFilterMain = (channel:GuildBasedChannel):boolean => {
    if (guild.me === null) return false;
    return channel.isText() && (channel.permissionsFor(guild.me).has('SEND_MESSAGES'));
  };
  return channelFilterMain;
};

export default (client:Client) : void => {
  /* eslint consistent-return: "off" */
  client.on('guildCreate', async (guild:Guild) => {
    const channel:GuildBasedChannel | undefined = guild.channels.cache.find(channelFilter(guild));
    if (channel === undefined) console.error('This server has no available text channel');
    if (channel !== undefined && channel.isText()) {
      // it always is a text channel, but the linter needs it so fine...
      await channel.send({ embeds: [message] });
    }
    addGuild(guild.id, channel?.id);
  });
};
