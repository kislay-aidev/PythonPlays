import turtle
import time

# Setup screen
screen = turtle.Screen()
screen.title("⏱ Modern Stopwatch")
screen.bgcolor("#1a1a1a")
screen.setup(width=600, height=400)

# Setup turtle
display = turtle.Turtle()
display.hideturtle()
display.speed(0)
display.pensize(2)

# State variables
seconds = 0
minutes = 0
hours = 0
running = False

def draw_frame():
    display.clear()
    display.penup()
    display.goto(0, 60)
    display.color("white")
    display.write("⏱ MODERN STOPWATCH", align="center", font=("Helvetica", 16, "bold"))

    # Draw rounded rectangle for glass effect
    display.goto(-120, -20)
    display.pendown()
    display.fillcolor("#ffffff")  # Pure white
    display.begin_fill()
    display.circle(20, 90)
    display.fd(240)
    display.circle(20, 90)
    display.fd(80)
    display.circle(20, 90)
    display.fd(240)
    display.circle(20, 90)
    display.fd(80)
    display.end_fill()
    display.penup()

def update_time():
    display.goto(0, -10)
    display.color("white")
    timer = f"{hours:02}:{minutes:02}:{seconds:02}"
    display.write(timer, align="center", font=("Courier", 28, "bold"))

def start():
    global running
    running = True
    run_timer()

def pause():
    global running
    running = False

def reset():
    global seconds, minutes, hours, running
    running = False
    seconds = minutes = hours = 0
    draw_frame()
    update_time()

def run_timer():
    global seconds, minutes, hours
    if running:
        time.sleep(1)
        seconds += 1
        if seconds >= 60:
            seconds = 0
            minutes += 1
        if minutes >= 60:
            minutes = 0
            hours += 1
        draw_frame()
        update_time()
        screen.ontimer(run_timer, 100)  # smoother update

# Button setup
def draw_button(x, y, label, command):
    button = turtle.Turtle()
    button.hideturtle()
    button.penup()
    button.goto(x, y)
    button.color("white")
    button.write(label, align="center", font=("Arial", 12, "bold"))
    screen.onclick(lambda tx, ty: command() if abs(tx - x) < 40 and abs(ty - y) < 20 else None)

# Layout and buttons
draw_frame()
update_time()
draw_button(-150, -130, "▶ START", start)
draw_button(0, -130, "⏸ PAUSE", pause)
draw_button(150, -130, "🔁 RESET", reset)

turtle.mainloop()