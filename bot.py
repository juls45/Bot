import discord
from bot_logic import gen_pass  # Importa la función gen_pass desde bot_logic

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$password'):
        try:
            # Obtén la longitud solicitada (por ejemplo, "$password 12")
            args = message.content.split()
            if len(args) == 2 and args[1].isdigit():
                length = int(args[1])
                if length > 0:
                    password = gen_pass(length)
                    await message.channel.send(f"Tu contraseña generada es: {password}")
                else:
                    await message.channel.send("Por favor, proporciona una longitud válida mayor a 0.")
            else:
                await message.channel.send("Uso correcto: $password <longitud>")
        except Exception as e:
            await message.channel.send("Ocurrió un error al generar la contraseña.")
            print(e)

client.run("¡EL TOKEN DE TU BOT DEBERÍA ESTAR AQUÍ!")
