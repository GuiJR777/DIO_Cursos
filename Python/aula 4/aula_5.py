lista= [1,2,3,4,5,6]

print(sum(lista))#retorna a soma dos itens da lista
print(max(lista))#retorna o maior numero da lista
print(min(lista))#retorna o menor
print(len(lista))#retorna a quantidade de objetos na lista 

if 7 in lista: #Confere se o elemento existe na lista
    print('Existe um 7 nessa lista')
else:
     lista.append(7)#Adiciona a lista

print(lista)

if 1 in lista:
    lista.pop()#remove ultimo

print(lista)

lista.remove(3)

print(lista)

tupla=  (1,2,3,4,5)
conjunto= {1,2,3,4,5}
