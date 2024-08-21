import os 
os.system("cls || clear ")

resultado = 0
numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))
opcao = input("digite uma opção (+, -, *, /): ")

match(opcao):
    case "+":
        resultado = numero1 + numero2 
    case "-":
        resultado = numero1 - numero2 
    case "*":
        resultado = numero1 * numero2 
    case "/":
        resultado = numero1 / numero2 
    case _:
        print(f"opção invalida")

print(f"resultado: {resultado}")

        





