saldo = 1000  # Supondo um saldo inicial de R$ 1000 para demonstração
historico = []  # Lista para armazenar o histórico de transações

# Variáveis para controlar os saques por dia
saques_no_dia = 0
total_sacado_no_dia = 0


def saque(saldo, saques_no_dia, total_sacado_no_dia):
    print("Você escolheu Saque")

    # Verifica se excedeu o limite de saques no dia
    if saques_no_dia >= 3:
        print("Você atingiu o limite máximo de saques por dia.")
        return saldo, saques_no_dia, total_sacado_no_dia

    valor = float(input("Digite o valor que deseja sacar: "))

    # Verifica se o valor do saque excede o limite por saque
    if valor > 500:
        print("O valor máximo por saque é de R$ 500.")
        return saldo, saques_no_dia, total_sacado_no_dia

    # Verifica se o valor do saque exce de o saldo disponível
    if valor <= saldo:
        saldo -= valor
        historico.append(("Saque", valor))
        print("Saque efetuado com sucesso. Saldo restante:", saldo)

        # Atualiza os contadores de saques no dia e total sacado no dia
        saques_no_dia += 1
        total_sacado_no_dia += valor
    else:
        print("Saldo insuficiente.")

    return saldo, saques_no_dia, total_sacado_no_dia


def deposito(saldo):
    print("Você escolheu Depósito")
    valor = float(input("Digite o valor que deseja depositar: "))
    # Aqui você pode adicionar a lógica para processar o depósito
    saldo += valor
    historico.append(("Depósito", valor))
    print("Depósito efetuado com sucesso. Novo saldo:", saldo)
    return saldo


def extrato(saldo):
    print("Você escolheu Extrato")
    print("Histórico de transações:")
    for transacao in historico:
        tipo, valor = transacao
        print(f"{tipo}: R$ {valor}")
    print("Saldo disponível:", saldo)


while True:
    print("--------------------------")
    print("----- Banco Linkbank ----")
    print("--------------------------")
    print("Escolha uma opção:")
    print("1 - Saque")
    print("2 - Depósito")
    print("3 - Extrato")
    print("4 - Sair")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        saldo, saques_no_dia, total_sacado_no_dia = saque(saldo, saques_no_dia, total_sacado_no_dia)
    elif opcao == "2":
        saldo = deposito(saldo)
    elif opcao == "3":
        extrato(saldo)
    elif opcao == "4":
        print("Saindo do Banco Linkbank. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
