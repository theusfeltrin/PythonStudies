menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

balance = 0
limite = 500
extract = []
withdraw_number = 0
withdraw_limit = 3

while True:

    option = input(menu)

    if option == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            balance += valor
            extract.append(f"Depósito: R$ {valor:.2f}\n")

        else:
            print("O valor informado é inválido.")

    elif option == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > balance:
            print("Você não tem saldo suficiente.")

        elif valor > limite:
            print(" O valor do saque excede o limite.")

        elif withdraw_number >= withdraw_limit:
            print(" Número máximo de saques excedido.")

        elif valor > 0:
            balance -= valor
            extract.append(f"Saque: R$ {valor:.2f}\n")
            withdraw_number += 1

        else:
            print("O valor informado é inválido.")

    elif option == "e":
        print("\n================ EXTRATO ================")
        if len(extract) > 0:
          for operacao in extract:
              print(operacao)
        else: 
            print("Não foram realizadas movimentações.")
        print(f"\nSaldo: R$ {balance:.2f}")
        print("==========================================")

    elif option == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")