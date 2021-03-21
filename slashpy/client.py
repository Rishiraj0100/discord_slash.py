import os
import sys
import importlib

from slashpy import Endpoints
from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
from quart import abort


class Client:
    def __init__(self, config=None, commands_folder: str = "commands"):
        self.endpoints = None
        self.config = config
        self.online_commands = []
        self.commands_folder = commands_folder
        self.commands = []

    async def verify(self, request):
        pub_key = self.endpoints.public_key
        verify_key = VerifyKey(bytes.fromhex(pub_key))
        signature = request.headers["X-Signature-Ed25519"]
        timestamp = request.headers["X-Signature-Timestamp"]
        body = await request.data

        try:
            verify_key.verify(f'{timestamp}{body.decode()}'.encode(), bytes.fromhex(signature))
        except BadSignatureError:
            abort(401, 'Invalid request signature')

    def get_command(self, command_name: str):
        command = next((g for g in self.commands if g.name == command_name), None)
        return command

    def add_command(self, command, guild_id: int = None):
        if self.get_command(command.name):
            raise ValueError(f"Command {command.name} already exists")

        online = next((g for g in self.online_commands if g["name"] == command.name), None)
        if online:
            self.endpoints.edit_command(online["id"], command.build, self.config["guild_id"])
        else:
            self.endpoints.create_command(command.build, self.config["guild_id"])

        self.commands.append(command)

    def delete_removed_commands(self):
        local_commands = [g.name for g in self.commands]
        for command in self.online_commands:
            if command["name"] not in local_commands:
                self.endpoints.delete_command(command["id"], self.config["guild_id"])

    def load_command(self, name):
        if self.get_command(name):
            raise Exception("This command already exists")

        spec = importlib.util.find_spec(f"{self.commands_folder}.{name}")

        if not spec:
            raise Exception("File not found")

        lib = importlib.util.module_from_spec(spec)
        sys.modules[name] = lib

        try:
            spec.loader.exec_module(lib)
            setup = getattr(lib, "setup")
            setup(self)
        except Exception as e:
            del sys.modules[name]
            raise Exception(e)

    def fetch_commands(self):
        for file in os.listdir(self.commands_folder):
            if file.endswith(".py"):
                name = file[:-3]
                self.load_command(name)

    def send(self, content: str, embeds: tuple = None, tts: bool = False):
        if embeds:
            if len(embeds) == 1:
                embeds = [embeds]

        return {
            "type": 4,
            "data": {
                "tts": tts,
                "content": content,
                "embeds": embeds if embeds else [],
                "allowed_mentions": {"parse": []}
            }
        }

    def start(self, token: str, public_key: str):
        self.endpoints = Endpoints(token, public_key)
        self.online_commands = self.endpoints.get_commands(self.config["guild_id"])
        self.fetch_commands()
        self.delete_removed_commands()