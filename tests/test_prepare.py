import json

from slashpy import Client, Command, Option

with open("config.json", "r") as f:
    config = json.load(f)

bot = Client(
    config["token"], config["public_key"],
    config=config, port=config["port"], debug=True
)


class TestOption(Command):
    """ memes again """
    def prepare(self, ctx):
        values = (
            ["First", "value1"],
            ["Second", "value2"]
        )

        option = Option()
        option.add_values(
            "Test values", "This is to simply test the values",
            values
        )

        """
        TODO:
        <Response [400]>
        b'{"code": 50035, "errors": {"options": {"0": {"name": {"_errors": [{"code": "STRING_TYPE_REGEX",
        "message": "String value did not match validation regex."}]}}}}, "message": "Invalid Form Body"}'
        """
        self.options = option.build()

    async def reply(self, ctx):
        return ctx.send("Well, it worked I guess?")


bot.add_command(TestOption(bot))
bot.start()
