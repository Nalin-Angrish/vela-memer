import {
  BaseCommandInteraction, Client, TextChannel,
} from 'discord.js';
import { SlashCommandBuilder, SlashCommandNumberOption } from '@discordjs/builders';
import { getMemes, sendMemes } from '../lib/meme';
import { Command, MemeData } from '../lib/types';

const quantityOption = new SlashCommandNumberOption()
  .setName('quantity')
  .setDescription('How many memes do you want? (1 by default)');

const Meme: Command = {
  data: new SlashCommandBuilder()
    .setName('meme')
    .setDescription('An endless supply of memes.')
    .addNumberOption(quantityOption)
    .toJSON(),

  run: async (client: Client, interaction: BaseCommandInteraction) => {
    let amount:number = interaction.options.get('quantity')?.value as number || 1;
    let info:string = '';
    if (amount > 10) {
      info = `${amount} memes is just too much. `;
      amount = 10;
    }
    const content:string = `${info}Sending you your ${amount} memes in a few secs!`;
    await interaction.followUp({ content });

    const channel:TextChannel = client.channels.cache.get(interaction.channelId) as TextChannel;
    const memes:MemeData = await getMemes(amount);
    await sendMemes(memes, channel);
  },
};

export default Meme;
