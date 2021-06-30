
def preguntar(preguntas): 
    puntos = 0
    total_puntos = 0
    for pregunta in preguntas:
        total_puntos += 1
        ans = input(pregunta['q'] + ' ')
        ans = pregunta['parser'](ans)
        if pregunta['a'] == ans: puntos += 1


    if puntos == total_puntos:
        print(f'Excelente, Bien Hecho! Sacaste {puntos} de {total_puntos}')
    elif puntos == 0:
        print(f'Reprobaste: 0 de {total_puntos}')
    else:
        print(f'Sacaste {puntos} de {total_puntos}')