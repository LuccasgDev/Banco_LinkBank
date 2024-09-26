from datetime import datetime
from fpdf import FPDF

informacao_bancaria = {
    "56663322010": {"Nome": "João", "Conta": "026630471", "Agencia": "3318", "Valor": 300, "Movimentacoes": [], "TotalMovimentacoes": 0},
    "97371851021": {"Nome": "Lucas", "Conta": "12330442", "Agencia": "4234", "Valor": 500, "Movimentacoes": [], "TotalMovimentacoes": 0}
}

def registrar_movimentacao(cpf, tipo, valor):
    data_hora = datetime.now().strftime("%d-%m-%Y %H:%M")
    saldo_atual = informacao_bancaria[cpf]["Valor"]
    informacao_bancaria[cpf]["Movimentacoes"].append({"data_hora": data_hora, "tipo": tipo, "valor": valor, "saldo": saldo_atual})
    informacao_bancaria[cpf]["TotalMovimentacoes"] += 1

def saque_conta(cpf):
    if informacao_bancaria[cpf]["TotalMovimentacoes"] >= 10:
        print("Você atingiu o limite de 10 movimentações.")
        return

    while True:
        print("=========")
        print("= SAQUE =")
        print("=========")
        saldo = informacao_bancaria[cpf]["Valor"]
        print(f"O valor que tem em conta é R$ {saldo}")
        valor_saque = int(input("Informe o valor do saque: "))
        if valor_saque > saldo:
            print("O valor do saque é maior que o que tem na conta.")
        elif valor_saque < saldo:
            informacao_bancaria[cpf]["Valor"] -= valor_saque
            registrar_movimentacao(cpf, "Saque", valor_saque)
            print("Saque realizado com sucesso !!")
            print(f"O novo valor da conta é R$ {informacao_bancaria[cpf]['Valor']}")
            registrar_movimentacao(cpf, "Saldo", informacao_bancaria[cpf]["Valor"])
            saque_novamente = input("Deseja sacar novamente (s) ou (n): ")
            if saque_novamente.lower() == "n":
                break
        elif valor_saque == saldo:
            zera_conta = input("Tem certeza que deseja sacar tudo da conta? (s) ou (n): ")
            if zera_conta.lower() == "s":
                informacao_bancaria[cpf]["Valor"] -= valor_saque
                registrar_movimentacao(cpf, "Saque", valor_saque)
                print(f"O novo valor da conta é R$ {informacao_bancaria[cpf]['Valor']}")
                registrar_movimentacao(cpf, "Saldo", informacao_bancaria[cpf]["Valor"])
                break

def deposito(cpf):
    if informacao_bancaria[cpf]["TotalMovimentacoes"] >= 10:
        print("Você atingiu o limite de 10 movimentações.")
        return

    while True:
        print("============")
        print("= Depósito =")
        print("============")
        deposito_conta = int(input("Digite o valor para depositar: "))
        informacao_bancaria[cpf]["Valor"] += deposito_conta
        registrar_movimentacao(cpf, "Depósito", deposito_conta)
        print("Depósito realizado com sucesso !!")
        print(f"A conta agora tem R$ {informacao_bancaria[cpf]['Valor']}")
        registrar_movimentacao(cpf, "Saldo", informacao_bancaria[cpf]["Valor"])
        deposito_continuar = input("Deseja continuar o depósito (s) ou (n): ")
        if deposito_continuar.lower() == "n":
            print("Obrigado por depositar em nosso Banco")
            break

def transferencia_bancaria(cpf):
    if informacao_bancaria[cpf]["TotalMovimentacoes"] >= 10:
        print("Você atingiu o limite de 10 movimentações.")
        return

    while True:
        conta_verificar = input("Digite o CPF da conta para transferência: ")
        if conta_verificar in informacao_bancaria:
            valor_transferir = int(input("Digite o valor para a transferência: "))
            if valor_transferir > informacao_bancaria[cpf]["Valor"]:
                print("Saldo insuficiente para a transferência.")
            else:
                informacao_bancaria[conta_verificar]["Valor"] += valor_transferir
                informacao_bancaria[cpf]["Valor"] -= valor_transferir
                registrar_movimentacao(cpf, "Transferência", valor_transferir)
                print("O valor foi transferido com sucesso !!")
                print(f"A sua conta agora tem R$ {informacao_bancaria[cpf]['Valor']}")
                registrar_movimentacao(cpf, "Saldo", informacao_bancaria[cpf]["Valor"])
        else:
            print("Conta não encontrada.")
        
        continuar_transferencia = input("Deseja continuar com transferências (s) ou (n): ")
        if continuar_transferencia.lower() == "n":
            break

def extrato(cpf):
    print("\n===== EXTRATO =====")
    for movimentacao in informacao_bancaria[cpf]["Movimentacoes"]:
        if movimentacao["tipo"] == "Saldo":
            print(f"{movimentacao['data_hora']} - Saldo: R$ {movimentacao['saldo']}")
        else:
            print(f"{movimentacao['data_hora']} - {movimentacao['tipo']}: R$ {movimentacao['valor']}")
    print("===================")

def menu():
    while True:
        entrar_conta = input("Digite seu CPF para entrar na conta ou pressione (E) para sair: ")
        if entrar_conta.lower() == "e":
            print("Obrigado por utilizar o nosso Banco !!")
            break
        if entrar_conta in informacao_bancaria:
            while True:
                print("========================")
                print(f"Bem-vindo {informacao_bancaria[entrar_conta]['Nome']} ao Banco LINK!")
                print("========================")
                print("1 - Saque")
                print("2 - Depósito")
                print("3 - Transferência")
                print("4 - Extrato")
                print("5 - Sair")
                menu_opcao = int(input("Selecione uma opção: "))
                match menu_opcao:
                    case 1:
                        saque_conta(entrar_conta)
                    case 2:
                        deposito(entrar_conta)
                    case 3:
                        transferencia_bancaria(entrar_conta)
                    case 4:
                        extrato(entrar_conta)
                    case 5:
                        print("Obrigado por utilizar o nosso Banco!")
                        break
                    case _:
                        print("Opção inválida. Tente novamente.")
        else:
            print("Erro em localizar a conta !!")

menu()
