from database import salvar_carros, carregar_carros

carros = carregar_carros()


def gerar_id():

    if not carros:
        return 1

    ultimo_id = carros[-1]["id"]

    return ultimo_id + 1


def cadastrar_carro():

    marca = input("Qual a marca do carro: ")
    modelo = input("\nQual o modelo do carro: ")
    ano = int(input("\nQual o ano do carro: "))
    preco = float(input("\nQual o preço do carro: "))

    carro = {
        "id": gerar_id(),
        "marca": marca,
        "modelo": modelo,
        "ano": ano,
        "preco": preco
    }

    carros.append(carro)

    salvar_carros(carros)

    print("\nCarro cadastrado com sucesso!")


def listar_carros():

    if len(carros) == 0:
        print("\nNão tem nenhum carro cadastrado!")
        return

    for carro in carros:

        print(
            f"ID: {carro['id']} | "
            f"{carro['marca']} - {carro['modelo']} - {carro['ano']} - "
            f"R$ {carro['preco']}"
        )


def buscar_carro():

    busca = input("\nDigite a marca ou modelo do carro: ").lower()

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

        print("\nNenhum carro foi encontrado!")


def remover_carro():

    id_carro = int(input("\nDigite o ID do carro para remover: "))

    for carro in carros:

        if carro["id"] == id_carro:

            carros.remove(carro)

            salvar_carros(carros)

            print("\nO carro foi removido!")

            return

    print("\nO carro não foi encontrado!")


def atualizar_carro():

    id_carro = int(input("\nDigite o ID do carro que deseja atualizar: "))

    for carro in carros:

        if carro["id"] == id_carro:

            print("\nDigite os novos dados do carro")

            carro["marca"] = input("\nNova marca do carro: ")
            carro["modelo"] = input("\nNovo modelo do carro: ")
            carro["ano"] = int(input("\nNovo ano do carro: "))
            carro["preco"] = float(input("\nNovo preço do carro: "))

            salvar_carros(carros)

            print("\nO carro foi atualizado com sucesso!")

            return

    print("\nO carro não foi encontrado!")


def ordenar_por_marca():

    carros.sort(key=lambda carro: carro["marca"])

    print("\nCarros ordenados por marca!")


def ordenar_por_preco():

    carros.sort(key=lambda carro: carro["preco"])

    print("\nCarros ordenados por preço!")


def estatisticas():

    if not carros:
        print("\nNenhum carro cadastrado!")
        return

    total = len(carros)

    anos = [carro["ano"] for carro in carros]

    print("\nTotal de carros: ", total)
    print("\nCarro mais novo: ", max(anos))
    print("\nCarro mais antigo: ", min(anos))


def relatorio():

    if not carros:
        print("\nNenhum carro cadastrado!")
        return

    total_carros = len(carros)

    total_valor = sum(carro["preco"] for carro in carros)

    preco_medio = total_valor / total_carros

    print("== RELATÓRIO DA CONCESSIONÁRIA ==")

    print("\nTotal de carros: ", total_carros)
    print("\nValor total do estoque: R$", total_valor)
    print("\nPreço médio dos carros: ", preco_medio)

