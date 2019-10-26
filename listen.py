import json
import sys
import bot_library
import bot_commands
from argparse import ArgumentParser

def listen(bot_api_token):
    last_update_id=None
    updates = bot_library.getUpdates(bot_api_token,last_update_id)
    last_update_id=bot_library.get_last_update_id(updates)
    while True:
        updates = bot_library.getUpdates(bot_api_token,last_update_id)
        if len(updates["result"]) > 0:
            (text, chat_id) = bot_library.get_last_chat_id_and_text(updates)
            bot_commands.ask_bot(text,bot_api_token,chat_id)
            last_update_id=bot_library.get_last_update_id(updates)+1

# read command line arguments
parser = ArgumentParser()
parser.add_argument("-c", "--config", action="store")

args = parser.parse_args()
# read config file
with open(args.config) as json_config_file:
    config_data = json.load(json_config_file)
bot_api_token = config_data["bot_api_token"]
# call main
listen(bot_api_token)

