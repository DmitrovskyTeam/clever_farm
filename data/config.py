from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
DATABASE_PATH = env.str("DATABASE_PATH")
SENSORS_TIMEOUT_REQUEST = env.int("SENSORS_TIMEOUT_REQUEST")
