#########################################
# Desafio #5: Funcionários              #
# Codificado por: Marcelo C. Costa      #
# Data: 08/04/2020                      #
#########################################

import json

#Realiza a abertura e leitura do arquivo de entrada
with open ('Funcionarios-10K.json') as f:
    data = json.load(f)

##Fechando o arquivo de entrada
f.close()

##Abrindo o arquivo de entrada
arquivo_saida = open("saida-10k", "w")

#Cria uma lista de dicionários com os funcionários da empresa
funcionarios = data ["funcionarios"]

#Cria uma lista de dicionários com as áeras da empresa
areas = data ["areas"] 
    
#1.Quem mais recebe e quem menos recebe na empresa e a média salarial da empresa.

#Cria um dicionário com os dados da empresa
empresa = {'numero_de_funcionarios': 0, 'salario_total': 0, 'maior_salario': 0, 'menor_salario': 0, 'salario_medio': 0} 

#Ordena os funcionários por salário
funcionarios = sorted(funcionarios, key=lambda k: k['salario'])

#Descobrindo o maior salário da empresa:
empresa['maior_salario'] = funcionarios[-1]['salario']

#Imprimindo o(s) nome(s) do(s) funcionários com o(s) maior(es) salários da empresa
for i in funcionarios:
    if (i['salario'] == empresa['maior_salario']):
        arquivo_saida.write ('global_max|' + i['nome'] + ' ' + i['sobrenome'] + '|' + '{:.2f}'.format (i['salario']) + '\n') 
        
#Ordena os funcionários por salário
funcionarios = sorted(funcionarios, key=lambda k: k['salario'])

#Descobrindo o menor salário da empresa:
empresa['menor_salario'] = funcionarios[0]['salario']

#Imprimindo o(s) nome(s) do(s) funcionários com o(s) menor(es) salários da empresa
for i in funcionarios:
    if (i['salario'] == empresa['menor_salario']):
        arquivo_saida.write ('global_min|' + i['nome'] + ' ' + i['sobrenome'] + '|' + '{:.2f}'.format (i['salario']) + '\n')

#Descobrindo o número total de funcionários da empresa:
empresa['numero_de_funcionarios'] = len(funcionarios)

#Descobrindo o salário total da empresa:
for i in funcionarios:
    empresa['salario_total'] = empresa['salario_total'] + i['salario']

#Descobrindo o salário médio da empresa:
if (empresa['numero_de_funcionarios'] > 0):
    empresa['salario_medio'] = empresa['salario_total'] / empresa['numero_de_funcionarios']
else:
    empresa['salario_medio'] = 0

#Imprimindo o salário médio da empresa:
arquivo_saida.write ('global_avg|' + '{:.2f}'.format (empresa['salario_medio']) + '\n')


#2.Quem mais recebe e quem menos recebe em cada área e a média salarial em cada área.

#Acrescentando novas chaves aos dicionários de áreas, isso facilita o acesso aos dados.
#A chave 'id' apesar de não ser necessária nesse momento, pode ser útil no futuro, para
#guardar a ordem original de cada área.
#A chave 'ordem_relatorio' foi criada para que as areas possam ser ordenadas na mesma ordem
#em que aparecem no relatório de funcionários.
contador = 0
for i in areas:
    i['id'] = contador
    i['maior_salario'] = 0
    i['menor_salario'] = 0
    i['salario_medio'] = 0
    i['salario_total'] = 0
    i['quantidade_funcionarios'] = 0
    i['ordem_relatorio'] = 0
    contador = contador + 1

#Ordena os funcionários por id
funcionarios = sorted(funcionarios, key=lambda k: k['id'])

#Captura a ordem em que as áreas aparecem no relatório de funcionários.
contador = 1
for funcionario in funcionarios:
    for area in areas:
        if (area['ordem_relatorio'] == 0) and (area['codigo'] == funcionario['area']):
            area['ordem_relatorio'] = contador
            contador = contador + 1
            break

#Ordena as áreas pela 'ordem_relatório'
areas = sorted(areas, key=lambda k: k['ordem_relatorio'])            

