import os


class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

    APP_ID = int(os.environ.get("APP_ID", 1234))

    API_HASH = os.environ.get("API_HASH", "")
