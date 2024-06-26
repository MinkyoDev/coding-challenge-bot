from pathlib import Path
import os, dotenv, datetime


env_path = Path('.') / '.env'
if env_path.exists():
    dotenv.load_dotenv(dotenv_path=env_path)

# main.py
BOT_TOKEN = os.getenv("BOT_TOKEN")

# git_API.py
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

# message_cog.py
CHANNEL_LIST = [1221059858111926352]

# user_channel.py
REGISTRATION_CHANNEL_ID = 1221104764012724344

# challenge_channel.py
CHALLENGE_CHANNEL_ID = 1223160187440074772

ADMIN_CHANNEL_ID = 1223614811280117820

# message_auto_delete.py
MAINTIME = 30

# commute_reminder.py
REMIND_CHANNEL_ID = 1230084679260966983

KST = datetime.timezone(datetime.timedelta(hours=9))
REMIND_TIME = datetime.time(hour=17, minute=58, tzinfo=KST)

CHECK_IN_TIMES = [
    datetime.time(hour=8, minute=50, tzinfo=KST),
    datetime.time(hour=9, minute=0, tzinfo=KST)
    ]

CHECK_OUT_TIMES = [
    datetime.time(hour=17, minute=50, tzinfo=KST),
    datetime.time(hour=18, minute=0, tzinfo=KST)
    ]