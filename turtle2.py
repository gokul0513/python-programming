import turtle
turtle.setup(800,600)
window=turtle.Screen()
window.title('absolute positioning')
the_turtle=turtle.getturtle()
turtle.hideturtle()
the_turtle.setposition(100,0)
the_turtle.setposition(100,100)
the_turtle.setposition(0,100)
the_turtle.setposition(0,0)

turtle.exitonclick()

