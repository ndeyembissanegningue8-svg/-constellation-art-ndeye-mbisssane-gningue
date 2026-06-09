import turtle


turtle.bgcolor("black")
turtle.speed(1)
turtle.color("white")

etoiles = [(0, 0), (50, 50), (100, 0), (50, -50)]

# Dessiner les étoiles
for x, y in etoiles:
    turtle.penup()          
    turtle.goto(x, y)       
    turtle.dot(10)         


turtle.penup()
turtle.goto(etoiles[0])
turtle.pendown()

for x,y in etoiles[1:]:
    turtle.goto(x,y)


turtle.goto(etoiles[0])

turtle.done()