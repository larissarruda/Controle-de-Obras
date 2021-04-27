import os

NFs = {}


def continuar():
    opcao = input(" ** Deseja fazer adicionar nova nota fiscal (S/N)? ")
    if opcao == "N":
        menu_op()
        coletar_opcao()
    else:
        coletar_NFs()


def limpar_tela():
    os.system("clear")
    print("** Orçamento de Obras. **")


def menu_inicial():
    print("** Orçamento de Obras. **")
    valor = float(input("Qual seu investimento inicial? "))
    return valor
    limpar_tela()

def menu_op():
    limpar_tela()
    print("Opções: ")
    print("1 - Inserir nota fiscal e sua descrição.")
    print("2 - Mostre-me quanto tenho agora. ")


def coletar_opcao():
    opcao = int(input("Qual a sua opção: "))

    return opcao


def coletar_NFs():
    descricao = input("Insira uma descrição: ")
    valor = int(input("Insira um valor: "))
    NFs[descricao]=valor
    print(NFs)
    continuar()


valor = menu_inicial()


def saldo():
    gastos = sum(NFs)
    return valor - gastos


while True:

    menu_op()
    opcao = coletar_opcao()
    if opcao == 1:
        coletar_NFs()
    if opcao == 2:
        saldo = saldo()
        if(saldo < 0):
            print(f"Você está devendo R${saldo}")
        else:
            print(f"Você ainda tem R${saldo}")