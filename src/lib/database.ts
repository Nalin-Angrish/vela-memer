import { Client } from 'pg';
import { DBGuild } from './types';

const database:Client = new Client({ connectionString: process.env.PG_URI });

const initDatabase = async () => {
  await database.connect();
};

const addGuild = async (guildId:string, defaultChannelId?:string) => {
  const guildData:DBGuild = {
    guildId,
    interval: 60 * 30,
    memeCount: 5,
  };
  if (defaultChannelId !== undefined) guildData.memeChannelId = defaultChannelId;
  await database.query(
    'INSERT INTO Guilds(guildId, interval, memeCount, memeChannelId) VALUES ($1, $2, $3, $4)',
    [guildData.guildId, guildData.interval, guildData.memeCount, guildData.memeChannelId],
  );
};

const deleteGuild = async (guildId:string) => {
  await database.query('DELETE FROM Guilds WHERE guildId = $1', [guildId]);
};

const updateGuild = async (guildId:string, data:DBGuild) => {
  const rawData = await database.query('SELECT * FROM Guilds WHERE guildId = $1', [guildId]);
  const newData = data;
  if (!newData.memeChannelId) newData.memeChannelId = rawData.rows[0].memechannelid;
  if (!newData.interval) newData.interval = rawData.rows[0].interval;
  if (!newData.memeCount) newData.memeCount = rawData.rows[0].memecount;
  await database.query(
    'UPDATE Guilds SET interval = $2, memeCount = $3, memeChannelId = $4 WHERE guildId = $1',
    [guildId, newData.interval, newData.memeCount, newData.memeChannelId],
  );
};

const filterByInterval = async (interval:number) => {
  const data = await database.query('SELECT * FROM Guilds WHERE interval = $1', [interval]);
  return data.rows;
};

export {
  initDatabase,
  addGuild,
  deleteGuild,
  updateGuild,
  filterByInterval,
};
