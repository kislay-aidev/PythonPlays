import turtle
import random
import math

# Set up the game window
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Space Dodger - Survive the Asteroids!")
screen.setup(width=800, height=600)
screen.tracer(0)  # Turn off animation for smooth gameplay

# Game variables
score = 0
game_over = False
asteroids = []
stars = []
difficulty = 1

# Create player ship
player = turtle.Turtle()
player.shape("triangle")
player.color("cyan")
player.penup()
player.speed(0)
player.goto(0, -250)
player.setheading(90)  # Point upward

# Create score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-350, 250)

# Create game over display
game_over_display = turtle.Turtle()
game_over_display.speed(0)
game_over_display.color("red")
game_over_display.penup()
game_over_display.hideturtle()
game_over_display.goto(0, 0)

# Create background stars
def create_stars():
    for i in range(50):
        star = turtle.Turtle()
        star.shape("circle")
        star.color("white")
        star.penup()
        star.speed(0)
        star.goto(random.randint(-400, 400), random.randint(-300, 300))
        star.shapesize(0.2, 0.2)
        stars.append(star)

# Player movement functions
def move_left():
    x = player.xcor()
    if x > -350:
        player.setx(x - 20)

def move_right():
    x = player.xcor()
    if x < 350:
        player.setx(x + 20)

def move_up():
    y = player.ycor()
    if y < 250:
        player.sety(y + 20)

def move_down():
    y = player.ycor()
    if y > -250:
        player.sety(y - 20)

# Bind keys
screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")
screen.onkeypress(move_up, "w")
screen.onkeypress(move_down, "s")

# Create asteroid
def create_asteroid():
    asteroid = turtle.Turtle()
    asteroid.shape("circle")
    asteroid.color("orange")
    asteroid.penup()
    asteroid.speed(0)
    asteroid.goto(random.randint(-400, 400), 350)
    asteroid.shapesize(random.uniform(0.5, 2.0), random.uniform(0.5, 2.0))
    asteroid.dy = random.uniform(-3, -1) * difficulty
    asteroid.dx = random.uniform(-2, 2)
    asteroids.append(asteroid)

# Check collision
def is_collision(t1, t2):
    distance = math.sqrt((t1.xcor() - t2.xcor())**2 + (t1.ycor() - t2.ycor())**2)
    return distance < 20

# Update score display
def update_score():
    score_display.clear()
    score_display.write(f"Score: {score}  Difficulty: {difficulty}", 
                       align="left", font=("Arial", 16, "normal"))

# Create power-up
def create_power_up():
    if random.random() < 0.02:  # 2% chance per frame
        power_up = turtle.Turtle()
        power_up.shape("square")
        power_up.color("green")
        power_up.penup()
        power_up.speed(0)
        power_up.goto(random.randint(-400, 400), 350)
        power_up.shapesize(0.8, 0.8)
        power_up.dy = -2
        power_up.is_power_up = True
        asteroids.append(power_up)

# Game over function
def show_game_over():
    game_over_display.clear()
    game_over_display.write(f"GAME OVER!\nFinal Score: {score}\nPress R to restart", 
                           align="center", font=("Arial", 24, "bold"))

# Restart game
def restart_game():
    global score, game_over, difficulty
    score = 0
    game_over = False
    difficulty = 1
    player.goto(0, -250)
    
    # Clear asteroids
    for asteroid in asteroids:
        asteroid.hideturtle()
    asteroids.clear()
    
    # Clear displays
    game_over_display.clear()
    
    # Start game loop again
    game_loop()

screen.onkeypress(restart_game, "r")

# Create initial stars
create_stars()

# Main game loop
def game_loop():
    global score, game_over, difficulty
    
    if not game_over:
        # Move background stars
        for star in stars:
            y = star.ycor()
            star.sety(y - 1)
            if y < -300:
                star.goto(random.randint(-400, 400), 300)
        
        # Create new asteroids
        if random.random() < 0.1 + (difficulty * 0.05):
            create_asteroid()
        
        # Create power-ups occasionally
        create_power_up()
        
        # Move asteroids
        for asteroid in asteroids[:]:
            asteroid.sety(asteroid.ycor() + asteroid.dy)
            if hasattr(asteroid, 'dx'):
                asteroid.setx(asteroid.xcor() + asteroid.dx)
            
            # Remove asteroids that are off screen
            if asteroid.ycor() < -350:
                asteroid.hideturtle()
                asteroids.remove(asteroid)
                if not hasattr(asteroid, 'is_power_up'):
                    score += 10
            
            # Check collision with player
            if is_collision(player, asteroid):
                if hasattr(asteroid, 'is_power_up'):
                    # Power-up collected
                    score += 50
                    asteroid.hideturtle()
                    asteroids.remove(asteroid)
                    # Flash player green briefly
                    player.color("green")
                    screen.ontimer(lambda: player.color("cyan"), 200)
                else:
                    # Game over
                    game_over = True
                    show_game_over()
                    return
        
        # Increase difficulty over time
        if score > 0 and score % 200 == 0:
            difficulty = min(3, 1 + score // 200)
        
        # Update score
        update_score()
        
        # Continue game loop
        screen.ontimer(game_loop, 20)
    
    screen.update()

# Start the game
update_score()
game_loop()

# Keep the window open
screen.mainloop()