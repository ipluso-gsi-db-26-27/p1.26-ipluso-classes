import random
lmin,lmax = 1,100
numbertoguess = random.randint(lmin,lmax)  

# guess = input(f"adivinha o numero entre {lmin} e {lmax}: -->")

# print(f'valor inserido: {guess}, do tipo ({type(guess).__name__})')
# print(f'{guess.isnumeric()} ;{guess.isdecimal()}')
guess = ""
attempt = 0
tentativas = []

while (guess != numbertoguess and guess != 'end'):
    guess = input(f"adivinha o numero entre {lmin} e {lmax}: -->")

    print(f'valor inserido: {guess}')
    if (guess.isnumeric()):
        guess = int(guess)
        if (guess > numbertoguess):
            print("mais baixo")
        elif (guess < numbertoguess):
            print("mais alto")
        else:
            print("acertou")   
        attempt += 1 # equivalente a attempt = attempt + 1
        tentativas.append(guess) # adiciona a última tentativa ao fim da lista de tentativas
    elif (guess != 'end'):
        print(f"'{guess}' não é um numero inteiro")

if (guess == 'end'):
    print(f'desitiu ao fim de {attempt} tentativas')
else:
    print(f'acertou no numero {numbertoguess} em {attempt} tentativas')
    print(tentativas)
for tentativa in tentativas:
    print(tentativa)