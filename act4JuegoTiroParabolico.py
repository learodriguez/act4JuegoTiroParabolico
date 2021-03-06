'''Herramientas Computacionales: El Arte de la Programación
Grupo: 201   TC1001S
Modified by:
        Léa Rodríguez Jouault A01659896   
        Mauricio Juárez Sánchez A01660336'''


from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):  # movimiento del proyectil dentro del espacio acordado
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 25
        speed.y = (y + 200) / 25

# límite del espacio en el que interactúan el proyectil y los balones
def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue') # tamaño de los balones

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')  # tamaño del proyectil

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150) # los balones aparecerán dentro de ese rango en y
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 3.5 # se puede cambiar la velocidad de los targets aquí

    if inside(ball):
        speed.y -= 0.5 #se puede cambiar la velocidad del proyectil aquí 
        ball.move(speed) 

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            # Se vuelve a generar nuevos targets, los que se pasan del límite desaparecen 
            target.x = 200 
            target.y = randrange(-150,150) 

    ontimer(move, 30) # de igual manera se puede modificar aquí

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
