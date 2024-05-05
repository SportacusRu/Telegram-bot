from decouple import config


TOKEN = config("TOKEN")
BASE_URL = config("BASE_URL")
FRONTEND_URL = config("FRONTEND_URL")
MODERATOR_ID = int(config("MODERATOR_ID"))
MODERATOR_KEY = config("MODERATOR_KEY")