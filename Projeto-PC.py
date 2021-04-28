import os
import time

NFs = {}
stop = True


def continuar():
    opcao = input("\n -> Deseja fazer adicionar nova nota fiscal (S/N)? ")
    if opcao == "N":
        limpar_tela()
    elif opcao == "S":
        coletar_NFs()
    else:
        print("Opção inválida!! Tente novamente.")
        continuar()


def limpar_tela():
    os.system("clear")


def cabecalho():
    print("-" * 22)
    print("| ORÇAMENTO DE OBRAS |")
    print("-" * 22)


def menu_inicial():
    cabecalho()
    valor = float(input("Qual seu investimento inicial? "))
    return valor


def menu_op():
    cabecalho()
    print("Opções: ")
    print("1 - Inserir nota fiscal e sua descrição.")
    print("2 - Mostre-me quanto tenho agora. ")
    print("3 - Mostrar o que comprei. ")

    print("0 - Terminar orçamento. ")


def coletar_opcao():
    opcao = int(input("Qual a sua opção? "))

    return opcao


def coletar_NFs():
    limpar_tela()
    cabecalho()
    descricao = input("Insira os itens da sua Nota Fiscal: ")
    valor = float(input("Insira o valor da sua Nota Fiscal: "))
    NFs[descricao] = valor
    #print(NFs)
    continuar()


def saldo():
    gastos = NFs.values()
    gastos = valor - sum(gastos)
    return gastos


def compras():
    for x in NFs:
        print(f"Item(s) da NF: {x}")
        print(f"Valor da NF: R$ {NFs[x]}")


valor = menu_inicial()
limpar_tela()
while stop is True:
    menu_op()
    opcao = coletar_opcao()
    if opcao == 1: 
        coletar_NFs()
    if opcao == 2:
        limpar_tela()
        cabecalho()
        if (saldo() < 0):
            print(f"Você está devendo R$ {(-1) * saldo():.2f}")
            time.sleep(3)
            limpar_tela()
        else:
            print(f"Você ainda tem R$ {saldo():.2f}")
            time.sleep(3)
            limpar_tela()
    if opcao == 3:
        limpar_tela()
        cabecalho()
        compras()
        time.sleep(2)
        limpar_tela()
    if opcao == 0:
        stop = False
