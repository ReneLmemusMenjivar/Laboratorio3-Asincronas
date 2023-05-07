
print(' -----------------------------------------------------------------------------------')
print(' |                       Bienvenido a nuestro programa                             |')
print(' -----------------------------------------------------------------------------------')

# Se definen los arrays de los departamentos y los municipios de cada uno.

departamentos = ['Chalatenango', 
                 'Sonsonate', 
                 'La Libertad', 
                 'La Unión', 
                 'San Salvador', 
                 'Usulután',
                 'Ahuachapán',
                 'Santa Ana',
                 'La Paz',
                 'Cabañas',
                 'San Miguel',
                 'Cuscatlán',
                 'San Vicente',
                 'Morazán']

municipios = [['Chalatenango', 'Agua Caliente', 'Arcatao', 'Azacualpa', 'Cancasque', 'Citalá', 'Comalapa', 'Concepción Quezaltepeque', 'Dulce Nombre de María', 'El Carrizal', 'El Paraíso', 'La Laguna', 'La Palma', 'La Reina', 'Las Flores', 'Las Vueltas', 'Nombre de Jesús', 'Nueva Concepción', 'Nueva Trinidad', 'Ojos de Agua', 'Potonico', 'San Antonio de la Cruz', 'San Antonio Los Ranchos', 'San Fernando', 'San Francisco Lempa', 'San Francisco Morazán', 'San Ignacio', 'San Isidro Labrador', 'San Luis del Carmen', 'San Miguel de Mercedes', 'San Rafael', 'Santa Rita', 'Tejutla'],
              ['Acajutla', 'Armenia', 'Caluco', 'Cuisnahuat', 'Izalco', 'Juayúa', 'Nahuizalco', 'Nahulingo', 'Salcoatitán', 'San Antonio del Monte', 'San Julián', 'Santa Catarina Masahuat', 'Santa Isabel Ishuatán', 'Santo Domingo de Guzmán', 'Sonsonate', 'Sonzacate'],
              ['Santa Tecla', 'Antiguo Cuscatlán', 'Chiltiupán', 'Ciudad Arce', 'Colón', 'Comasagua', 'Huizúcar', 'Jayaque', 'Jicalapa', 'La Libertad', 'Nuevo Cuscatlán', 'Opico', 'Quezaltepeque', 'Sacacoyo', 'San José Villanueva', 'San Juan Opico', 'San Matías', 'San Pablo Tacachico', 'Talnique', 'Tamanique', 'Teotepeque', 'Tepecoyo', 'Zaragoza'],
              ['La Unión', 'Anamorós', 'Bolívar', 'Concepción de Oriente', 'Conchagua', 'El Carmen', 'El Sauce', 'Intipucá', 'Lislique', 'Meanguera del Golfo', 'Nueva Esparta', 'Pasaquina', 'Polorós', 'San Alejo', 'San José', 'Santa Rosa de Lima', 'Yayantique', 'Yucuaiquín'],
              ['San Salvador', 'Aguilares', 'Ayutuxtepeque', 'Ciudad Delgado', 'Cuscatancingo', 'Guazapa', 'Nejapa', 'Ilopango', 'Rosario de Mora', 'San Marcos', 'San Martin', 'El Paisnal', 'Apopa', 'Mejicanos', 'Panchimalco', 'Santiago Texacuangos', 'Santo Tomás', 'Soyapango', 'Tonacatepeque'],
              ['Usulután', 'Alegría', 'Berlín', 'California', 'Concepción Batres', 'El Triunfo', 'Ereguayquín', 'Estanzuelas', 'Jiquilisco', 'Jucuapa', 'Jucuarán', 'Mercedes Umaña', 'Nueva Granada', 'Ozatlán', 'Puerto El Triunfo', 'San Agustín', 'San Buenaventura', 'San Dionisio', 'San Francisco Javier', 'Santa Elena', 'Santa María', 'Santiago de María', 'Tecapán'],
              ['Ahuachapán', 'Apaneca', 'Atiquizaya', 'Concepción de Ataco', 'Jujutla', 'Tacuba', 'Turín', 'San Lorenzo', 'El Refugio', 'Guaymango', 'San Pedro Puxtla', 'San Francisco Menéndez'],
              ['Santa Ana', 'Candelaria de la Frontera', 'El Porvenir', 'El Congo', 'Texistepeque', 'Chalchuapa', 'Coatepeque', 'Masahuat', 'Metapán', 'San Antonio Pajonal', 'San Sebastián Salitrillo','Santa Rosa Guachipilín', 'Santiago de la Frontera', 'Texistepeque'],
              ['Zacatecoluca', 'Cuyultitán', 'El Rosario', 'Jerusalén', 'Mercedes La Ceiba', 'Olocuilta', 'Paraíso de Osorio', 'San Antonio Masahuat', 'San Emigdio', 'San Francisco Chinameca', 'San Pedro Masahuat', 'San Juan Nonualco', 'San Juan Talpa', 'San Juan Tepezontes', 'San Luis La Herradura', 'San Luis Talpa', 'San Miguel Tepezontes', 'San Pedro Nonualco', 'San Rafael Obrajuelo', 'Santa María Ostuma', 'Santiago Nonualco', 'Tapalhuaca'],
              ['Sensuntepeque', 'Cinquera', 'Dolores', 'Guacotecti', 'Ilobasco', 'San Isidro', 'Victoria', 'Tejutepeque', 'Jutiapa'],
              ['San Miguel', 'Carolina', 'Chapeltique', 'Chinameca', 'Chirilagua', 'Ciudad Barrios', 'Comacarán', 'El Tránsito', 'Lolotique', 'Moncagua', 'Nueva Guadalupe', 'Nuevo Edén de San Juan', 'Quelepa', 'San Antonio', 'San Gerardo', 'San Jorge', 'San Luis de la Reina', 'San Rafael Oriente', 'Sesori', 'Uluazapa'],
              ['Cojutepeque', 'Candelaria', 'El Carmen', 'El Rosario', 'Monte San Juan', 'Oratorio de Concepción', 'San Bartolomé Perulapía', 'San Cristóbal','San José Guayabal', 'San Pedro Perulapán', 'San Rafael Cedros', 'San Ramón', 'Santa Cruz Analquito', 'Santa Cruz Michapa', 'Suchitoto', 'Tenancingo'],
              ['San Vicente', 'Apastepeque', 'San Cayetano istepeque', 'San Esteban Catarina', 'San Ildefonso', 'Tecoluca', 'Verapaz', 'Santo Domingo', 'Guadalupe', 'Santa Clara', 'San Lorenzo', 'San Sebastian', 'Tepetitán'],
              ['San Francisco Gotera', 'Arambala', 'Cacaopera', 'Chilanga', 'Corinto', 'Delicias de Concepción', 'El Divisadero', 'El Rosario', 'Gualococti', 'Guatajiagua', 'Joateca', 'Jocoaitique', 'Jocoro', 'Lolotiquillo', 'Meanguera', 'Osicala', 'Perquín', 'San Carlos', 'San Fernando', 'San Isidro', 'San Simón', 'Sensembra', 'Sociedad', 'Torola', 'Yamabal', 'Yoloaiquín']
             ]

