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


def generate_embed(title: str, desc: str, dic: dict, color: discord.Color = None, inline = True) -> discord.Embed:
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
    embed = discord.Embed(  # Crio um EMBED
        title=title,  # Título do embed
        description=desc,  # Descrição do embed
        color=color  # Cor do embed
    )

    for key in dic.keys():  # Para cada chave na chave do dicionário
        all_commands = ''  # Crio uma string para adicionar meus comandos
        for command in dic[key]:  # Para cada comando no dicionário dos valores
            all_commands += f'{Text().code_block(command, "line")} '  # Concateno all_commands com bloco de código
        embed.add_field(name=key, value=all_commands, inline=inline)  # Adiciono um field
    
    return embed  # Retorno o Embed


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
