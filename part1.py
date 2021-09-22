#1.1 Bottles of beer

def bottles(number):
    for i in range(number):
        song = (number,"bottles of beer on the wall,", number , "bottles of beer")
        number = number - 1
        song_two = ("Take one down, pass it around,", number ,"bottles of beer on the wall")
        print(song)
        print(song_two)
        

#bottles(99)

#1.2 multiplication table
def table(n):
    for i in range(1,n + 1):
        for multiply in range(1,n + 1):
            times = (i*multiply)
            print(times, end = " ", sep = " ")
        print()

#table(5)

#1.3
def summation(N):
    answer = 0
    for i in range(1, N + 1):
        answer += (i**2)
    print(answer, end = " ", sep = " ")
#summation(5)

#2.1
#2.1.1 DrawSquare
import turtle
fran = turtle.Turtle()


def drawSquare(myTurtle, squareSize):
    for i in range(4):
        myTurtle.forward(squareSize)
        myTurtle.left(90)
#drawSquare(fran, 50)
        

#2.1.2 Drawing a row of squares
def drawRow(myTurtle, length, squareSize):
    for i in range(length):
        drawSquare(myTurtle, squareSize)
        myTurtle.forward(squareSize)
        
#drawRow(fran,5,50)
    
        

#2.1.3 Drawing a grid   
def drawGrid(myTurtle, size, squareSize):
    myTurtle.speed(10)
    for i in range(size):
        drawRow(myTurtle, size, squareSize)
        myTurtle.up()
        myTurtle.left(90)
        myTurtle.forward(squareSize)
        myTurtle.right(90)
        myTurtle.backward(squareSize * size)
        myTurtle.down()
#drawGrid(fran,5,50)
#2.1.4
def drawSquareStairs(myTurtle, height, squareSize):
    fran.speed(10)
    for i in range(height):
        drawRow(myTurtle, height, squareSize)
        myTurtle.up()
        myTurtle.left(90)
        myTurtle.forward(squareSize)
        myTurtle.right(90)
        myTurtle.backward(squareSize * height)
        myTurtle.down()
        height -= 1
#drawSquareStairs(fran,5,50)
#2.2 Spirals
#2.2.1 N Sided Polygon
def drawNgon(myTurtle, numSides, sideLength):
    for i in range(numSides):
        myTurtle.forward(sideLength)
        myTurtle.left(360//numSides)
#drawNgon(fran,6,100)
#2.2.2
def drawNgonSpiral(myTurtle, numSides, sideLength, numShapes):
    fran.speed(10)
    for i in range(numShapes):
        drawNgon(myTurtle, numSides, sideLength)
        myTurtle.left(360//numShapes)
#drawNgonSpiral(fran,6,50,50)

#Bonus
#3.1 Hourglass
def hourGlass():
    print(""'|""""""""""|'"")
    multiply = [5,4,3,2,1]
    for i in range(4,0,-1):
        top = print(multiply[i] * " ","\\",(i * "::"),"/",sep = "")
    print("     ||")
    for i in range(1,5):
        bottom = print(multiply[i] * " ","/",(i * "::"),"\\",sep = "")
    print(""'|""""""""""|'"")  
        
        
#hourGlass()
    

#3.3 Super Duper Spiral
import random
def drawNgonSpiral(myTurtle, numSides, sideLength, numShapes):
    fran.speed(10)
    for i in range(numShapes):
        drawNgon(myTurtle, numSides, sideLength)
        myTurtle.left(360//numShapes)
        myTurtle.color(random.random(),random.random(),random.random())

#drawNgonSpiral(fran,6,50,50)


















