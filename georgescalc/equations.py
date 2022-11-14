def delta (a:(int, float), b:(int, float), c:(int, float)) -> int,float:
    """
    Recebe: coeficientes a, b e c de uma equação de segundo grau
    Retorna: valor de delta.
    """
    return ((b**2) -4*a*c)


def bhaskara (a:(int, float), b:(int, float), c:(int, float)) -> int,float:
    """
    Recebe: coeficientes a, b e c de uma equação de segundo grau
    Retorna: os valores de x, ou None, se não houver raízes reais.
    """
    if delta(a,b,c) > 0:
        x1 = (-b + delta**(1/2))/(2*a)
        x2 = (-b - delta**(1/2))/(2*a)
        return([x1, x2])
    elif delta == 0: 
        return ((-b + delta**(1/2))/(2*a))
    else: 
        print('Não possui raízes reais')
        return (None)