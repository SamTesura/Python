#Preguntas de Examen
pregunta1 = input('¿En que año Cristóbal Colón llegó a América? ')
pregunta2 = input('¿En qué año gobernó Juan Bosch? ')
pregunta3 = input('¿Quién es el padre de la Patria? ')
#Convertir Variables
pregunta1 = int(pregunta1)
pregunta2 = int(pregunta2)
pregunta3 = str(pregunta3)
#Empezar desde cero
puntos = 0
#Incrementar el puntaje dependiendo la respuesta
puntos += 1 if  pregunta1 == 1492 else 0
puntos += 1 if  pregunta2 == 1963 else 0
puntos += 1 if  pregunta3.lower() == 'juan pablo duarte' else 0

if  0 < puntos < 3: 
    print(f'Sacaste {puntos} de 3')
elif puntos == 3:
    print(f'Excelente, Bien Hecho! Sacaste {puntos} de 3')
else: 
    puntos = 0
    print('Reprobaste')