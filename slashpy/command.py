"""
MIT License

Copyright (c) 2021 AlexFlipnote

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


import inspect


class Command:
    """ No description available """
    def __init__(self, bot):
        self.bot = bot
        doc_desc = type(self).__doc__
        self.name = type(self).__name__.lower()
        self.description = inspect.cleandoc(doc_desc) if doc_desc else ""
        self.options = []
        self.command = {}
        self.id = None

        if not isinstance(self.name, str):
            raise TypeError("Command name must be a string")

    def prepare(self, bot):
        pass

    async def reply(self, bot):
        pass

    @property
    def raw(self):
        """ Display raw JSON """
        return self.command

    def build(self):
        """ Build the JSON command """
        self.prepare(self.bot)
        self.command["name"] = self.name
        self.command["description"] = self.description or "No description available"
        self.command["options"] = self.options
        return self.command


class Option:
    def __init__(self):
        self.options = []

    def build(self):
        return self.options

    def add_values(self, name: str, description: str, values: tuple, required: bool = True):
        choices = [
            {"name": name, "value": value}
            for name, value in values
        ]

        make_option = {
            "name": name, "description": description,
            "type": 3, "required": required, "choices": choices
        }

        self.options.append(make_option)
        return make_option
