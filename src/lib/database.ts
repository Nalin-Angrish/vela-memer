import assert from 'assert';
import mongoose, { Mongoose } from 'mongoose';
import { DBGuild } from './types';

let database!:Mongoose;

const initDatabase = async () => {
  assert(process.env.MONGO_URI);
  database = await mongoose.connect(process.env.MONGO_URI);
  console.log(database.connection.readyState);
  // database.connection.useDb('vela-memer');
};

const collection = () => database.connection.useDb('vela-memer').collection('guilds');

const addGuild = async (guildId:string, defaultChannelId:string) => {
  await collection().insertOne({
    guildId,
    // these are default options, and can be updated by the admin(s) of the guilds
    memeChannelId: defaultChannelId,
    interval: 60 * 30,
    memeCount: 5,
  });
};

const deleteGuild = async (guildId:string) => {
  await collection().deleteOne({ guildId });
};

const updateGuild = async (guildId:string, data:DBGuild) => {
  const filteredData:DBGuild = {};
  if (data.memeChannelId) filteredData.memeChannelId = data.memeChannelId;
  if (data.interval) filteredData.interval = data.interval;
  if (data.memeCount) filteredData.memeCount = data.memeCount;
  console.log('Updated data in guild:', guildId, 'new content:', filteredData);
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
