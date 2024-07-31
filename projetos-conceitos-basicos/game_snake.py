import random
import time
import turtle

# Configuração da tela
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("Green")
wn.setup(width=600, height=600)
wn.tracer(0)

# Cabeça da cobra
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0)
head.direction = "stop" 

# Comida da cobra
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Funções de movimentação
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Liga as funções de movimentação às teclas
wn.listen()
wn.onkey(go_up, "Up")
wn.onkey(go_down, "Down")
wn.onkey(go_left, "Left")
wn.onkey(go_right, "Right")

# Loop principal do jogo
while True:
    wn.update()

    # Verifica se houve colisão com a borda
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Esconde os segmentos do corpo
        for segment in segments:
            segment.goto(1000, 1000)

        # Limpa a lista de segmentos
        segments.clear()

    # Verifica se houve colisão com a comida
    if head.distance(food) < 20:
        # Move a comida para um local aleatório
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # Adiciona um novo segmento ao corpo
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # Move os segmentos do corpo
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move o segmento 0 para onde a cabeça está
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Verifica colisões com o próprio corpo
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Esconde os segmentos do corpo
            for segment in segments:
                segment.goto(1000, 1000)

            # Limpa a lista de segmentos
            segments.clear()

    time.sleep(0.5)

wn.mainloop()
