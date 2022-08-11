"""
Leer tres numeros (a, b, c). Y ordenelo en forma descendente,
es decir de mayor a menor. Favor controlar errores.
"""
try :
    a = int(input("Digite un primer numero =>") )
except :
    print("Porfavor ingrese un numero ... ! ") 
try :
    b = int(input("Digite un segundo numero =>") )
except :
    print("Porfavor ingrese un numero ... ! ")  
try :      
    c = int(input("Digite un tercer numero =>") )
except :
    print("porfavor ingrese un numero ... ! ")
mayor,intermedio, menor = 0,0,0


if a > b and a > c:
    mayor = a
    if b > c:
        intermedio=b
        menor =  c
    else:
           intermedio = c
           menor= b

if b > a and b > c:
    mayor = b
    if a > c:
          intermedio=a
          menor =  c
    else:
          intermedio=c 
          menor = a

if c > a and c > b:
    mayor = c
    if a > b:
          intermedio= a
          menor = b
    else:
        intermedio= b
        menor = a

print(f"El numero mayor es {mayor}, El intermedio es {intermedio}, y el menor es {menor}")

