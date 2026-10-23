# escrever um programa que aceita entradas do utilizador
# adicionando-as a uma lista até o utilizador escrever 'end'
# quando o utilizador escreve 'fim', o programa apresenta a 
# a lista em ecra, uma linha de cada vez, sem o 'fim'

texto = ""
lista = []

while (texto != 'end'):
        texto = input('escreve qualquer coisa:')
#        if (texto != 'end'):
        lista.append(texto)
lista.remove('end')
for texto in lista:
    print(texto)