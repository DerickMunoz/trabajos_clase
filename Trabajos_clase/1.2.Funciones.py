def devolver_distintos(a,b,c):
    suma=a+b+c
    if suma > 15:
        return max(a,b,c)
    elif suma < 10:
        return min(a,b,c)
    else:
        return (a+b+c) - min(a,b,c)-max(a,b,c) 
    
print(devolver_distintos(8,1,2))

#Funcion ordenar numeros

def ordena_valores(a,b,c):
    return sorted([a,b,c])

print(ordena_valores(8,1,2))