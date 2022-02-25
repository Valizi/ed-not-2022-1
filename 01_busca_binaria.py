def busca_binaria(lista, val):
    ini = 0 #inicio da lista
    fim = len(lista) - 1 # fim da lista
    while ini <= fim:   
        meio = (ini + fim) /2 #meio da lista

        #1 caso : o valor da posição do meio da lista 
        #corresponde ao valor buscado; Encontramos e 
        #E retornamos a posição encontrada (meio)
        if val == lista[meio]:
            return meio

        #2 caso, o valor de busca é maior que o valor
        # no meio da lista
        elif val > lista[meio]:
            ini = meio + 1


        #3 caso: O valor de busca é menor que o valor
        #do meio da lista
        else:
            ini = meio - 1