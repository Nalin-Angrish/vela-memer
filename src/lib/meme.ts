import axios, { AxiosResponse } from 'axios';
import { MessageEmbed, TextChannel } from 'discord.js';
import { MemeData, Meme as t_Meme } from './types';

export const getMemes = async (amount:number):Promise<MemeData> => {
  const res:AxiosResponse = await axios.get(`https://meme-api.com/gimme/${amount}`);
  if (res.statusText !== 'OK') return getMemes(amount);
  const data:MemeData = await res.data;
  return data;
};

export const sendMemes = async (memeData:MemeData, channel:TextChannel) => {
  const memeEmbeds:MessageEmbed[] = memeData.memes.map((meme:t_Meme):MessageEmbed => new MessageEmbed({
    title: meme.title,
    image: {
      url: meme.url
      // url: meme.preview[meme.preview.length - 1],
    },
  }));
  await channel.send({ embeds: memeEmbeds });
};
