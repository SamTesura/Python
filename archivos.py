def app():
    #Crear el archivo
    archivo = open('archivo.txt', 'w') # w es escritura, si no existe lo creará

    # Generar números en archivo
    for i in range(0, 20):
        archivo.write('Esta el la linea ' + str(i) + "\r" )

    # Cerrar el archivos
    archivo.close()


app()