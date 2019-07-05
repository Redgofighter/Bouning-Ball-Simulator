import turtle
import random

code = "https://github.com/Redgofighter/Bouning-Ball-Simulator"
tutorial = "https://www.youtube.com/watch?v=HHQV3ifJopo"
creater = "by Christian Thompson"
logger = False

print(code)
print(tutorial)
print(creater)

wn = turtle.Screen()
wn.tracer()
wn.bgcolor("black")
wn.title("Bouning Ball Simulator")
wn.tracer(10)

NoOfBalls = random.randint(10, 20)
print(NoOfBalls)

balls = []

for _ in range(NoOfBalls):
    balls.append(turtle.Turtle())

colors = ["red","green","blue","yellow","pink","orange","purple","white"]
shapes = ["circle","triangle","square","turtle"]

for ball in balls:    
    #ball = turtle.Turtle()
    ball.shape(random.choice(shapes))
    ball.color(random.choice(colors))
    ball.penup()
    ball.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(200, 400)
    ball.goto(x, y)
    ball.dy = random.randint(-1, 1)
    ball.dx = random.randint(-3, 3)
    ball.da = random.randint(-5, 5)

gravity = 0.1

while True:
    wn.update()

    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= gravity
        ball.sety(ball.ycor()+ball.dy)

        ball.setx(ball.xcor() + ball.dx)
        
        if(logger == True):
            logger = ("y info",ball.dy,"|",ball.ycor)
            print(logger)
            logger = ("x info",ball.dx,"|",ball.xcor)
            print(logger)
            
        if(ball.xcor() > 300):
            ball.dx *= -1
            ball.da *= -1

        if(ball.xcor() < -300):
            ball.dx *= -1
            ball.da *= -1
    
        if ball.ycor() <= -300:
            ball.sety(-300)
            ball.dy *= -1
            ball.da *= -1

