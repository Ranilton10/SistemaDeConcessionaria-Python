from database import salvar_carros, carregar_carros

carros = carregar_carros()


def gerar_id():

    if not carros:
        return 1

    ultimo_id = carros[-1]["id"]

    return ultimo_id + 1


def cadastrar_carro():

    marca = input("Qual a marca do carro: ")
    modelo = input("Qual o modelo do carro: ")
    ano = int(input("Qual o ano do carro: "))
    preco = float(input("Qual o preço do carro: "))

    carro = {
        "id": gerar_id(),
        "marca": marca,
        "modelo": modelo,
        "ano": ano,
        "preco": preco
    }

    carros.append(carro)

    salvar_carros(carros)

    print("Carro cadastrado com sucesso!")


def listar_carros():

    if len(carros) == 0:
        print("Não tem nenhum carro cadastrado!")
        return

    for carro in carros:

        print(
            f"ID: {carro['id']} | "
            f"{carro['marca']} - {carro['modelo']} - {carro['ano']} - "
            f"R$ {carro['preco']}"
        )


def buscar_carro():

    busca = input("Digite a marca ou modelo do carro: ").lower()

    encontrados = []

    for carro in carros:

        if busca in carro["marca"].lower() or busca in carro["modelo"].lower():

            encontrados.append(carro)

    if encontrados:

        for carro in encontrados:

            print(
                f"{carro['marca']} - {carro['modelo']} - {carro['ano']} - R$ {carro['preco']}"
            )

    else:

        print("Nenhum carro foi encontrado!")


def remover_carro():

    id_carro = int(input("Digite o ID do carro para remover: "))

    for carro in carros:

        if carro["id"] == id_carro:

            carros.remove(carro)

            salvar_carros(carros)

            print("O carro foi removido!")

            return

    print("O carro não foi encontrado.")


def ordenar_por_marca():

    carros.sort(key=lambda carro: carro["marca"])

    print("Carros ordenados por marca!")


def ordenar_por_preco():

    carros.sort(key=lambda carro: carro["preco"])

    print("Carros ordenados por preço!")


def estatisticas():

    if not carros:
        print("Nenhum carro cadastrado!")
        return

    total = len(carros)

    anos = [carro["ano"] for carro in carros]

    print("Total de carros: ", total)
    print("Carro mais novo: ", max(anos))
    print("Carro mais antigo: ", min(anos))


def relatorio():

    if not carros:
        print("Nenhum carro cadastrado!")
        return

    total_carros = len(carros)

    total_valor = sum(carro["preco"] for carro in carros)

    preco_medio = total_valor / total_carros

    print("\n=== RELATÓRIO DA CONCESSIONÁRIA ===")

    print("Total de carros: ", total_carros)
    print("Valor total do estoque: R$", total_valor)
    print("Preço médio dos carros: ", preco_medio)

