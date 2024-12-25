#importando bibliotecas
import os 
import time

#criando variariaveis
nome = None
cpf = None
saldo = 0

#dados a serem inseridos para acessar o sistema
os.system("clear")
user_name = input("coloque seu nome: ")
user_cpf = input("coloque seu CPF: ")

name = user_name
cpf = user_cpf


#inicio do sistema
while True:

    #funcao que pega o valor que o usuario insere para fazer consultas, saque, deposito
    def verify(valor_user):

        number_conversor = int(valor_user)

        #consulta da variavel saldo
        if number_conversor == 1:
            os.system("clear")
            print(f"o seu saldo atual: {saldo} R$")
            time.sleep(1)
            return "consulta"

        #sistema para Deposito
        elif number_conversor == 2:
            os.system("clear")
            user_deposit = int(input("Coloque a quantia: "))
            os.system("clear")
            print(f"Você depositou {user_deposit} R$")
            time.sleep(1)
            return "deposit", user_deposit

        #sistema de Saque
        elif number_conversor == 3:
            os.system("clear")
            user_saque = int(input("Quantia de Saque: "))
            os.system("clear")
            print(f"Você sacou {user_saque} R$")
            time.sleep(1)
            return "Sacar", user_saque
            


    #validador dos dados do cliente caso esteje vazio
    if name == "" or cpf == "":
        os.system("clear")
        print("Preencha os campos")
        time.sleep(4)
    
    else:
        #sistema que pega o valor do usuario para leva-lo há funcao a cima
        os.system("clear")
        print("1. Consultar Saldo")
        print("2. Depositar")
        print("3. Sacar")
        user_value = input("coloque um numero: ")

        #a fucao retorna 2 valores, o tipo de valor e o valor em si
        deposit = verify(valor_user=user_value)

        #se o usuario depositar, sera retornado um index em string e um valor que sera somado na variavel saldo
        if deposit[0] == "deposit":
            saldo = saldo + deposit[1]

        #se o usuario sacar, sera retornado um index em string e um valor que sera subtraido na variavel saldo
        elif deposit[0] == "Sacar":
            saldo = saldo - deposit[1]
        
        time.sleep(4)

        


