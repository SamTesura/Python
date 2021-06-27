# Revisar si una condicion es mayor a
balance = 500
if balance > 0:
    print('Puedes pagar')
else:
    print('No tienes saldo')
    
 #Likes
likes = 200
if likes >= 200:
    print('Excelente, 200 Likes')
else:
        print('Casi llegas a 200')

#IF con texto
lenguaje = 'PHP'
if not lenguaje == 'Python':
    print('Excelente decision')

#Evaluar un Boolean
usario_autenticado = True

if usario_autenticado:
    print('Acceso al sistema')
else:
    print('Debes iniciar sesion')

#Evaluar un elemento de una lista
lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript', 'PHP']
if 'PHP' in lenguajes:
    print('PHP Si existe')
else:
    print('No, no esta en la lista')


#IF Anidadados
usario_autenticado = False
usuario_admin = False

if usario_autenticado:
    if usuario_admin:
        print('ACCESO TOTAL')
    else:
            print('Acceso al sistema')
else:
    print('Debes iniciar sesion')