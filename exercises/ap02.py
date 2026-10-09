import sys
sys.stdout.reconfigure(encoding="utf-8")
# comentario
'''
comentario de varias linhas
'''

nome = 'Luis A. Gomes'
print("olá " + nome)

print(f"Olá {nome}, \nbem-vindo!")

# receber dados de utilizador
# uc = input(f"Olá {nome}, escreve o nome de uma disciplina:")

print("Olá {nome}, \nbem-vindo a {uc}!")

print("nome é do tipo: " + type(nome).__name__)