import turtle

#Stworzenie okna
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)

#Wynik
score_a = 0
score_b = 0

#Paletka A
paddle_a = turtle.Turtle()
paddle_a.speed("fastest")
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paletka B
paddle_b = turtle.Turtle()
paddle_b.speed("fastest")
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Piłka
ball = turtle.Turtle()
ball.speed("fastest")
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5

#Początkowy wynik
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("0 : 0", align="center", font=("Times New Roman", 32, "normal"))


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#main
while True:
    wn.update()   
    
    #Ruch piłki
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #Ściana 
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    
    #ściany za paletkami
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1    
        score_a += 1
        pen.clear()
        pen.write("{} : {}".format(score_a, score_b), align="center", font=("Times New Roman", 32, "normal"))

    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1        
        pen.clear()
        pen.write("{} : {}".format(score_a, score_b), align="center", font=("Times New Roman", 32, "normal"))
    
    #Spotkanie piłki z paletką
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
    
    elif (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1        