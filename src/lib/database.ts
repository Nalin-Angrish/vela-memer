import assert from 'assert';
import mongoose, { Mongoose } from 'mongoose';
import { DBGuild } from './types';

let database!:Mongoose;

const initDatabase = async () => {
  assert(process.env.MONGO_URI);
  database = await mongoose.connect(process.env.MONGO_URI);
};

const collection = () => database.connection.useDb('vela-memer').collection('guilds');

const addGuild = async (guildId:string, defaultChannelId?:string) => {
  const guildData:DBGuild = {
    guildId,
    interval: 60 * 30,
    memeCount: 5,
  };
  if (defaultChannelId !== undefined) guildData.memeChannelId = defaultChannelId;
  await collection().insertOne(guildData);
};

const deleteGuild = async (guildId:string) => {
  await collection().deleteOne({ guildId });
};

const updateGuild = async (guildId:string, data:DBGuild) => {
  const filteredData:DBGuild = {};
  if (data.memeChannelId) filteredData.memeChannelId = data.memeChannelId;
  if (data.interval) filteredData.interval = data.interval;
  if (data.memeCount) filteredData.memeCount = data.memeCount;
  await collection().updateOne({ guildId }, {
    $set: filteredData,
  });
};

const filterByInterval = (interval:number) => collection().find({ interval });

export {
  initDatabase,
  addGuild,
  deleteGuild,
  updateGuild,
  filterByInterval,
};
