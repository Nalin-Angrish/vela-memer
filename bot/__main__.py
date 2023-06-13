"""
Vela Memer - Python rewrite
"""
from sys import argv
import dotenv
import bot

dotenv.load_dotenv()

if "test" in argv:
    bot.run_tests()
if "run" in argv:
    bot.run_main()
