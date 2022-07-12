import { Client, DiscordAPIError, TextChannel } from 'discord.js';
import { filterByInterval } from './lib/database';
import { getMemes, sendMemes } from './lib/meme';
import { MemeData } from './lib/types';

export const intervalInfo:number[] = [
  60,
  60 * 5,
  60 * 10,
  60 * 30,
  60 * 60,
  60 * 60 * 3,
  60 * 60 * 6,
  60 * 60 * 12,
  60 * 60 * 24,
  60 * 60 * 24 * 2,
];

const initInterval = (client:Client, interval:number) => {
  setInterval(async () => {
    const memes:MemeData = await getMemes(10);
    filterByInterval(interval).forEach((_guild) => {
      if (!_guild.memeChannelId) return;
      const channel:TextChannel = client.channels.cache.get(_guild.memeChannelId) as TextChannel;
      const memesForThisGuild:MemeData = {
        count: _guild.memeCount || 10,
        memes: memes.memes.slice(0, _guild.memeCount || 10),
      };
      sendMemes(memesForThisGuild, channel).catch((e:DiscordAPIError) => { console.error(e); });
    });
  }, interval * 1000);
};

const initAutoMemeSender = (client:Client) => {
  intervalInfo.forEach((interval:number) => initInterval(client, interval));
};

export default initAutoMemeSender;
