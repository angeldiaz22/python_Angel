"""
Leer un numero entero positivo y calcular su Factorial. Ej

Fact(5) = 5 x 4 x 3 x 2 x 1

Fact(5) = 120
"""


factorial=1
print("Dijite el valor a factoriar")
numero=eval (input())
for i in range (1,numero+1):
    factorial=factorial*i
print(f"el factorial de {numero} es {factorial}")
