class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 9696783
    API_HASH = "3e74a9830493e9261410a947428dbb34"

    CASH_API_KEY = "8SOSKTRI0KPL"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://u6n1pffsk11ibd:p4149ea98c8b460704146ec5b87a689fd62b7bab3d06d1fa6f952f89eb84b7568@c1vo05l6n8k8mv.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d1bqch8k0bcb4r"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002404751523)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://ayanosuvii0925:subhichiku123@cluster0.uw8yxkl.mongodb.net/mydatabase"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://te.legra.ph/file/40eb1ed850cdea274693e.jpg"

    SUPPORT_CHAT = "DevilsHeavenMF"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "7924613089:AAH6R72kd02f-Sx91UscWNgraT7VHunBPTs"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "https://timezonedb.com/api"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 7225660023  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
