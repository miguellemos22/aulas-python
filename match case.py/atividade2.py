import os 
os.system("cls || clear ")



print("""
      
      1 - picanha
      2 - lasanha
      3 - strogonoff
      4 - bife acebolado
      5 - pão com ovo

      """)
prato = int(input("selecione o prato desejado: "))

match(prato):
    case 1:
        print("picanha = 25.00")
    case 2:
        print("lasanha = 20.00")
    case 3:
        print("strogonoff = 18.00")
    case 4:
        print("bife acebolado = 15.00")
    case 5: 
        print("pão com ovo = 5.00")
    case _:
        pass
    
   
