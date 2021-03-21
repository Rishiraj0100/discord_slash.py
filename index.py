import json

from slashpy import Client
from quart import Quart, request, abort

app = Quart(__name__)


with open("config.json", "r") as f:
    config = json.load(f)

bot = Client(config)
bot.start(config["token"], config["public_key"])


# This is where the magic happens
@app.route("/", methods=["POST"])
async def interactions():
    data = await request.json
    await bot.verify(request)

    if data["type"] == 1:
        return {"type": 1}

    command = bot.get_command(data["data"]["name"])
    if command:
        return await command.reply(bot)
    else:
        return abort(400)

app.run(port=config["port"])
