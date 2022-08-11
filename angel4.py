
import os
import math


try:
                num = int(
                    input("Digita un numero para obtener la solucion de la serie: "))
                dato = 0
                os.system('cls')
                for i in range(0, num + 1):
                    dato += (math.pow(5, i) / math.factorial(i))
                print('Respuesta de la serie: ', dato)
except:
                print('Error dato invalido')