#Laço que percorre área por área 
for i in areas:    
    #Cálculo do maior salário da área
    for j in funcionarios:
        if j['area'] == i['codigo'] and j['salario'] > i['maior_salario']:
            i['maior_salario'] = j['salario']

    #Impressão do(s) funcionário(s) que recebe(m) o maior salário da área
    for j in funcionarios:
        if j['area'] == i['codigo'] and j['salario'] == i['maior_salario']:
            arquivo_saida.write ('area_max|' + i['nome'] + '|' + j['nome'] + ' ' + j['sobrenome'] + '|' + '{:.2f}'.format (i['maior_salario']) + '\n')

    #Cálculo do menor salário da área
    i['menor_salario'] = i['maior_salario']
    for j in funcionarios:
        if j['area'] == i['codigo'] and j['salario'] < i['menor_salario']:
            i['menor_salario'] = j['salario']

    #Impressão do(s) funcionário(s) que recebe(m) o menor salário da área
    for j in funcionarios:
        if j['area'] == i['codigo'] and j['salario'] == i['menor_salario']:
            arquivo_saida.write ('area_min|' + i['nome'] + '|' + j['nome'] + ' ' + j['sobrenome'] + '|' + '{:.2f}'.format (i['menor_salario']) + '\n')

    #Cálculo da quantidade de funcionário e do salário total da área
    for j in funcionarios:
        if j['area'] == i['codigo']:
            i['quantidade_funcionarios'] = i['quantidade_funcionarios'] + 1
            i['salario_total'] = i['salario_total'] + j['salario']

    #Cálculo do salário médio da área
    if (i['quantidade_funcionarios'] != 0):
        i['salario_medio'] = i['salario_total'] / i['quantidade_funcionarios']
    else:
        i['salario_medio'] = 0
        
    #Impressão do salário médio da área
    arquivo_saida.write ('area_avg|' + i['nome'] + '|' + '{:.2f}'.format (i['salario_medio']) + '\n')


#3.Área(s) com o maior e menor número de funcionários.

#Ordena as áreas pela quantidade de funcionários
areas = sorted(areas, key = lambda k: k['quantidade_funcionarios'])

#Descobrindo a maior quantidade de funcionários em uma área:
maior_quantidade_funcionarios_area = areas[-1]['quantidade_funcionarios']

#Descobrindo a menor quantidade de funcionários em uma área:
menor_quantidade_funcionarios_area = areas[0]['quantidade_funcionarios']

#Impressão da(s) área(s) com maior número de funcionários
for i in areas:
    if i['quantidade_funcionarios'] == maior_quantidade_funcionarios_area:
        arquivo_saida.write ('most_employees|' + i['nome'] + '|' + '{}'.format (i['quantidade_funcionarios']) + '\n')

#Impressão da(s) área(s) com menor número de funcionários
for i in areas:
    if i['quantidade_funcionarios'] == menor_quantidade_funcionarios_area:
        arquivo_saida.write ('least_employees|' + i['nome'] + '|' + '{}'.format (i['quantidade_funcionarios']) + '\n')

#4. Maiores salários para funcionários com o mesmo sobrenome

#Lista que contém todos os sobrenomes dos funcionários.
sobrenomes = []

#Preenchendo a lista de sobrenomes.
for i in funcionarios:
    sobrenomes.append(i['sobrenome']) 

#Lista que contém apenas os sobrenomes repetidos.
sobrenomes_repetidos = []

#Ordena a lista de sobrenomes em ordem alfabética
sobrenomes.sort()

#Descobrindo os sobrenomes que se repetem.
tamanho_lista = len(sobrenomes)
i = 1
while i < tamanho_lista:
    if (sobrenomes[i] == sobrenomes[i-1]):
        sobrenomes_repetidos.append (sobrenomes[i])
    i = i + 1

#Agora, a lista 'sobrenomes_repetidos' está preenchida,
#no entanto, dentro dessa lista podem haver ítens que se
#repetem, por isso, devemos exclui-los.
sobrenomes_repetidos = list(dict.fromkeys(sobrenomes_repetidos))

#Aqui criamos a lista 'maior_salario_sobrenome' que recebe o
#maior salario por sobrenome
maior_salario_sobrenome = []
for i in sobrenomes_repetidos:
    maior_salario = 0
    for j in funcionarios:
        if (j['sobrenome'] == i and j['salario'] > maior_salario):
            maior_salario = j['salario']
    maior_salario_sobrenome.append(maior_salario)

#Agora que temos uma lista com os sobrenomes repetidos e outra
#com o maior salario por cada sobrenome repetido, vamos
#usá-las para criar um único dicionário, que possui as duas informaçoes
maior_salario_mesmo_sobrenome = []
i = 0
j = len(sobrenomes_repetidos)
while i < j:
    maior_salario_mesmo_sobrenome.append({'sobrenome': '', 'maior_salario': 0})
    maior_salario_mesmo_sobrenome[i]['sobrenome'] = sobrenomes_repetidos[i]
    maior_salario_mesmo_sobrenome[i]['maior_salario'] = maior_salario_sobrenome[i]
    i = i + 1

#Imprimindo os maiores salários para funcionários com o mesmo sobrenome
for i in maior_salario_mesmo_sobrenome:
    for j in funcionarios:
        if (j['sobrenome'] == i['sobrenome'] and j['salario'] == i['maior_salario']):
            arquivo_saida.write ('last_name_max|' + i['sobrenome'] + '|' + j['nome'] + ' ' + j['sobrenome'] + '|' + '{:.2f}'.format (j['salario']) + '\n')

##Fechando o arquivo de saída
arquivo_saida.close()























    






 












    


        










