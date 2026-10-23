"""
Tal como as listas, os Dicionários são coleções dinâmicas e não ordenadas de pares chave-valor.
Os dicionários têm um significado especial em programação porque armazenam valores juntamente com as suas chaves/variáveis correspondentes.
Isto permite simular um arquivo de dados sem recurso a um SGBD. Como veremos futuramente, este tipo de estrutura está particularmente
associado o um formato próprio de armazenamento de dados - JSON - amplamente utilizado para troca de informação entre sistemas.

Cada chave deve ser única num dicionárioe imutável, enquanto os valores podem ser de qualquer tipo.
Os dicionários são definidos por chaves {}, os pares chave-valor são separados por vírgulas e, dentro de cada par, a chave e o valor 
são separados por dois-pontos.
"""
# criar um dicionário (vazio)
dicionario_vazio = {}
print(dicionario_vazio)
print(type(dicionario_vazio).__name__)

# criar um dicionário com elementos
pessoa = {'nome': 'João', 'idade': 30, 'cidade': 'Lisboa'}
print(pessoa)
print(type(pessoa).__name__)

# aceder a elementos do dicionário por chave
print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']}")
print(f"Cidade: {pessoa['cidade']}")

# adicionar elementos ao dicionário
pessoa['profissao'] = 'Engenheiro'
print(pessoa)

# modificar elementos do dicionário
pessoa['idade'] = 31
print(pessoa)

# remover elementos do dicionário
del pessoa['profissao']
print(pessoa)

# retirar elementos do dicionário: pop()
idade = pessoa.pop('idade')
print(f"Idade removida: {idade}")
print(pessoa)

# verificar se uma chave existe no dicionário
if 'nome' in pessoa:
    print(f"Nome: {pessoa['nome']}")
else:
    print("Chave 'nome' não existe no dicionário")

# percorrer os elementos do dicionário: ciclo FOR (EACH)
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# obter todas as chaves do dicionário
print(f"Chaves: {list(pessoa.keys())}")

# obter todos os valores do dicionário
print(f"Valores: {list(pessoa.values())}")

# obter todos os pares chave-valor do dicionário
print(f"Pares chave-valor: {list(pessoa.items())}")

# Note-se que o resultado de cada uma das operações acima é uma lista, mesmo que o dicionário esteja vazio ou contenha apenas um elemento.
# não é coincidência...

# Pode-se simular uma tabela utilizando uma lista de dicionários
tabela = [
    {'nome': 'João', 'idade': 30, 'cidade': 'Lisboa'},
    {'nome': 'Maria', 'idade': 25, 'cidade': 'Porto'},
    {'nome': 'Pedro', 'idade': 35, 'cidade': 'Coimbra'}
]

# iterar sobre cada linha da tabela (lista de dicionários)
for linha in tabela:
    print(linha)
    # iterar sobre cada par chave-valor da linha (dicionário)
    for chave, valor in linha.items():
        print(f"  {chave}: {valor}")

# também se pode criar um dicionário a partir de listas de chaves e valores
chaves = ['nome', 'idade', 'cidade']
valores = ['Ana', 28, 'Funchal']
novo_dicionario = dict(zip(chaves, valores))
print(novo_dicionario)

# também se pode criar um dicionário a partir de uma lista de tuplos (pares chave-valor)
tuplos = [('nome', 'Carlos'), ('idade', 40), ('cidade', 'Braga')]
dicionario_tuplos = dict(tuplos)
print(dicionario_tuplos)

# Notar que a função dict() pode ser utilizada para criar um dicionário a partir de qualquer sequência de pares chave-valor, 
# como listas de tuplos ou listas de listas.

# um dicionário pode ter um lista como valor
dicionario_com_lista = {'nome': 'Lucas', 'hobbies': ['futebol', 'leitura', 'cinema']}
print(dicionario_com_lista)

# um dicionário pode ter outro dicionário como valor
dicionario_com_dicionario = {'nome': 'Lucas', 'endereco': {'rua': 'Rua A', 'cidade': 'Lisboa'}}
print(dicionario_com_dicionario)

# A complexidade pode crescer bastante... mesmo que apenas com listas, dicionários e estruturas afins
# Essa estrutura é nativa para o JSON e facilmente manipulável em Python, mesmo quando há a necessidade de persistência de dados
# Estas caracteristicas tornam os dicionários uma ferramenta poderosa para representar dados complexos de forma estruturada e flexível.
# Python e JSON têm grande e utilização precisamente por permitirem esta integração direta entre estruturas de dados complexas e programação de forma simples 
# e eficiente.