import turtle
def draw_square(turtle):
    for i in range(1,5):
        turtle.forward(100)
        turtle.right(90)



def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
    brad = turtle.Turtle()
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)

    window.exitonclick()

draw_art()
 


    
