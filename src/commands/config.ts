import { BaseCommandInteraction, Client } from 'discord.js';
import { SlashCommandBuilder, SlashCommandChannelOption, SlashCommandNumberOption } from '@discordjs/builders';
import { ChannelType } from 'discord-api-types/v9';
import { updateGuild } from '../lib/database';
import { Command } from '../lib/types';
import { intervalInfo } from '../AutoMemeSender';

const Config: Command = {
  data: new SlashCommandBuilder()
    .setName('config')
    .setDescription('Configure Vela Memer')
    .addChannelOption(
      new SlashCommandChannelOption()
        .setName('channel')
        .setDescription('The Channel to send memes into')
        .addChannelTypes(ChannelType.GuildText),
    )
    .addNumberOption(
      new SlashCommandNumberOption()
        .setName('frequency')
        .setDescription('How often to send the memes in the configured channel. (1-10)'),
    )
    .addNumberOption(
      new SlashCommandNumberOption()
        .setName('num_memes')
        .setDescription('Number of memes to send every time. (1-10)'),
    )
    .toJSON(),

  run: async (client: Client, interaction: BaseCommandInteraction) => {
    if (!interaction.guildId) return;

    // Check if the user has the permissions
    if (!(
      interaction.memberPermissions?.any('ADMINISTRATOR')
      || interaction.memberPermissions?.any('MANAGE_GUILD')
    )) {
      await interaction.followUp('c\'mon bruh how could you even think you were allowed to do this?');
      return;
    }

    let interval;
    if (interaction.options.get('frequency')?.value) {
      interval = intervalInfo[intervalInfo.length - (interaction.options.get('frequency')?.value as number)];
      console.log(intervalInfo.length - (interaction.options.get('frequency')?.value as number), interval);
    } else {
      interval = undefined;
    }

    await updateGuild(interaction.guildId, {
      memeChannelId: interaction.options.get('channel')?.value as string,
      interval: interval as number,
      memeCount: interaction.options.get('num_memes')?.value as number,
    });
    await interaction.followUp('The settings have been updated!');
  },
};
export default Config;
