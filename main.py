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
bot = commands.Bot(command_prefix=options['configs']['prefix'], help_command=None)
default_commands = {  # Dicionário contendo os comandos do bot
    'RPG:': [
        'iniciar',
        'login',
        'ver'
    ],
    'GERAL': [
        'rolar'
    ],
    'CRÉDITOS': [
        'creditos'
    ]
}


@bot.event
async def on_ready():
    print("Logged successfully!")


# Comando de ajuda
@bot.command(name='help')
async def ajuda(ctx, *args):
    embed = generate_embed(
        'AJUDA',
        'Eu sou Pedro, o Mamaco Programador, e esta mensagem serve para dar uma ajudinha sobre os comandos que posso interpretar, o corno'
        'do João Pedro tá terminando de fazer o resto dos comandos, inclusive os do RPG, então é só ter um pouquinho de paciência :)',
        default_commands,
        discord.Color.blue(),
        False
    )

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
    # Validando para caso o usuário não tenha passado nenhum parâmetro
    if len(args) == 0:
        await ctx.send("Por favor, passe os parâmetros corretos!")

    results = []
    index = None  # Index que vou utilizar para fazer as operações complexas
    for argument in args:
        for letter in argument:  # Para cada letra dentro do argumento
            if letter in '+-*/':  # Se a letra estiver dentre os símbolos
                index = argument.index(letter)  # Eu pego o índice do símbolo
    
    dado = argument[:index] if bool(index) else argument[:]  # Pego o dado
    
    qtd = int(dado[:dado.index('d')])  # Quantidade de vezes que vou girar
    faces = int(dado[dado.index('d')+1:])  # Faces do dado
    operacao = argument[index:] if bool (index) else ""  # Pego a operação matemática passada

    for c in range(qtd):  # Faço a escolha dos resultados aleatoriamente
        results.append(randint(1, faces))  # Adiciono o resultado em uma lista
    
    soma = sum(results)  # Calcula a soma dos resultados

    soma_final = calcular_dado(soma, operacao)  # Calcula a soma final

    await ctx.send(Text().code_block(f"Dado de {faces} faces girado {qtd} vezes \nResultado(s): {results} -> {soma}\n"
                                        f"{soma}{operacao} = {soma_final}", 'multiple'))


# ===================
# COMANDOS DE CONFIGURAÇÕES
# ===================


@bot.command(name='rir')
async def laugh(ctx, *args):
    await ctx.send(':joy_cat:'*10)


# Comando de mostrar os créditos
@bot.command(name='creditos')
async def credit(ctx, *args):
    await ctx.send('Bot criado por João Pedro. Jotinha#0252 :sunglasses:')


bot.run(os.getenv('BOT_TOKEN'))
