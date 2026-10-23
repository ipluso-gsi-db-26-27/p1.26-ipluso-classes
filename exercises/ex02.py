'''
Escrever uma aplicação que recebe 2 numero do utilizador
E devolve a soma
'''

'''
num1 = input("Escreve o primeiro numero")
num2 = input("Escreve o segundo numero")

if type(num1).__name__ == 'str':
    print(f"{num1} é uma string")

num1 = float(num1)

print(f"soma: {num1} + {num2} = {num1+int(num2)}")
'''
import random
lmin,lmax = 1,1000
numbertoguess = random.randint(lmin,lmax)  

# guess = input(f"adivinha o numero entre {lmin} e {lmax}: -->")

# print(f'valor inserido: {guess}, do tipo ({type(guess).__name__})')
# print(f'{guess.isnumeric()} ;{guess.isdecimal()}')
guess = ""
attempt = 0

while (guess != numbertoguess and guess != 'end'):
    guess = input(f"adivinha o numero entre {lmin} e {lmax}: -->")

    print(f'valor inserido: {guess}')
    if (guess.isnumeric()):
        guess = int(guess)
        print(f"numero inserido: {guess}")
        if (guess > numbertoguess):
            print("mais baixo")
        elif (guess < numbertoguess):
            print("mais alto")
        else:
            print("acertou")   
        attempt += 1
    elif (guess != 'end'):
        print(f"{guess} não é um numero inteiro")

if (guess == 'end'):
    print(f'desitiu ao fim de {attempt} tentativas')
else:
    print(f'acertou no numero {numbertoguess} em {attempt} tentativas')