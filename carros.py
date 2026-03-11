from database import salvar_carros, carregar_carros

carros = carregar_carros()

def cadastrar_carro():
    marca = input("Qual a marca do carro: ")
    modelo = input("Qual o modelo do carro: ")
    ano = int(input("Qual o ano do carro: "))

    carro = {
        "marca": marca,
        "modelo": modelo,
        "ano": ano

    }

    carros.append(carro)

    salvar_carros(carros)

    print("Seu carro foi cadastrado com êxito!")

