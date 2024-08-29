import keyboard
import sys

class Banco:
    def __init__(self) -> None:
        pass
        self.saldo = 0
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.LIMITE_SAQUES = 3

    def deposito(self):
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            self.saldo += valor
            self.extrato += f"Depósito: R$ {valor:.2f}\n"
        elif valor == 0:
            print("O valor a ser depositado precisa ser maior que zero.")
        else:
            print("Operação falhou! O valor informado é inválido.")
    
    def saque(self):
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > self.saldo

        excedeu_limite = valor > self.limite

        excedeu_saques = self.numero_saques >= self.LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
    
    def mostrar_extrato(self):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("==========================================")

    def menu_banco(self):
        while True:
            key = input("""
Aperte uma das seguintes teclas:
1. Para depósito
2. Para saque
3. Para visualizar extrato
Para cancelar a operação, aperte '4'.\n
""")
            if key == '1':
                self.deposito()
            elif key == '2':
                self.saque()
            elif key == '3':
                self.mostrar_extrato()
            elif key =='4':
                break
            else:
                print("Opção inválida, por favor selecione novamente a operação desejada")

if __name__ == "__main__":
    banco = Banco()
    banco.menu_banco()