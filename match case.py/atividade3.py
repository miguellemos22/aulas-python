import os 
os.system("cls || clear ")

print("""
    1 - domingo
    2 - segunda
    3 - terça
    4 - quarta
    5 - quinta
    6 - sexta
    7 - sabado
    """)
numero = int(input("digite um numero: "))
match(numero):

    case 1:
     print("final de semana")
    case 2:
        print("dia util")
    case 3:
        print("dia util")
    case 4:
        print("dia util")
    case 5:
        print("dia util")
    case 6:
        print("dia util")
    case 7:
        print("final de semana")
    case _:
        pass
    
