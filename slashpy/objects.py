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



class User:
    def __init__(self, data):
        self.name = data["username"]
        self.id = int(data["id"])
        self.discriminator = data["discriminator"]
        self.avatar = data["avatar"]

    def __str__(self):
        """ Builds full username to Discord user """
        return f"{self.name}#{self.discriminator}"

    def is_avatar_animated(self):
        """ Returns True/False depending if avatar is animated """
        return bool(self.avatar and self.avatar.startswith("a_"))

    @property
    def mention(self):
        """ Returns a Discord ping to targeted user """
        return f"<@{self.id}>"

    def avatar_url(self, img_format: str = "webp", size: int = None):
        """ Builds the AvatarURL for a Discord user """
        if self.avatar:
            if self.is_avatar_animated():
                img_format = "gif"

            if size:
                valid_size = [1024, 512, 256, 128, 64, 32]
                if size not in valid_size:
                    raise ValueError(f"Size can only be the following: {valid_size}")
                size_str = f"?size={size}"
            else:
                size_str = ""
            return f"https://cdn.discordapp.com/avatars/{self.id}/{self.avatar}.{img_format}{size_str}"
        return f"https://cdn.discordapp.com/embed/avatars/{int(self.discriminator) % 5}.png"
