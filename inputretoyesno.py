def string_parser(x):
    return str(x.lower())

def yes_no_parser(x):
    if x.lower() in ['n','no','0']:
        return 0
    if x.lower() in ['y','si','yes','1']:
        return 1
    return -1

preguntas = [
    # {
    #     'parser': int,
    #     'a': 1492,
    #     'q': '¿En que año Cristóbal Colón llegó a América?',
    # },
    # {
    #     'parser': int,
    #     'a': 1963,
    #     'q': '¿En qué año gobernó Juan Bosch?'
    # },
    # {
    #     'parser': string_parser,
    #     'a': 'juan pablo duarte',
    #     'q': '¿Quién es el padre de la Patria?'
    # },
    {
        'parser': yes_no_parser,
        'a': 1,
        'q': 'Omega esta preso por violencia?'
    },
]

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




