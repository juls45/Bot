# bot_logic.py
import random

def gen_pass(pass_length):
    """
    Genera una contraseña aleatoria de la longitud especificada.
    """
    elements = "+-/*!&$#?=@<>"
    password = "".join(random.choice(elements) for _ in range(pass_length))
    return password

def flip_coin():
    """
    Lanza una moneda al aire y devuelve "Cara" o "Cruz".
    """
    return random.choice(["Cara", "Cruz"])

def random_emoji():
    """
    Devuelve un emoji aleatorio.
    """
    emojis = ["😀", "😂", "🥳", "😎", "🤔", "🎉", "🔥", "💥", "🌟", "🚀"]
    return random.choice(emojis)
