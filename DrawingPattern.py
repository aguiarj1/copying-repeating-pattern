import turtle
import math

wn = turtle.Screen()
alex = turtle.Turtle()
alex.speed(0)
alex.pu()
alex.setx(-300.0)
alex.sety(300.0)
turtle.tracer(0.0)

def pattern(size, color1,color2):
    '''draws 4 columns of the specified size, 
    color1, color2. This function completes the pattern'''
    for i in range(2):
        colm(size,color1,color2)
        gobackup(size)
        colm(size,color2,color1)
        gobackup(size)

def gobackup(size):
    '''places the turtle on the top right corner 
    of the previous column to start a new column ''' 
    alex.left(90)
    alex.forward(72*size)
    alex.right(90)
    alex.forward(18*size)



def colm(size,color1,color2):
    '''draws one colmun wich is 4 sixrowpattern
    stacked on top of each other '''
    for i in range(2):
        for i in range(3):
            sixrowspattern(size,color1,color2)
        for i in range(3):
            sixrowspattern(size,color2,color1)

def sixrowspattern(size,color1,color2):
    '''draws the pattern of 6x6 square using the 
    size, color1, color2 parameters '''
    for i in range(3):
        row1pattern(size, color1,color2)
    startnewline(size)
    for i in range(3): 
        row2pattern(size, color1, color2)
    startnewline(size)
    for i in range(3):
        row3pattern(size,color1,color2)
    startnewline(size)
    for i in range(3):
        row4pattern(size,color1,color2)
    startnewline(size)
    for i in range(3):
        row5pattern(size,color1,color2)
    startnewline(size)
    for i in range(3):
        row6pattern(size,color1,color2)
    startnewline(size)

def startnewline(size):
    '''starts a new line and takes the input
    of the size of one square'''
    alex.left(180)
    alex.forward(size * 18)
    alex.left(90)
    alex.forward(size)
    alex.left(90)



def row1pattern(size, color1,color2):    
    '''draws the pattern on row 1 with the specified size, color1 and color2'''
    square(size,color1)
    squaresplit(size,color1, color2, 1)
    squaresplit(size,color2,color1, 1)
    squaresplit(size,color2,color1, 2)
    squaresplit(size,color1,color2, 2)
    square(size,color1)

def row2pattern(size,color1,color2):
    '''draws the pattern on row 2 with the specified size, color1 and color2'''
    squaresplit(size,color1, color2, 1)
    square(size,color1)
    squaresplit(size,color1, color2, 1)
    squaresplit(size,color1,color2, 2)
    square(size,color1)
    squaresplit(size,color1,color2, 2)

def row3pattern(size,color1,color2):
    '''draws the pattern on row 3 with the specified size, color1 and color2'''
    squaresplit(size,color2,color1, 1)
    squaresplit(size,color1,color2, 1)
    square(size,color2)
    square(size,color2)
    squaresplit(size,color1,color2, 2)
    squaresplit(size,color2,color1, 2)

def row4pattern(size,color1,color2):
    '''draws the pattern on row 4 with the specified size, color1 and color2'''
    squaresplit(size,color1,color2, 2)
    squaresplit(size,color2,color1, 2)
    square(size,color2)
    square(size,color2)
    squaresplit(size,color2,color1, 1)
    squaresplit(size,color1,color2, 1)

def row5pattern(size,color1,color2):
    '''draws the pattern on row 5 with the specified size, color1 and color2'''
    squaresplit(size,color2,color1, 2)
    square(size, color1)
    squaresplit(size,color2,color1, 2)
    squaresplit(size,color2,color1, 1)
    square(size, color1)
    squaresplit(size,color2,color1, 1)

def row6pattern(size,color1,color2):
    '''draws the pattern on row 6 with the specified size, color1 and color2'''
    square(size, color1)
    squaresplit(size,color2,color1,2)
    squaresplit(size,color1,color2,2)
    squaresplit(size,color1,color2,1)
    squaresplit(size,color2,color1,1)
    square(size,color1)

def square(size, fillcolor):
    '''draws a square of with the size and fillcolor specified '''
    alex.pd()
    alex.color(fillcolor)
    alex.begin_fill()
    for i in range(4):
        alex.forward(size)
        alex.right(90)
    alex.end_fill()
    alex.pu()
    alex.forward(size)


def squaresplit(size,color1,color2, version):
    '''draws a square split in the middle with two colors on each side, color1, color2. 
    one version (if you use 1 as the parameter) is split from the bottom left corner to 
    the top right corner and the other one (if you put any othe number) is split from 
    the top left corner to the bottom right corner'''
    alex.pd()
    if (version == 1):
        alex.right(90)
        alex.forward(size)
        alex.left(180)
    triangle(size, color1)
    alex.right(90+45)
    alex.forward(size)
    alex.right(90)
    alex.forward(size)
    alex.right(90)
    triangle(size, color2)
    alex.pu()
    if (version == 1):
        alex.right(45)
    else:
        alex.left(90+45)
        alex.forward(size)
        alex.right(90)


def triangle(size, color):
    '''draws a right angle triangle of size
    'size' and filled with the color 'color' '''
    alex.color(color)
    alex.begin_fill()
    alex.forward(size)
    alex.right(90)
    alex.forward(size)
    alex.right(90+45)
    alex.forward(pythagorean(size))
    alex.end_fill()


def pythagorean(side):
    '''given the size of the length of a right 
    triangle it will return the size of the hypotenuse'''
    return math.sqrt(side**2  + side**2)

pattern(8, "blue", "yellow")
#squaresplit(100, "blue","yellow", 2)
#triangle(100, "blue")
#row1pattern(100,"blue","yellow")
#colm(8,"blue","yellow")
wn.mainloop()


