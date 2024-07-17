
import discord
import random
import os
import requests 
from  discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot y aconsejante pata evitas contaminacion {bot.user}!')

@bot.command()
async def mem(ctx):
    lista_de_imagenes = os.listdir('images')
    image_aleatoria = random.choice(lista_de_imagenes)
    with open(f'images/{image_aleatoria}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def menos_contaminacion(ctx):
    await ctx.send(f'la mejor manera de tener menos contaminacion es reciclanso y comprando solo lo que nececitas {bot.user}!')

@bot.command()
async def como_reciclar(ctx):
    await ctx.send(f'asegurate de botas las cosas reciclables en los basureros correctos y no compres cosas nuevas a menos que la antigua no se pueda usar {bot.user}!')

@bot.command()
async def comprar_menos(ctx):
    await ctx.send(f'intenta no comprar tanta ropa o cosas que no nececitas {bot.user}!')

bot.run("token")
