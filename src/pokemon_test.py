
from pokemon import *


if __name__ == "__main__":
<<<<<<< HEAD
    fichero = "./data/pokemon/pokemon.csv"
=======
    fichero = "./FP-Proyecto-Python-1B/data/pokemon/pokemon.csv"
>>>>>>> d9b7dd2beaafe4e30351944e6db349f2cc00c6cb
    pokemon = leer_pokemons(fichero)


def test_leer_pokemons(pokemon):
    print("Ejercicio 1:")
    print("Los 3 primeros datos leidos son \n",pokemon[:3])
    print("Los 3 ultimos datos leidos son \n",pokemon[-3:])

def test_filtrar_pokemon_tipo(pokemon):
    print("Ejercicio 2:")
    print("- Número de pokemon de tipo {} : {}".format("Poison", len(filtrar_pokemon_tipo (pokemon, "Poison"))))

def test_conjunto_de_tipos(pokemon):
    print("Ejercicio 3:")
    print("- Conjunto de tipos de los pokemon : {}".format(conjunto_de_tipos (pokemon)))
    


test_leer_pokemons(pokemon)
test_filtrar_pokemon_tipo(pokemon)
test_conjunto_de_tipos(pokemon)

