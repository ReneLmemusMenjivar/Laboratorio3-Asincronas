integrantes = ['Oswaldo', 'Alondra', 'Rene', 'Jeremy', 'Norlin','Erick'  ]
nombres = ['Oswaldo', 'Alondra', 'Rene', 'Jeremy', 'Norlin', 'Erick']
apellidos = ['Monterroza', 'Lopez', 'Lemus', 'Segura', 'Moreno', 'Diaz']
sexo = ['M', 'F', 'M', 'M', 'M', 'M']
edades = [24, 29, 31, 27, 26]
departamentos = ['Chalatenango', 'Chalatenango', 'La libertad', 'Chalatenango', 'Chalatenango', 'Chalatenango']
municipios = ['Potonico', 'ojos de Agua', 'Quezaltepeque', '0', 'El Carrizal', '0']
direcciones = ['Barrio El Centro', 'canton El Zapotal', 'cantón Tacachico', '0', 'Bario El Centro', '0']

def ejecutar_programa():
    respuesta = input("¿Quieres ejecutar el programa? (Si/No): ")
    if respuesta.lower() == 'si':
        print("Integrantes del grupo:")
        for i in range(len(integrantes)):
            print(i+1, "-", integrantes[i])
        nombre = input("Ingresa el nombre de un integrante del grupo: ")
        intentos = 0
        while nombre not in nombres and intentos < 3:
            intentos += 1
            print("Nombre incorrecto. Por favor, inténtalo de nuevo.")
            nombre = input("Ingresa el nombre de un integrante del grupo: ")
        if nombre in nombres:
            indice = nombres.index(nombre)
            print("Nombre: ", nombres[indice])
            print("Apellido: ", apellidos[indice])
            print("Sexo: ", sexo[indice])
            print("Edad: ", edades[indice])
            print("Departamento: ", departamentos[indice])
            print("Municipio: ", municipios[indice])
            print("Dirección: ", direcciones[indice])
        else:
            print("Demasiados intentos fallidos. Volviendo al inicio...")
            ejecutar_programa()
    else:
        print("Programa no ejecutado.")
        
ejecutar_programa()
