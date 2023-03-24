import turtle
import random
import math
import pygame

pygame.mixer.init()
pygame.mixer.music.load("background.mp3")

block_size = 20
direction = "none"
screenx = 400
screeny = 400

lose = True

title = turtle.Turtle()
title.hideturtle()

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


def game_loop():
  global screen, direction, lose

  screen.ontimer(game_loop, 250)

  if lose:
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
  global pause, screen, lose, title
  lose = True
  title.hideturtle()
  title.write("Game Over", align='center', font=('Impact', 20, 'bold'))
  screen.update()
  clear_body()
  background_music()


def start_game():
  global lose, title, screen
  lose = False
  title.clear()
  screen.update()
  background_music()





def move_body():
  global snake
  for i in range(len(snake) - 1, 0, -1):
    snake[i].goto(snake[i - 1].xcor(), snake[i - 1].ycor())


def grow_snake():
  global snake, head
  body = turtle.Turtle()
  body.shape("square")
  body.color("#12c92b")
  body.speed(0)
  body.penup()
  body.goto(head.xcor(), head.ycor())
  snake.append(body)


def clear_body():
  global snake
  for body in snake[1:]:
    body.hideturtle()
  snake = [head]


def press_space():
  global lose
  if lose:
    start_game()





def background_music():
  global lose
  if lose:
    pygame.mixer.music.stop()
  if not lose:
    pygame.mixer.music.play()


def move_apple():
  global apple
  applex = random.randint(-200, 200)
  appley = random.randint(-200, 200)
  apple.goto(applex, appley)


def distance(x1, y1, x2, y2):
  return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def check_eat_apple():
  global head, apple
  return distance(head.pos()[0], head.pos()[1], apple.pos()[0], apple.pos()[1]) < block_size


screen = turtle.Screen()

apple = turtle.Turtle()
apple.shape("circle")
apple.color("red")
apple.speed(0)
apple.penup()
move_apple()

screen.ontimer(game_loop, 250)
screen.onkeypress(press_left, "Left")
screen.onkeypress(press_right, "Right")
screen.onkeypress(press_down, "Down")
screen.onkeypress(press_up, "Up")
screen.onkeypress(press_space, "space")

screen.listen()
screen.tracer(0)

screen.mainloop()
