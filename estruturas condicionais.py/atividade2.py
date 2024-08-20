numero1 = int(input("digite o primeiro valor:"))
numero2 = int(input("digite o segundo valor:"))
produto = float
soma = float
menor = float
maior =float

media = (numero1 + numero2) /2
produto = numero1 * numero2
soma = numero1 + numero2
if numero1 > numero2:
    maior = numero1
    menor = numero2
    print(f"maior: {numero1}")
    print(f"menor: {numero2}")
else:
    maior = numero2
    menor = numero1
    print(f"maior: {numero2}")
    print(f"menor: {numero1}")    




print(f"media: {media}")
print(f"soma: {soma}")
print(f"produto: {produto}")
