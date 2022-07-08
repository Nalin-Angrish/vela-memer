import { Command } from './lib/types';

import Help from './commands/help';
import Meme from './commands/meme';
import Config from './commands/config';

const Commands:Command[] = [Help, Meme, Config];
export default Commands;
