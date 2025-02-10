# Listas 
#=========================================================================================#

#Listas 
# --> Arrays, Vetores, Matrizes. 
# --> São variáveis que conseguem guardar uma quantidade muito grande de informações, porém não de forma organizada
#-----------------------------------------------------------------------------------------#

lista_dos_sonhos = ['Pizza de 8 sabores', 'Morar na Suiça', 'Pastel de 32 sabores', 'Pizza de Tanajura', 12, 3.78, True, False, 'Douglas elogiando o Pyhton', 'Cris aprendendo Python!!!']

print(lista_dos_sonhos)
print(lista_dos_sonhos[1])


#-----------------------------------------------------------------------------------------#
# Indexação Negativa: Invés de mostra o primeiro elemento ele mostra o úlyimo elemento

print(lista_dos_sonhos[-1])

#-----------------------------------------------------------------------------------------#
# Tipo de dado da var
print(type(lista_dos_sonhos))

#-----------------------------------------------------------------------------------------#
# Quantidade total das informações
print(len(lista_dos_sonhos))

#=========================================================================================#
#Manipular esse lista, métodos de listas
#=========================================================================================#

#------------------------------------------------------------------------------------------

#1) insert -> adiciona uma informação especifica, na posição que nós quisermos
#                        inicio da posição , "o que quer colocar nessa posição"
lista_dos_sonhos.insert(0, "Thamyres vai patrocina nossa aposentadoria")
lista_dos_sonhos.insert(3, "Tomar café")

print(lista_dos_sonhos)

#------------------------------------------------------------------------------------------
#2) append -> adicionar uma informação ao final da nossa lista

lista_dos_sonhos.append("Ser poliglota")

print(lista_dos_sonhos)

#------------------------------------------------------------------------------------------
# 3) sort - Ordena a nossa lista em ordem alfanúmerica de forma crescente ou descrescente

nomes = ['Joaquim', 'Fernanda', 'Douglas', 'Vinicius', 'Leonardo', 'Argel', 'Enzo', 'Marlon', 'Grazi', 'Emanuelle', 'Natalia', 'Bernardo']

#antes
print(nomes)

#usando o sort
nomes.sort()
print(nomes)

nomes.sort(reverse=True)
print(nomes)

numeros = [1000, 345, 126, 579, 2, 20, 34, 67, 1]

numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)

#------------------------------------------------------------------------------------------
# 4) Remove

# OBS: Não funciona pelo index tem que ser número que está na lista
numeros.remove(1)
print(numeros)

#------------------------------------------------------------------------------------------

# 5) pop --> remove a informação da nossa lista a partir do índice que informamos

print(numeros)

numeros.pop(0)
print(numeros)

