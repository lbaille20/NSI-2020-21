##import turtle
import jupyturtle_pkg as turtle

##screen = turtle.Screen()
##screen.setup(width=0.495, height=0.5, startx=-1.2, starty=0)

##print("Taille de l'écran :",screen.screensize())

##screen.tracer(None, 25)#définit la fréquence de rafraîchissement
"""default
>>> screen.tracer()
1
>>> screen.delay()
10
>>>
"""


def init():
    """
    - efface les tracés éventuels avec de précédentes tortues
    - cache d'éventuelles précédentes tortues
    """
    tinit=turtle.Turtle(1)
    tinit.hide_turtle()
    ##[t.clear() for t in turtle.turtles() if t != t0]
    ##[t.hideturtle() for t in turtle.turtles() if t != t0]
    ##trepere.clearscreen()

##fonction de tracé du repère
def trace_repere():
    global r_objects
    r_objects = []
    xmin, xmax = -200, 200
    ymin, ymax = -150, 150
    pas = 10
    trepere = turtle.Turtle()
    trepere.hide_turtle()
    trepere.penup()
    trepere.penstyle('dashed')
    trepere.pencolor('lightgrey')
    trepere.speed(0)
    for y in range(ymin+10, ymax + 1, pas):
        trepere.goto(xmin, y)
        trepere.pendown()
        trepere.goto(xmax, y)
        trepere.penup()
    for x in range(xmin+10, xmax + 1, pas):
        trepere.goto(x, ymin)
        trepere.pendown()
        trepere.goto(x, ymax)
        trepere.penup()
    r_objects.append(trepere)
    trepere = turtle.Turtle()
    trepere.penstyle('-')
    trepere.pencolor('black')
    trepere.penup()
    trepere.goto(xmin, 0)
    trepere.pendown()
    trepere.goto(xmax-5, 0)
    trepere.show_turtle()
    r_objects.append(trepere)
    trepere = turtle.Turtle()
    trepere.orient(90)
    trepere.penstyle('-')
    trepere.pencolor('black')
    trepere.penup()
    trepere.goto(0, ymin)
    trepere.pendown()
    trepere.goto(0, ymax-5)
    trepere.show_turtle()
    trepere.turtle_update()
    r_objects.append(trepere)
    trepere = turtle.Turtle()
    trepere.speed(0)
    offset = 10
    ticksize = 4
    for x in range(xmin, xmax + 1, 20):
        trepere.penup();trepere.goto(x, -ticksize/2);trepere.pendown();trepere.goto(x, +ticksize/2)
        trepere._ax.text(x, -offset, str(x), horizontalalignment='center', verticalalignment='center')
    offset = 5
    for y in range(ymin, ymax + 1, 20):
        trepere.penup();trepere.goto(-ticksize/2, y);trepere.pendown();trepere.goto(+ticksize/2, y)
        trepere._ax.text(-offset, y, str(y), horizontalalignment='right', verticalalignment='center')
    trepere.hide_turtle()
    r_objects.append(trepere)

def efface_repere():
    global r_objects
    pass

