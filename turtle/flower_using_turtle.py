import turtle
def draw_tri(turtle):
    for i in range(1,4):
        turtle.forward(100)
        turtle.right(120)
        
         
        
def draw_flower():
    window = turtle.Screen()
    window.bgcolor("red")
    flower = turtle.Turtle()
    for i in range(1,37):
        draw_tri(flower)
        flower.right(10)
        
        
        
    window.exitonclick()
        
    

draw_flower()    
    
