from turtle import Turtle, Screen
import random

Is_game_on = False

screen = Screen()
screen.setup(height=400, width=600)
user_bet = screen.textinput(title="Make your bet", 
                            prompt="Choose your color among these five color Red, Green, Yellow, pink,Purple")
Colors = ["Red", "Green", "Black", "Pink", "Purple"]
Y_position = [-60, -30, 0, 30, 60]
all_turtle = []

# /create 5 new turtle
for i in range(0,5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(Colors[i])
    new_turtle.goto(x=-280, y=Y_position[i])
    all_turtle.append(new_turtle)

if user_bet:
    Is_race_on = True

while Is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 280:
            Is_race_on = False
            if user_bet == turtle.pencolor():
                print(f"You've won! the {turtle.pencolor()} is the winner!")
            else:
                print(f"You've lost! the {turtle.pencolor()} is the winner!")
        # make each turtle a random movement
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()

