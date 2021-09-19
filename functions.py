import discord


class Text:
    def __init__(self):
        pass

    @staticmethod
    def bold(text):
        return f'**{text}**'

    @staticmethod
    def italic(text):
        return f'*{text}*'

    @staticmethod
    def striketrough(text):
        return f'~~{text}~~'

    @staticmethod
    def underline(text):
        return f'__{text}__'

    @staticmethod
    def code_block(text, tp):
        if tp == 'line':
            return f'`{text}`'
        elif tp == 'multiple':
            return f'```{text}```'

    @staticmethod
    def block_quote(text):
        return f'> {text}'


def generate_embed(dic: dict) -> discord.Embed:
    ...
