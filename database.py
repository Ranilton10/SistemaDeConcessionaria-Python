import json

def salvar_carros(carros):

    with open("carros.json", "w") as arquivo:
        json.dump(carros, arquivo, indent = 4)


