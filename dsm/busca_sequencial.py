##################################################################
#BUSCA SEQUENCIAL 
#
#PROCURA POR UM  VALOR DA LISTA DO PRIMEIRO ELEMENTO ATÉ O ULTIMO. RETORNA!
#RETORNA:
#a)A POSIÇÃO DO ELEMENTO CASO ELE EXISTA
#B)-1, CASO O VALOR NÃO EXISTIR
nums = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60]

"""
Função que implementa a busca sequencial
procura por uma val dentro da lista

"""
def busca_sequencial (val, lista):
    for pos in range(len(lista)):
        #se encontra coinscidencia, retorna pisoção
        if lista [pos] == val: return pos
    return -1 #nada encontrado

print(f'posição de 27: {busca_sequencial(27, nums)}')
print(f'posição de 40: {busca_sequencial(40, nums)}')
