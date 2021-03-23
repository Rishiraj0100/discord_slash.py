import json
import random

from slashpy import Client, Command

with open("config.json", "r") as f:
    config = json.load(f)

bot = Client(
    config["token"], config["public_key"],
    config=config, port=config["port"]
)


class Test(Command):
    """ memes again """
    async def reply(self, ctx):
        return ctx.send(
            f"This is a test from 1-10: **{random.randint(1, 10)}**"
        )


bot.add_command(Test(bot))
bot.start()
