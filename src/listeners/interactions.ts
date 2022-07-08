import { BaseCommandInteraction, Client, Interaction } from 'discord.js';
import { Command } from '../lib/types';
import Commands from '../Commands';

const handleSlashCommand = async (
  client: Client,
  interaction: BaseCommandInteraction,
): Promise<void> => {
  const command:Command | undefined = Commands.find((cmd:Command) => cmd.data.name === interaction.commandName);

  if (!command) {
    interaction.followUp({
      content: 'An error occurred. This command does not exist.',
    });
    return;
  }

  await interaction.deferReply();
  command.run(client, interaction);
};

export default (client: Client): void => {
  client.on('interactionCreate', async (interaction: Interaction) => {
    if (interaction.isCommand() || interaction.isContextMenu()) {
      await handleSlashCommand(client, interaction);
    }
  });
};
