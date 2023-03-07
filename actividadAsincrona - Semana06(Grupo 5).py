print("")
print("Bienvenido ingeniero. Esta es la resolución de la actividad asincrona correspondiente a la semana 6")
print("")

print("---------------------------------------------------------------------------------------------------------------------")

print("Sumar 3 variables distintas y asignar el valor a una cuarta variable.")
print("")
suma1 = 8
suma2 = 5
suma3 = 2

suma = suma1 + suma2 + suma3

print(f"Suma: {suma1} + {suma2} + {suma3} = {suma}")
suma4 = 15
print(f"El resultado de la suma es: {suma4}")

print("---------------------------------------------------------------------------------------------------------------------")

print("Restar 4 variables siendo en la tercera variable más alta que la primera.")
print("")
resta1 = 3
resta2 = 9
resta3 = 6
resta4 = 10

resta = resta1 - resta2 - resta3 - resta4

print(f"Resta: {resta1} - {resta2} - {resta3} - {resta4} = {resta}")
resta5 = -22
print(f"El resultado de la resta es: {resta5}")

print("---------------------------------------------------------------------------------------------------------------------")

print("Multiplicar 2 variables asignarlas a otra variable y esa variable multiplicar por la segunda variable de suma y resta.")
print("")
multiplicacion1 = 9
multiplicacion2 = 5

primeraMultiplicacion = multiplicacion1 * multiplicacion2

print(f"Primera multiplicación: {multiplicacion1} * {multiplicacion2} = {primeraMultiplicacion}")
multiplicacion3 = 45
print(f"El resultado de la primera multiplicación es: {multiplicacion3}")

segundaMultiplicacion = multiplicacion3 * (suma2 * resta2)

print(f"Segunda multiplicación: {multiplicacion3} * {suma2} * {resta2} = {segundaMultiplicacion}")
multiplicacion4 = 2025
print(f"El resultado de la segunda multiplicación es: {multiplicacion4}")

print("---------------------------------------------------------------------------------------------------------------------")

print("Sacar a la primera variable de la multiplicación el exponente de la segunda variable de la multiplicación.")
print("")
exponente = multiplicacion1 ** multiplicacion2

print(f"Exponente: {multiplicacion1} ** {multiplicacion2} = {exponente}")
print(f"El resultado del exponente es: {exponente}")

print("---------------------------------------------------------------------------------------------------------------------")

print("Sacar el módulo de la primera variable de la suma con la primera variable de la resta.")
print("")
modulo = suma1 % resta1
 
print(f"Modulo: {suma1} % {resta1} = {modulo}")
print(f"El resultado del modulo es: {modulo}")

print("---------------------------------------------------------------------------------------------------------------------")

print("Dividir la variable resultado del exponente entre la variable resultado del módulo.")
print("")
divisionNormal = exponente / modulo

print(f"División normal: {exponente} / {modulo} = {divisionNormal}")
print(f"El resultado de la división normal es: {divisionNormal}")

print("---------------------------------------------------------------------------------------------------------------------")

print("Realizar la división entera de la división normal.")
print("")
divisionEntera = exponente // modulo

print(f"División normal: {divisionEntera}")
print(f"El resultado de la división entera de la división normal es: {divisionEntera}")

print("---------------------------------------------------------------------------------------------------------------------")
