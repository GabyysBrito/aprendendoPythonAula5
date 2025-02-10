# Um mini projeto na aula

cadastro = []

qntd_pessoas = int(input("Quantas pessoas deseja cadastrar: "))
index = 0

while len(cadastro) < qntd_pessoas:
    cadastro.append(input(f'Digite o {index + 1}° nome: '))
    index+=1

print:(f'As pessoas cadastradas foram: {cadastro}')
