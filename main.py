from carros import *

def menu():

    while True:

        print("\n=== Sistema da Concessionária ===")
        print("1 - Cadastrar carro")
        print("2 - Listar carros")
        print("3 - Buscar carro")
        print("4 - Remover carro")
        print("5 - Ordenar carros")
        print("6 - Estatísticas da Concessionária")
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
            ordenar_carros()

        elif opcao == "6":
            estatisticas()

        elif opcao == "0":
            print("Ok... encerrando o sistema da concessionária!")
            break

        else:
            print("Opção inválida!")


menu()

