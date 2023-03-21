import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = ","6289175472:AAHvwwTpchbbHxYk10Q_zF-eCCtWqjKA0_U None)
    STRING_SESSION = 1BVtsOJQBu61mqs_3wKaA9tywoo3B88el3ytRiHk4BRlfAxyCdYAI8kZSkPxeFbBaFmmY4z3GOYEXyFLP-zWof_HLfKJC9v2t5daWNoNhpBtO6O_jAaSbfHyJj34xgFn0EZe3_q8_hag97qPVCsKxHqlLEG7EDjvCcoOyYWAqFgz9IkiJrXJrQSSNLyGk17ll76pTcF8iz9wPrTKHQlNVZQoBfGCZOyOYnozaqsfCdcT_LWgfpyD8BXa7IFf5uSnoceecOCvfhNRxpmXm8uCmI5XQKjcUxS2sJhKYkh7FIDijQ0yd4B9-ZN6KrUj0rd3s6nBOnIVl9Nl7BZXMBEFt7JjRPGtBizk= None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
