from carros import *
from utils import titulo

def menu():

    while True:

        titulo("SISTEMA DA CONCESSIONÁRIA")

        print("1 - Cadastrar carro")
        print("2 - Listar carros")
        print("3 - Buscar carro")
        print("4 - Remover carro")
        print("5 - Ordenar carros por marca")
        print("6 - Ordenar carros por preço")
        print("7 - Estatísticas da concessionária")
        print("8 - Relatório da concessionária")
        print("9 - Atualizar carro")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_carro()

        elif opcao == "2":
            listar_carros()

        elif opcao == "3":
            buscar_carro()

        elif opcao == "4":
            remover_carro()

        elif opcao == "5":
            ordenar_por_marca()

        elif opcao == "6":
            ordenar_por_preco()

        elif opcao == "7":
            estatisticas()

        elif opcao == "8":
            relatorio()

        elif opcao == "9":
            atualizar_carro()

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida!")


menu()

