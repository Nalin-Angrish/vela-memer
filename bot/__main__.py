"""
Vela Memer - Python rewrite
"""
from sys import argv
import asyncio
import dotenv
import bot

dotenv.load_dotenv()

if "test" in argv:
    print("Disabled for now...")
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # asyncio.run(bot.run_tests())
    # loop.close()
if "run" in argv:
    bot.run_main()
