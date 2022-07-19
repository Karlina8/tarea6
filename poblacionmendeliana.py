import scipy # es un package que ayudara a ejecutar las funciones dadas

def creando_poblacion(N, p):
    """ 
    Creo una poblacion de N=500 con una probabilidad de p=0.22, esta funcion me permite ver la probabilidad 
    de los alelos "A" o "a" al azar de la poblacion y devolver una poblacion completa. 
    """
    poblacion = []
    for i in range(N):
        allele1 = "A"
        if scipy.random.rand() > p:
            allele1 = "a"
        allele2 = "A"
        if scipy.random.rand() > p:
            allele2 = "a"
        poblacion.append((allele1, allele2))
    return poblacion

def frecuencias_geno(poblacion):
    """ 
    Esta funcion me permite onbservar las frecuencias genotipicas haciendo un conteo de cada para de alelo.
    """
    AA = poblacion.count(("A", "A"))
    Aa = poblacion.count(("A", "a"))
    aA = poblacion.count(("a", "A"))
    aa = poblacion.count(("a", "a"))
    return({"AA": AA, "aa": aa, "Aa": Aa, "aA": aA})    

def reproduccion_pobla(poblacion):
    """
    Esta funcion me permite observar la reproduccion de la poblacion inicial obteniendo la siguiente generacion 
    para consiguiente tomar a esta nueva generacion como mi poblacion actual y obtener la siguiente generacion 
    y asi sucesivamente.
    """
    new_generation = []
    N = len(poblacion)
    for i in range(N):
        # La integracion se hara de 1 hasta N-1
        dad = scipy.random.randint(N)
        mom = scipy.random.randint(N)
        # Desde los cromosomas de mama
        chr_mom = scipy.random.randint(2)
        offspring = (poblacion[mom][chr_mom], poblacion[dad][1 - chr_mom])
        #if offspring == ("a", "a"): 
        #next()
        new_generation.append(offspring)
    return new_generation