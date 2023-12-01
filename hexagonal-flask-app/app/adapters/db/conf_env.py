import os

DB_USER_NAME = os.environ.get("DB_USER_NAME", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "example")
DB_HOST = os.environ.get("DB_HOST", "127.0.0.1")
DB_NAME = os.environ.get("DB_NAME", "phyact")
DB_STRING_CHECK = os.environ.get("DB_STRING_CHECK")

if not DB_STRING_CHECK:
    os.environ["DB_STRING"] = f"mysql+pymysql://{DB_USER_NAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    
DB_STRING = os.environ.get("DB_STRING")