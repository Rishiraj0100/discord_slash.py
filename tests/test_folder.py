import json

from slashpy import Client

with open("config.json", "r") as f:
    config = json.load(f)

bot = Client(
    config["token"], config["public_key"],
    config=config, load_folder="testfolder", port=config["port"]
)

bot.start()
