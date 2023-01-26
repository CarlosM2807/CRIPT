def codificacionHuffman(alf,prob):
    codif = crearDicc(alf)
    dep = crearDicc(alf)
    while(1 not in prob):
        min1, min2, indice1, indice2,dep = obtenerMenores(alf,prob,dep)
        #print("Cogemos --> ", alf[indice2],alf[indice1])
        #print(dep)
        dep2 = (dep.get(alf[indice1])).split()
        #print(dep2)
        if(len(dep2) == 0):
            if(min2 > min1):
                codif[alf[indice2]] = "0" + codif.get(alf[indice2])
                codif[alf[indice1]] = "1" + codif.get(alf[indice1])
        else:
            if(min2 > min1):
                for i in range(len(dep2)):
                    if(i < len(dep2)-1):
                        codif[dep2[i]] = "1" + codif.get(dep2[i])
                    else:
                        codif[dep2[i]] = "0" + codif.get(dep2[i])
                        cou = i
                        #print(cou)
                        #print("Print fumador:",dep.get(alf[cou-1]))
                        if(dep.get(alf[cou-1]) != ""):
                            dep3 = (dep.get(alf[cou-1])).split()
                            #print("XDDDDD", dep3)
                            for k in range(len(dep3)):
                                if(k == 0):
                                    continue
                                else:
                                    codif[dep3[k]] = "0" + codif.get(dep3[k])
                                    
    return codif

# Obtenemos las dos probabilidades menores del array de probabilidades
# puesto que luego formamos un subarbol con ellas, una la eliminamos y actualizamos valor con la suma
def obtenerMenores(alf,probabilidad,dep):
    min1 = 1
    min2 = 1
    indice = 0

    m = 0
    #print(probabilidad)
    for i in range(len(probabilidad)):
        if(probabilidad[i] < min1):
            min1 = probabilidad[i]
            indice = i
    for k in range(len(probabilidad)):
        if(probabilidad[k] < min2 and k != indice):
            min2 = probabilidad[k]
            m = k
    # Introduce el valor nuevo de la prob en la casilla de indice mas bajo y elimina la de indice mas alto
    # evitamos asi problemas con el limite del array
    
    if(indice > m):
        probabilidad[m] = min1 + min2
        probabilidad[indice] = 700
    else:
        probabilidad[indice] = min1 + min2
        probabilidad[m] = 700
    
    # Almacena las dependencias
    #print("Lo que mira: ",dep.get(alf[indice]))
    #print(m)
    if(dep.get(alf[indice]) == ""):
        if(m < indice):
            dep[alf[m]] = alf[m] + " " + alf[indice]
        else:
            dep[alf[indice]] =alf[indice] + " " + alf[m]
    else:
        #print("Indices m: ",m," y indice: ",indice)
        #print("El indice m es: ", alf[m], " y el indice indice es: ", alf[indice])
        if(m < indice):
            dep[alf[m]] = dep[alf[m]] + " " + alf[indice]
        else:
            dep[alf[indice]] = dep[alf[indice]] + " " + alf[m]

    return min1,min2,indice,m,dep

    # Creamos el diccionario que va a contener la codificación

def crearDicc(alf):
    d = {}
    for i in range(len(alf)):
        d[alf[i]] = ""
    return d

alfabeto = ["a","b","c","d","e","f"]
probabilidad = [0.1,0.2,0.15,0.34,0.12,0.09]
codificacionHuffman(alfabeto,probabilidad)