import os 
import time

nome = None
cpf = None
saldo = 0

os.system("clear")
user_name = input("coloque seu nome: ")
user_cpf = input("coloque seu CPF: ")

name = user_name
cpf = user_cpf



while True:

    def verify(valor_user):

        number_conversor = int(valor_user)

        if number_conversor == 1:
            os.system("clear")
            print(f"o seu saldo atual: {saldo} R$")
            time.sleep(1)
            return "consulta"

        elif number_conversor == 2:
            os.system("clear")
            user_deposit = int(input("Coloque a quantia: "))
            os.system("clear")
            print(f"Você depositou {user_deposit} R$")
            time.sleep(1)
            return "deposit", user_deposit
        elif number_conversor == 3:
            os.system("clear")
            user_saque = int(input("Quantia de Saque: "))
            os.system("clear")
            print(f"Você sacou {user_saque} R$")
            time.sleep(1)
            return "Sacar", user_saque
            



    if name == "" or cpf == "":
        os.system("clear")
        print("Preencha os campos")
        time.sleep(4)
    else:
        os.system("clear")
        print("1. Consultar Saldo")
        print("2. Depositar")
        print("3. Sacar")
        user_value = input("coloque um numero: ")
        deposit = verify(valor_user=user_value)

        if deposit[0] == "deposit":
            saldo = saldo + deposit[1]

        elif deposit[0] == "Sacar":
            saldo = saldo - deposit[1]
        
        time.sleep(4)

        


