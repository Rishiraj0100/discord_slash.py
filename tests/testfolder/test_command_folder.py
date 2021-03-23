from slashpy import Command


class FolderTest(Command):
    """ folder test """
    async def reply(self, ctx):
        return ctx.send("folder test")


def setup(bot):
    bot.add_command(FolderTest(bot))
