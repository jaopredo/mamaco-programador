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


@bot.event
async def on_ready():
    print("Logged successfully!")


# ===================
# COMANDOS DO RPG
# ===================

# Iniciar o personagem
@bot.command(name='iniciar', help='Comando que inicia o personagem.\n?iniciar')
async def iniciar(ctx, *args):
    await ctx.send('COMANDO DE INICIAR PERSONAGEM')


# Criar um personagem que já está feito
@bot.command(name='login', help='Faz login em um personagem que já existe.\n?login <senha>')
async def login(ctx, *args):
    await ctx.send('COMANDO DE LOGAR O PERSONAGEM')


# Comando para ver o personagem
@bot.command(name='ver', help='Ver atributos de um personagem com base no seu nome\n?ver <nome>')
async def ver(ctx, *args):
    await ctx.send('COMANDO DE VER O PERSONAGEM')


# ===================
# COMANDOS GERAIS
# ===================

# Comando de rolar um dado
@bot.command(name='rolar', help='Comando que rola um dado na estrutura:\n1d20(Operação) -> 1d20+3, 2d10*2, etc.\n?rolar <dado><operação>')
async def rolar(ctx, *args):
    # Validando para caso o usuário não tenha passado nenhum parâmetro
    if len(args) == 0:
        await ctx.send("Por favor, passe os parâmetros corretos!")
        return

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

# Comando de mostrar os créditos
@bot.command(name='creditos', help='Comando para dar os créditos\n?creditos')
async def creditos(ctx, *args):
    await ctx.send('Bot criado por João Pedro. Jotinha#0252 :sunglasses:')


# ===================
# COMANDOS DE AJUDA
# ===================

# Comando de ajuda
@bot.command(name='ajuda', help='Comando que mostra os outros comandos...')
async def ajuda(ctx, comando='', *args):
    default_commands = {  # Dicionário contendo os comandos do bot
        'RPG:': [
            iniciar,
            login,
            ver
        ],
        'GERAL': [
            rolar
        ],
        'CRÉDITOS': [
            creditos
        ]
    }

    if comando == '':  # Se não tiver passado nenhum comando (Apenas digitei ?ajuda)
        embed = generate_embed(  # Eu gero um EMBED contendo os comandos
            'AJUDA',
            'Eu sou Pedro, o Mamaco Programador, e esta mensagem serve para dar uma ajudinha sobre os comandos que posso interpretar, o corno'
            'do João Pedro tá terminando de fazer o resto dos comandos, inclusive os do RPG, então é só ter um pouquinho de paciência :)',
            default_commands,
            discord.Color.blue(),
            False
        )
        await ctx.send(embed=embed)  # Mostro o comando no chat do discord
    else:  # Se não
        for lista in default_commands.values():  # Para cada lista dentro dos valores de default_commands
            for command in lista:  # Para cada comando dentro dessas listas
                if command.name == comando:  # Se o comando da lista for igual ao comando passado pelo usuário
                    formated_command = discord.Embed(
                        title=f'Comando {Text().italic(command.name)}',
                        description=command.help,
                        color=discord.Color.blue()
                    )
                    await ctx.send(embed=formated_command)
                    return
        else:
            await ctx.send('O comando informado não está na lista dos comandos cadstrados, por favor tente novamente')
            

@bot.command()
async def dm(ctx, person, *message):
    await person.send(message)


bot.run(os.getenv('BOT_TOKEN'))
