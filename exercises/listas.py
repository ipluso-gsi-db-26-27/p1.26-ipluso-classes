"""
Listas são coleções dinâmicas (i.e. podem ser alteradas) e ordenadas de elementos.
Cada elemento da lista pode ser de tipos diferente, incluindo outras listas.
Als listas são definidas por parenteses retos [] e os elementos são separados por vírgulas.
Cada elemento da lista tem um número de ordem, ou índice, que começa em 0.
Sendo dinâmicas, podem ser alteradas, adicionando, removendo ou modificando os seus elementos."""
# criar uma lista (vazia)
singular =[]

# criar uma lista com elementos
pessoas = ['eu','tu','ele','nós','vos','eles']

# aceder a elementos da lista por índice
print(f"A primeira pessoa do plural é {pessoas[3].upper()}")
print(pessoas)

# acrescentar elementos à lista: método append()
# Adiciona o elemento ao fim da lista
singular.append('eu')
singular.append('ele')

#adicionar elementos em posição específica: insert()
singular.insert(1,'tu')

print(singular)

# remover elementos da lista
# apagar por valor: remove()
singular.remove('ele')  
# Remove a primeira ocorrência do valor especificado
# Pode ser utilizado com variaveis

# apagar por índice: del
del singular[1]
print(singular)

# retirar elementos da lista: pop()
# Retira o último elemento da lista e permite a sua atribuição a uma variável
ultimo=singular.pop()
print(f"último elemento retirado: {ultimo}")
print(singular)

# pop também pode retirar um elemento em posição específica, indicando-se o índice
singular.append('eu')
singular.append('tu')
singular.append('ele')

segundo=singular.pop(1)
print(f"elemento retirado: {segundo}")
print(singular)

# percorrer os elementos da lista: ciclo FOR
for pessoa in pessoas:
    print(pessoa)
# ATENÇÃO À IDENTAÇÃO    
# o ciclo de iteração tanto dá para saída para ecrã como para código complexo a ser executado para cada elemento

# funções especiais:
# 1. ordenar uma lista: sort()
pessoas.sort()
# A ordenação por sort() é permanente (altera a lista original)

# 2. converter lista para string com separador: join()
print("ordenado: "+",".join(pessoas))

# 3. Uma lista pode ser percorrida em ordem inversa
for p in reversed(pessoas):
    print(p)

# ou pesquisada a partir do final
print(f"última pessoa: {pessoas[-1]}")

# 4. encontrar a ordem de um elemento: index()
print(f"índice d'ele: {pessoas.index('ele')}")

# 5. obter o tamanho da lista: len()
print(f"número de pessoas na lista: {len(pessoas)}")