#Verifica se o elemento está na lista utilizando a busca binária
def buscaBinaria(lista, e): 
    x = 0 
    first = 0
    last = len(lista)-1
    found = False
    #Definindo os parâmetros da busca binária 
    while first<=last and not found:
        x+=1
        midpoint = (first + last)//2
        if lista[midpoint] == e:
            print("Elemento {} localizado".format(midpoint))
            return "Foram feitas {} tentativas para achar o valor".format(x) 
        else:
            if e < lista[midpoint]:
                last = midpoint-1
            else:     
                first = midpoint+1
    print("-1")
    
lista1 = []
n = int(input("Quantos elementos terá a lista?: ")) #Usuário diz o tamanho da lista, seja de 10, 50, 100, 500, 1000, 5000, 10.000, 50.000 ou 100.000

lista1 = list(range(0, n))
print(lista1)
    
e = int(input("Qual o item que deseja buscar na lista?: "))
print(buscaBinaria(lista1, e))
