HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    SESSION_STRING = environ[
        "SESSION_STRING"
    ]  # Check Readme for session
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    CHAT_ID = int(environ["CHAT_ID"])
    DEFAULT_SERVICE = environ.get("DEFAULT_SERVICE") or "youtube"
    BITRATE = int(environ["BITRATE"])

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 12797581
    API_HASH = "a28a82d59f72b92f38b8ea755a5ec8a3"
    ARQ_API_KEY = "Get this from @ARQRobot"
    CHAT_ID = -490902896
    DEFAULT_SERVICE = "saavn"  # Must be one of "youtube"/"saavn"
    BITRATE = 512 # Must be 512/320

# don't make changes below this line
ARQ_API = "https://thearq.tech"
