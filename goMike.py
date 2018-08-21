from turtle import Turtle
from turtle import Screen
import sys
sys.setExecutionLimit(65000)

class Mike(Turtle):
    firstname = 'Mike'
    def __init__(self, color, speed):
        Turtle.__init__(self) 
        self.shellcolor = color
        self.color(color)
        self.speed(speed)


    def drawAndBack(self, length, angle):
        for i in range(2):
            self.forward(length / 2)
            self.forward(-length)
            self.forward(length / 2)
            self.left(90)
        self.right(180)

    def drawSquare(self, length):
        # turtle is facing it's right, relative right
        self.forward(length/2)
        self.left(90)
        self.forward(length/2)
        for i in range(3):
            self.left(90)
            self.forward(length)
        self.left(90)
        self.forward(length/2)
        self.right(90)
        self.forward(-length/2)
        # should end up facing it's relative right

    def draw_line(self, length, angle):
        self.left(angle)
        self.drawAndBack(length, angle)
        self.drawSquare(length)
        

    def star(self, lines):
        print("Go " + self.firstname + "!!!")
        steps = int(180/lines)
        for angle in range(0, 180, steps):
            if angle == 0:
                self.draw_line(200, 0)
            else:
                compAngle = angle % steps + steps
                self.draw_line(200, compAngle)
            

def main():
    wn = Screen()
    wn.bgcolor("lightgreen")
    mike = Mike('blue', 5)

    mike.star(5)
    wn.exitonclick()
    
if __name__ == "__main__" :
    main()
    