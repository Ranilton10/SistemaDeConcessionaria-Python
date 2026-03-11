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


def listar_carros():

    if len(carros) == 0:
        print("Não tem carros cadastrados!")
        return
    
    for carro in carros:
        print(f"{carro['marca']} - {carro['modelo']} - {carro['ano']}")


def buscar_carro():

    busca = input("Digite a marca do carro: ")

    for carro in carros:

        if carro["marca"].lower() == busca.lower():

            print("Encontramos o carro:")
            print(f"{carro['marca']} - {carro['modelo']} - {carro['ano']}")
            return

    print("O carro não foi encontrado!")


def remover_carro():

    modelo = input("Digite o modelo do carro para remover: ")

    for carro in carros:

        if carro["modelo"].lower() == modelo.lower():

            carros.remove(carro)

            salvar_carros(carros)

            print("Carro removido com êxito!")
            return

    print("O carro não foi encontrado!")


