from pathlib import Path
import os, dotenv

env_path = Path('.') / '.env'
if env_path.exists():
    dotenv.load_dotenv(dotenv_path=env_path)

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DATABASE = os.getenv('DATABASE')

DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DATABASE}?charset=utf8'
