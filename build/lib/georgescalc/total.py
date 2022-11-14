def total_sum (*args: float)-> float:
    """Retorna a soma total dos argumentos."""
    total=0
    for n in args:
        total+=n
    return total

def total_product (*args:float)-> float:
    """Retorna o produto total dos argumentos."""
    total=1
    for n in args:
        total*=n
    return total
