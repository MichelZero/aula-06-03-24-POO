# 10. Crie uma função que receba uma lista de números e 
# retorne uma nova lista apenas
# com os números pares.

def parImpar(lista, t):
    """
    Retorna uma lista apenas com os números pares.

    Argumentos:
        lista: Lista de números.

    Retorno:
        Lista apenas com os números pares.
    """
    """     L1 = []
        for n in lista:
            if n % 2 == 0:
                L1.append(n)
        return L1 """
    
    if (t == 'P' or t =='p'):
        L1 = []
        for n in lista:
            if n % 2 == 0:
                L1.append(n)
        return L1
    else:
        L2 = []
        for n in lista:
            if n % 2 != 0:
                L2.append(n)
        return L2
    

# Teste da função
L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tipo = 'P'
print(parImpar(L, tipo)) # [2, 4, 6, 8, 10]
