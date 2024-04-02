import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
                
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)


@bot.command()
async def reciclaje(ctx):
    with open('image/r1.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send(" escoge el producto con menor envase o envases que puedas reciclar. Separa la basura orgánica de los envases. Separa los envases dependiendo de su material: plásticos, vidrio, aluminio o metal. Coloca cada envase en el contenedor que corresponde.")

@bot.command()
async def contaminacion(ctx):
    with open('images/c1.png', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    await ctx.send("Se entiende por contaminación ambiental cuando existe la presencia de sustancias nocivas en el agua, aire o suelo.")

problemas = [
    "Calentamiento global.",
    "Lluvia acida.",
]

problem = [
    "Calentamiento global.",
    "Lluvia acida.",
]

@bot.command()
async def problemas(ctx):
    consejo = random.choice(problem)
    await ctx.send(problem)}


bot.run("token")
