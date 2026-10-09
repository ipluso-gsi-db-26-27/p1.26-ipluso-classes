'''
Escrever uma aplicação que recebe 2 numero do utilizador
E devolve a soma
'''

num1 = input("Escreve o primeiro numero")
num2 = input("Escreve o segundo numero")

if type(num1).__name__ == 'str':
    print(f"{num1} é uima string")

num1 = float(num1)

print(f"soma: {num1} + {num2} = {num1+int(num2)}")