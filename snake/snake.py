import turtle
import random
import math
block_size = 20
direction = "none"
screenx= 400
screeny= 400
pause = False

head = turtle.Turtle()
head.shape("square")
head.color("dark green")
head.speed(0)
head.penup()

snake = [head]

def press_left():
    global direction
    direction = "left"
def press_right():
    global direction
    direction = "right"
def press_down():
    global direction
    direction = "down"
def press_up():
    global direction
    direction = "up"

def move_snake():
    global screen,direction,pause

    screen.ontimer(move_snake, 250)
    
    if pause:
        return

    move_body()

    if direction == "left":
        head.setheading(180)
    elif direction == "right":
        head.setheading(0)
    elif direction == "up":
        head.setheading(90)
    elif direction == "down":
        head.setheading(270)

    if direction != "none":
       head.forward(block_size)
       if check_lose():
           game_over()

    if check_eat_apple():
        move_apple()
        grow_snake()

    screen.update()

def check_lose():
    global snake, head
    for body in snake[1:]:
        if head.xcor() == body.xcor() and head.ycor() == body.ycor():
            return True

    return False

def game_over():
    global pause, screen
    pause = True
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.write("Game Over", align = 'center', font = ('Impact', 20, 'bold'))
    screen.update()

def move_body():
    global snake
    for i in range(len(snake) - 1, 0, -1):
        snake[i].goto(snake[i-1].xcor(), snake[i-1].ycor())

def grow_snake():
    global snake, head
    body = turtle.Turtle()
    body.shape("square")
    body.color("#12c92b")
    body.speed(0)
    body.penup()
    body.goto(head.xcor(), head.ycor())
    snake.append(body)

def press_space():
    global pause
    pause = not pause
def move_apple():
    global apple
    applex =random.randint(-200, 200)
    appley =random.randint(-200, 200)
    apple.goto(applex, appley)
def distance(x1, y1 , x2 , y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
def check_eat_apple():
    global head, apple
    return distance(head.pos()[0], head.pos()[1],apple.pos()[0],apple.pos()[1]) < block_size


def spaceplay_game():
    playzone = turtle.Turtle()
    playzone.penup()
    playzone.pensize(10)
    playzone.goto(-300, 200)
    playzone.pendown()
    playzone.goto(300, 200)
    playzone.goto(300,-200)
    playzone.goto(-300,-200)
    playzone.goto(-300, 200)
    playzone.color("dark blue")
    playzone.hideturtle()
    check_lose
    game_over


screen = turtle.Screen()



apple = turtle.Turtle()
apple.shape("circle")
apple.color("red")
apple.speed(0)
apple.penup()
move_apple()

screen.ontimer(move_snake, 250)
screen.onkeypress(press_left,"Left")
screen.onkeypress(press_right,"Right")
screen.onkeypress(press_down,"Down")
screen.onkeypress(press_up,"Up")
screen.onkeypress(press_space, "space")

screen.listen()
screen.tracer(0)

screen.mainloop()