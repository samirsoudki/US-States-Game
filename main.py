import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. names")

writer = turtle.Turtle("turtle")
writer.penup()
writer.hideturtle()

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
df = pd.read_csv("50_states.csv")

states_list = df["state"].to_list()

guessed_states = 0
guessed_states_name = []

while True:
    answer = screen.textinput(title=f"{guessed_states}/ 50 Guess the States name", prompt="guess the state").title()
    for state in states_list:
        if state == answer and answer not in guessed_states_name:
            answer = state
            state_name = df[df.state == answer]
            writer.goto(int(state_name.x), int(state_name.y))
            writer.write(answer)
            guessed_states += 1
            guessed_states_name.append(answer)
            print(guessed_states_name)
            if len(states_list) == len(guessed_states_name):
                writer.write("you guessed all the states", font=("candara", 24, "bold"))







