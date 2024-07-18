# #Funciones

# def mi_funcion():
#     return "Hola Mundo"

# import os
# os.system('cls'if os.name == 'nt' else 'clear')

# resultado =mi_funcion()

# print(resultado)

# #Funcion del factorial

# def factorial(n):
#     resultado =1
#     for i in range (1,n+1):
#         resultado *= i
#     return resultado

# n= int(input("Ingrese un numero: "))

# print(factorial(n))
import os
os.system('cls'if os.name == 'nt' else 'clear')

def funcion_1():
    a=1
    return a
def funcion_2(a):
    b=2+a
    return b
def funcion_3(a,b):
    c=3+a+b
    return c
def funcion_4(a,b,c):
    d=4+a+b+c
    return d

f1=funcion_1()
f2=funcion_2(f1)
f3=funcion_3(f2,f1)
f4=funcion_4(f3,f2,f1)

print(f4)