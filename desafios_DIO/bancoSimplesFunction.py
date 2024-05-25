import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [n]\tNova Conta
    [l]\tLista Contas
    [u]\tNovo usuario
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def withdraw(*, value, balance, limit, withdraw_limit, withdraw_number, extract):
    if value > balance:
        print("\nVocê não tem saldo suficiente.")
    elif value > limit:
        print("\nO valor do saque excede o limite.")
    elif withdraw_number >= withdraw_limit:
        print("\nNúmero máximo de saques excedido.")
    elif value > 0:
        balance -= value
        extract.append(f"Saque: R$ {value:.2f}\n")
        withdraw_number += 1
    else:
        print("\nO valor informado é inválido.")

    return balance, extract


def deposit(balance, value, extract, /):
    if value > 0:
        balance += value
        extract.append(f"Depósito: R$ {value:.2f}\n")
        print("\n=== Deposito realizado com sucesso. ===")
    else:
        print("\n O valor informado é inválido.")

    return balance, extract


def get_extract(balance, /, *, extract):
    print("\n================ EXTRATO ================")
    if len(extract) > 0:
        for operacao in extract:
            print(operacao)
    else:
        print("Não foram realizadas movimentações.")
    print(f"\nSaldo: R$ {balance:.2f}")
    print("==========================================")


def filter_user(cpf, users):
    for user in users:
        if user["cpf"] == cpf:
            return user
        else:
            return None


def create_users(users):
    cpf = input("Informe o CPF (somente numeros): ")
    user = filter_user(cpf, users)

    if user:
        print("\n Ja existe usuario com esse CPF")
        return

    name = input("Informe o nome completo: ")
    birthday = input("Informe a data de nascimento (dd-mm-aaaa): ")
    address = input(
        "Informe o endereco (logradouro, nro - bairro - cidade/sigla estado)")

    users.append({"name": name, "birthday": birthday,
                 "cpf": cpf, "address": address})

    print("Usuario criado com sucesso!")


def create_account(agency, account_number, accounts, users):
    cpf = input("Informe o CPF (somente numeros): ")
    user = filter_user(cpf, users)

    if user:
        print("\n Conta criada com sucesso.")
        accounts.append(
            {"agency": agency, "account_number": account_number, "user": user})

    print("\n Usuario nao encontrado, fluxo encerrado.")


def list_accounts(accounts):
    for account in accounts:
        text = f"""\
          Agencia: \t{account['agency']}
          C/C: \t{account['account_number']}
          Titular: \t{account['user']['name']}
        """
        print('=' * 100)
        print(textwrap.dedent(text))


def main():
    # configs
    agency = "0001"
    withdraw_limit = 3

    # variables
    balance = 0
    limit = 500
    extract = []
    withdraw_number = 0
    users = []
    accounts = []
    account_number = 1

    # main loop
    while True:

        option = menu()

        if option == "d":
            value = float(input("Informe o valor do depósito: "))

            balance, extract = deposit(balance, value, extract)

        elif option == "s":
            value = float(input("Informe o valor do saque: "))

            balance, extract = withdraw(
                balance=balance,
                extract=extract,
                limit=limit,
                value=value,
                withdraw_limit=withdraw_limit,
                withdraw_number=withdraw_number
            )

        elif option == "e":
            get_extract(balance, extract=extract)

        elif option == "n":
            create_account(agency, account_number, accounts, users)
            account_number += 1

        elif option == "l":
            list_accounts(accounts)

        elif option == "u":
            create_users(users)

        elif option == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
