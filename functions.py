import discord
import json


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


def generate_embed(title: str, desc: str, dic: dict, color: discord.Color = None, inline = True, tp: str = 'list') -> discord.Embed:
    """
    Essa função gera um EMBED do discord com base no dicionário passado

    Args:
        title (str): Título do EMBED
        desc (str): Descrição
        dic (dict): Dicionário de geração
        color (discord.Color, optional): Cor. Padrão é None.
        inline (bool, optional): Se as categorias serão na mesma linha. Padrão é True.

    Returns:
        discord.Embed: [description]
    """
    embed = discord.Embed(
        title=title,
        description=desc,
        color=color
    )
    if tp == 'list':
        for key in dic.keys():
            all_commands = ''
            for command in dic[key]:
                all_commands += f'{Text().code_block(command, "line")} '
            embed.add_field(name=key, value=all_commands, inline=inline)
    elif tp == 'dict':
        for key in dic.keys():
            all_commands = ''
            for command in dic[key]:
                all_commands += f'{Text().code_block(command, "line")} '
            embed.add_field(name=key, value=all_commands, inline=inline)
    
    return embed


def calcular_dado(valor: int, op: str) -> int:
    """
    Esta função pega dois valores, o valor e a string com uma operação, exemplo.
    calcular_dado(3, '*2') -> 6

    Args:
        valor ([int]): Valor que será executada a operação
        op ([str]): Operação que será executada
    """
    ldict = {}
    exec(f'soma_final = {valor}{op}', globals(), ldict)
    soma_final = ldict['soma_final']
    
    return soma_final
