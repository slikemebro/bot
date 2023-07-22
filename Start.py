import subprocess
import logging
from AcceptApplications.config import *
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage

subprocess.Popen('python AcceptApplications/bot.py')

logging.basicConfig(level=logging.INFO)