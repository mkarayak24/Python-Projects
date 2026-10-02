import time
import turtle
import random

WIDTH, HEIGHT = 500, 500
COLORS = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan", "magenta"] 

def get_number_of_turtles():
    while True:
            num_turtles = input("Enter the number of turtles (2-10): ")
            if num_turtles.isdigit():
                num_turtles = int(num_turtles)
            else:
                print("Invalid input. Please enter a number.")
                continue
            if 2 <= num_turtles <= 10:
                return num_turtles
            else:
                print("Please enter a number between 2 and 10.")
                continue

def race(colors):
    turtles = create_turtles(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            _, y = racer.pos()
            if y >= HEIGHT//2 - 10:
                return colors[turtles.index(racer)]

def create_turtles(colors):
    turtles = []
    spacing = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacing, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
        
    return turtles

def init_turtle_race():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Race")
  
racers = get_number_of_turtles()
init_turtle_race()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print(f"The winner is the {winner} turtle!")
time.sleep(5)