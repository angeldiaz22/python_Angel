
import math
try:
                n = int(input("Digita el valor de n: "))
                x = int(input("Digita el valor de x: "))

                sen = math.pow(-1, n) * (math.pow(x, 2*n+1) /
                                         math.factorial(2*n+1))
                cos = math.pow(-1, n) * (math.pow(x, 2*n) /
                                         math.factorial(2*n))

                print('SENO: ', sen)
                print('COSENO: ', cos)
except:
    print('Error dato invalido')
    