# Se solicita crear un programa que se ejecute mediante una función, este deberá preguntar al usuario si quiere ejecutar el programa.
def ejecutar_programa():
    respuesta = input("\n¿Desea ejecutar el programa? (Si/No): ")
    
    # Si la respuesta es si, el programa inicia su ejecución.
    if respuesta.lower() == 'si':
        while True: 
            print("\nDepartamentos del país:")
            
            # Mediante un for se recorren los índices del arrays para luego mostrarlo como un menú, estos datos se mostrarán uno debajo del otro.
            for i in range(len(departamentos)):
                print(i + 1, "-", departamentos[i])
            
            # Se solicita al usuario ingresar el nombre de cualquier departamento, y este mostrará los municipios que le pertenecen.
            nombre = input("\nIngrese el nombre del departamento: ")
            intentos = 0
            while nombre not in departamentos and intentos < 3:
                intentos += 1
                print("\nNombre incorrecto. Por favor, inténtelo de nuevo.")
                nombre = input("\nIngrese el nombre del departamento: ")
            
            # Según el nombre ingresado, se recorrera el array para mostrar los municipios correspondientes:
            for i in range(len(departamentos)):
                if nombre == departamentos[i]:
                    print('Sus municipios son: ')
                    for municipio in municipios[i]:
                        print(municipio)
                    break
                
            else:
                print("\nDemasiados intentos fallidos. Volviendo al inicio...")
            
            # Se indica si desea ingresar otro departamento, si su respuesta es no, el programa finaliza.
            continuar = input("\n¿Desea consultar otro departamento? (Si/No): ")
            if continuar.lower() != 'si':
                break

    # Si la respuesta es no, el programa no se ejecuta.
    else:
        print("\nPrograma no ejecutado")

# Se hace el llamado a la función que ejecutará el programa.     
ejecutar_programa()

print('\nFin del programa')