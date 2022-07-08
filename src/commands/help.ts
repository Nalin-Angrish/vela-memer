import { BaseCommandInteraction, Client, MessageEmbed } from 'discord.js';
import { SlashCommandBuilder } from '@discordjs/builders';
import { Command } from '../lib/types';

const Help: Command = {
  data: new SlashCommandBuilder()
    .setName('help')
    .setDescription('A help menu for you noobs.')
    .toJSON(),

  run: async (client: Client, interaction: BaseCommandInteraction) => {
    const content = new MessageEmbed({
      title: 'Vela Memer\'s help menu',
      description: 'The slash commands that can be used with this bot are described below:',
      fields: [
        {
          name: '`/help`',
          value: 'Shows this message.',
        },
        {
          name: '`/meme`',
          value: 'Sends you a meme.',
        },
        {
          name: '`/meme <n>`',
          value: 'Sends you `n` memes. `n` should be a number between 0 and 10.',
        },
        {
          name: '`/config <channel> <frequency> <num_memes>`',
          value: 'Helps you configure the options for this server. It\'s options are described in more detail below.',
        },
      ],
    });
    const configHelpEmbed = new MessageEmbed({
      fields: [
        {
          name: '`channel`',
          value: 'Sets the given channel as the meme dump.',
        },
        {
          name: '`frequency`',
          // eslint-disable-next-line no-multi-str
          value: 'Sets the frequency with which the bot sends the memes in the configured channel.\
          It should be a number between 1 and 10 (inclusive). The higher the frequency,\
          the faster the bot sends the memes. More details:\n\
          10: 1 min\n9: 5 min\n8: 10 min\n7: 30 min\n6: 1 hr\n5: 3 hrs\n4: 6 hrs\n3: 12 hrs\n2: 1 day\n1: 2days',
        },
        {
          name: '`num_memes`',
          // eslint-disable-next-line no-multi-str
          value: 'The number of memes you want the bot to send after every interval. \
          It should be a number between 1 and 10',
        },
      ],
    });

    await interaction.followUp({
      ephemeral: true,
      embeds: [content, configHelpEmbed],
    });
  },
};
export default Help;
