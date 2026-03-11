import json

def salvar_carros(carros):

    with open("carros.json", "w") as arquivo:
        json.dump(carros, arquivo, indent = 4)


def carregar_carros():

    try:
        with open("carros.json", "r") as arquivo:
            return json.load(arquivo)
        
    except FileNotFoundError:
        return[]
    

