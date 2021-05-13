import turtle

class SpecialTurtle(turtle.Turtle):

    def __init__(self):
        turtle.Turtle.__init__(self)
        # the getscreen() method returns the Screen object that
        #    the turtle lives in
        self.amount_forward = 1
        self.turn_amount = 90
        self.getscreen().onkey(self.stop,'s')
        self.getscreen().onkey(self.close, 'q')
        self.getscreen().onkey(self.up, 'Up')
        self.getscreen().onkey(self.down, 'Down')
        self.getscreen().onkey(self.turn_right, 'Right')
        self.getscreen().onkey(self.turn_left, 'Left')
        self.getscreen().onkey(self.turn_more, 'q')
        self.getscreen().onkey(self.turn_less, 'a')
        
        
        self.goforward()


    def goforward(self):
        self.forward(self.amount_forward)
        self.getscreen().ontimer(self.goforward,40)

    def stop(self):
        self.amount_forward = 0
    def up(self):
        self.amount_forward += .25
    def down(self):
        self.amount_forward -= .25
    def turn_right(self):
        self.right(self.turn_amount)
    def turn_left(self):
        self.left(self.turn_amount)
    def close(self):
        self.getscreen().bye()
    def turn_more(self):
        self.turn_amount += 15
    def turn_less(self):
        self.turn_amount -= 15

wn = turtle.Screen()
st = SpecialTurtle()
wn.listen()
wn.mainloop()
