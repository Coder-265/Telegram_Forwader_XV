from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5185789068:AAGY9HRjzf6I0qVA1ax3r0l3r2P-at35D0w"  # Your bot API key
    OWNER_ID = 862271564  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    
    FROM_CHATS = [-1001521887631,-1001257120208]# List of chat id's to forward messages from.
    TO_CHATS = [-1001586301275]# List of chat id's to forward messages to.

    REMOVE_TAG = False
    WORKERS = 16
   
    
