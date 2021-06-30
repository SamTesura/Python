#Creando un dicciario simple
cancion = {
    'artista' : 'Metallica', #llave y valor
    'cancion' : 'Enter Sandman',
    'lanzamiento' : 1992,
    'likes' : 3000 
}

#Acceder a los elementos del diccionario
print(cancion['artista'])
print(cancion['lanzamiento'])

#Mezclar con un string
artista = cancion['artista']
print(f'Estoy escuchando a {artista}')

print(cancion)

#Agregar nuevos valores
cancion['playlist'] = 'Heavy Metal'
print(cancion)

#Reemplazar valor existente
cancion['playlist'] = 'Seek & Destroy'
print(cancion)

#Eliminar un valor
del cancion['lanzamiento']
print(cancion)
