import discord
from discord.ext import commands
import os
import json
from dotenv import load_dotenv
from random import randint
from functions import *

# Variáveis do JSON
with open('options.json', 'r') as file:
    options = json.load(file)

# Variáveis
load_dotenv()
client = discord.Client()
bot = commands.Bot(command_prefix=options['prefix'], help_command=None)
default_commands = {
    'RPG:': [
        'iniciar',
        'login',
        'ver'
    ],
    'GERAL': [
        'rolar'
    ],
    'CONFIGS': [
        'configs',
        'creditos'
    ]
}
configurations = {}


@bot.event
async def on_ready():
    print("Logged successfully!")


# Comando de ajuda
@bot.command(name='help')
async def ajuda(ctx, *args):
    embed = discord.Embed(
        title='AJUDA',
        description='Eu sou Pedro, o Mamaco Programador, e esta mensagem serve para dar uma ajudinha sobre os comandos que posso interpretar, o corno'
                    'do João Pedro tá terminando de fazer o resto dos comandos, inclusive os do RPG, então é só ter um pouquinho de paciência :)',
        color=discord.Color.blue()
    )

    for key in default_commands.keys():
        all_commands = ''
        for command in default_commands[key]:
            print(command)
            all_commands += f'{Text().code_block(command, "line")} '
        embed.add_field(name=key, value=all_commands, inline=False)

    await ctx.send(embed=embed)


# ===================
# COMANDOS DO RPG
# ===================

# Iniciar o personagem
@bot.command(name='iniciar')
async def init(ctx, *args):
    await ctx.send('COMANDO DE INICIAR PERSONAGEM')


# Criar um personagem que já está feito
@bot.command(name='login')
async def login(ctx, *args):
    await ctx.send('COMANDO DE LOGAR O PERSONAGEM')


# Comando para ver o personagem
@bot.command(name='ver')
async def see(ctx, *args):
    await ctx.send('COMANDO DE VER O PERSONAGEM')


# ===================
# COMANDOS GERAIS
# ===================

# Comando de rolar um dado
@bot.command(name='rolar')
async def roll(ctx, *args):
    """
    Rola um dado de acordo com os parâmetros passados
    :param ctx: Mensagem
    :param args: Argumentos
    """
    
    if len(args) == 0:
        await ctx.send("Por favor, passe os parâmetros corretos!")

    results = []
    for argument in args:
        if 'd' in argument:
            try:
                rolls = argument[:argument.index('d')]
                faces = int(argument[argument.index('d')+1:])

                if rolls == '':
                    rolls = 1
                else:
                    rolls = int(rolls)
                for c in range(rolls):
                    results.append(randint(1, faces))

                await ctx.send(Text().code_block(f"{rolls} dado(s) de {faces} faces: \n{results} \nA soma foi: {sum(results)}", 'multiple'))
            except ValueError:
                await ctx.send(Text().code_block("Você passou algum parâmetro de forma incorreta, tente novamente, por favor!", 'multiple'))
        else:
            await ctx.send(argument)


# ===================
# COMANDOS DE CONFIGURAÇÕES
# ===================


@bot.command(name='rir')
async def laugh(ctx, *args):
    await ctx.send(':joy_cat:'*10)


# Comando de configurações
@bot.command(name='configs')
async def configs(ctx, *args):
    if len(args) <= 0:  # Se nenhum parâmetro for passado
        embed = discord.Embed(
            title='CONFIGURAÇÕES',
            description='Veja as configurações que podem ser alteradas à seguir:',
            color=discord.Color.blue()
        )
    else:  # Se não
        for command in args:  # Para cada comando nos parâmetros
            if command == 'prefix':
                pass

    await ctx.send('CONFIGURAÇÕES')


# Comando de mostrar os créditos
@bot.command(name='creditos')
async def credit(ctx, *args):
    await ctx.send('Bot criado por João Pedro. Jotinha#0252 :sunglasses:')


bot.run(os.getenv('BOT_TOKEN'))
