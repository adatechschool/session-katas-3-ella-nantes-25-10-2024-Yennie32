# # STEP 1 : import json and print in console
# import json
# import pandas as pd
# from itertools import count
#
#
#
#

#
# # count number of pokemon > 10kg
#
# for pokemon in pokedex_data["pokemon"]:
#     big_pokemon = []
#     # if  pokemon["weight"] >= 10 :
#     big_pokemon.append(pokemon["weight"])
#     sorted_big_pokemon = sorted(big_pokemon)
#     print("weight", sorted_big_pokemon)

import json

class Pokemon :
    def __init__(self, id, name, type, weight, weaknesses):
        self.id, self.name, self.type, self.weight, self.weaknesses = id, name, type, weight, weaknesses

    def __str__(self):
        return f"This is {self.name}, it's a pokemon type {self.type}, it weighs {self.weight}. It's weaknesses are {', '.join(self.weaknesses)}"

    def show_pokemon (self):
        return self.name

    def show_weight(self):
        return self.weight

    @staticmethod # pour faire en sorte que la méthode ne soit pas instanciée
    def count_pokemon (pokemons):
        return len(pokemons)

    @staticmethod
    def big_pokemons (pokemons):
        big_pokemons = []

        for pokemon in pokemons:
            weight_value = float(pokemon.weight.split()[0])
            if weight_value > 10 :
                big_pokemons.append(pokemon)
        return big_pokemons

def load_pokemon(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    pokedex_info = []
    for pokedex_data in data['pokemon']:
        pokemon = Pokemon(
            id=pokedex_data['id'],
            name=pokedex_data['name'],
            type=pokedex_data['type'],
            weight=pokedex_data['weight'],
            weaknesses=pokedex_data['weaknesses']
        )
        pokedex_info.append(pokemon)
    return pokedex_info

pokemons = load_pokemon('pokedex.json')
total_pokemons = Pokemon.count_pokemon(pokemons)
big_pokemons = Pokemon.big_pokemons(pokemons)
sorted_big_pokemons = sorted(big_pokemons, key=lambda p: float(p.weight.split()[0]))
print(f"Total Pokémon: {total_pokemons}")
for pokemon in sorted_big_pokemons:
    print("big pokemons :", pokemon)





#for pokemon in pokemons:
    #print(pokemon)

# # count number of pokemon entries
# def count_pokedex_id (obj, key) :
#     if isinstance(obj, list):
#         return sum(count_pokedex_id(item, key) for item in obj)
#
#     elif isinstance(obj, dict):
#         if key in obj:
#             value = obj[key]
#             if isinstance(value, list):
#                 return len(value)
#             else :
#                 return count_pokedex_id(value, key)
#         else:
#             return 0
#     return 1
#
# pokemon_nb = count_pokedex_id(pokedex_data, 'pokemon')




