# STEP 1 : import json and print in console
import json
from itertools import count

with open('pokedex.json', 'r') as pokedex_file:
    pokedex_data = json.load(pokedex_file)
    print(json.dumps(pokedex_data, indent=4))


# count number of pokemon entries
def count_pokedex_id (obj, key) :
    if isinstance(obj, list):
        return sum(count_pokedex_id(item, key) for item in obj)

    elif isinstance(obj, dict):
        if key in obj:
            value = obj[key]
            if isinstance(value, list):
                return len(value)
            else :
                return count_pokedex_id(value, key)
        else:
            return 0
    return 1

pokemon_nb = count_pokedex_id(pokedex_data, 'pokemon')
pokemon_weight = count_pokedex_id(pokedex_data, 'weight')
print("Number of pokemon entries : ", pokemon_weight)

def big_pokemon (data, key):
    

# count number of pokemon > 10kg

# def parse_json(data):
#     result = {}
#     for key, value in data.items():
#         if isinstance(value, dict):
#             result[key] = parse_json(value)
#
#         else:
#             result[key] = value
#     return result
#
# pokedex_str = json.dumps(pokedex_data)
#



# print("type", type(pokedex_data))
# print(pokedex_str)
# parsed_data = parse_json(json.loads(pokedex_str))
# weight = parsed_data['pokemon']['weight']
#
# print("weight", weight)