def limpiar(lista):
    return [x for x in lista if x is not None]

def escalar(lista):
    max_val = max(lista)
    return [x/max_val for x in lista]

def media(lista):
    return sum(lista)/len(lista)
