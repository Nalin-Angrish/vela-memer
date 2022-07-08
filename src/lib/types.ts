import { RESTPostAPIApplicationCommandsJSONBody } from 'discord-api-types/v9';
import { BaseCommandInteraction, Client } from 'discord.js';

export interface Command {
  data: RESTPostAPIApplicationCommandsJSONBody
  run: (client: Client, interaction: BaseCommandInteraction) => void;
}

export interface Meme {
  postLint:string
  subreddit:string
  title:string
  url:string
  nsfw:boolean
  spoiler:boolean
  author:string
  ups:number
  preview:string[]
}

export interface MemeData {
  count:number
  memes:Meme[]
}

export interface DBGuild {
  id?:string
  memeChannelId?:string
  interval?:number
  memeCount?:number
}
