import turtle
import random
import time

# Setup screen
screen = turtle.Screen()
screen.title("Catch the Turtle Game")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# Score tracker
score = 0
game_running = True

# Turtle to catch
catcher = turtle.Turtle()
catcher.shape("turtle")
catcher.color("green")
catcher.penup()
catcher.speed(0)

# Score display
score_writer = turtle.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(0, 260)
score_writer.write("Score: 0", align="center", font=("Arial", 16, "bold"))

# Function to update score
def update_score(x, y):
    global score
    if game_running:
        score += 1
        score_writer.clear()
        score_writer.write(f"Score: {score}", align="center", font=("Arial", 16, "bold"))
        move_turtle()

# Function to move turtle randomly
def move_turtle():
    x = random.randint(-280, 280)
    y = random.randint(-280, 250)
    catcher.goto(x, y)

# End game after time limit
def end_game():
    global game_running
    game_running = False
    catcher.hideturtle()
    score_writer.goto(0, 0)
    score_writer.write(f"Game Over!\nFinal Score: {score}", align="center", font=("Arial", 18, "bold"))

# Register click handler
catcher.onclick(update_score)

# Start game loop
move_turtle()
screen.ontimer(end_game, 20000)  # 20-second timer
screen.mainloop()