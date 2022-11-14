def fibonacci(n_termo: int)->int:
    """
    Recebe: quantidade de termos requeridos.
    Retorna: a lista os termos da sequência de fibonacci.
    """
    termo= 1
    termo2=1
    lista_termos=[]
    for i in range(1, n_termo+1):
        if i==1:
            lista_termos.append(termo)
        elif i==2:
            lista_termos.append(termo2)
        else:
            termo_n=termo+termo2
            lista_termos.append(termo_n)
            termo = termo2
            termo2 = termo_n

    return (lista_termos)
        
def fatorial (num: int)->int:
    """
    Recebe: Um número natural.
    Retorna: O fatorial do número.
    """
    fat=1
    if num<0:
        print('Valor inválido. O fatorial só é válido para números naturais')
    elif num==0 or num==1:
        return fat
    else:
        for i in range(1,num+1):
            fat*=i
        return fat