import sys
from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient
from pyrogram import Client

import config
from ..logging import LOGGER


temp_client = Client(
        "Stranger",
        bot_token=config.BOT_TOKEN,
        api_id=config.API_ID,
        api_hash=config.API_HASH,
    )
temp_client.start()
info = temp_client.get_me()
username = info.username
database="Stranger__" + username
temp_client.stop()

if config.MONGO_DB_URI is None:
    LOGGER(__name__).warning(
        "No MONGO DB URL found.. Exiting....."
    )
    sys.exit()
else:
    _mongo_async_ = _mongo_client_(config.MONGO_DB_URI)
    _mongo_sync_ = MongoClient(config.MONGO_DB_URI)
    database_names = _mongo_sync_.list_database_names()
    if config.MONGO_DB_NAME :
        mongodb = _mongo_async_[config.MONGO_DB_NAME]
        pymongodb = _mongo_sync_[config.MONGO_DB_NAME]
    else:
        mongodb = _mongo_async_[database]
        pymongodb = _mongo_sync_[database]
