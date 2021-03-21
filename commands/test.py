import random

from slashpy import Command


class TestAgain(Command):
    """ memes again """
    async def reply(self, ctx):
        return ctx.send(
            f"This is a test from 1-10: **{random.randint(1, 10)}**"
        )


def setup(bot):
    bot.add_command(TestAgain(bot))
