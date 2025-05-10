"""
"""
from faker import Faker
import random

f = Faker()

cantones_loja = [
    "Loja",
    "Calvas",
    "Catamayo",
    "Celica",
    "Chaguarpamba",
    "Espíndola",
    "Gonzanamá",
    "Macará",
    "Olmedo",
    "Paltas",
    "Pindal",
    "Puyango",
    "Quilanga",
    "Saraguro",
    "Sozoranga",
    "Zapotillo"
]

def obtener_id():

    valor = random.randint(10000000, 99999999)
    return valor

def obtener_ciudad_nacimiento():
    """
    """
    return cantones_loja[random.randint(0, len(cantones_loja)-1)]

archivo = open("data/personas.csv", "w")
archivo.write(f"id_persona|nombre|apellido|ciudad_nacimiento\n")
for i in range(0, 200):
    id = obtener_id()
    nombre = f.first_name()
    apellido = f.last_name()
    ciudad_nacimiento = obtener_ciudad_nacimiento()
    archivo.write(f"{id}|{nombre}|{apellido}|{ciudad_nacimiento}\n")
archivo.close()
