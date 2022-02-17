import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

# print(answer_state)
# user input a state, if it match the csv file, state name is added to the image. and state name is placed at the (x,
# y) coordinates according to the csv file
data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
coor_x_list = data.x.to_list()
coor_y_list = data.y.to_list()
# print(coor_x_list)

game_on = True
count = 0
while game_on:
    answer_state = (screen.textinput(title=f"{count}/50  Guess the State", prompt="What's another State's name?")).title()
    if answer_state == "Exit":
        break
    if answer_state in state_list:
        count += 1
        answer_state_index = state_list.index(answer_state)
        stata_x_coor = coor_x_list[answer_state_index]
        stata_y_coor = coor_y_list[answer_state_index]
        turtle_state = turtle.Turtle()
        turtle_state.hideturtle()
        turtle_state.penup()
        turtle_state.goto(stata_x_coor, stata_y_coor)
        turtle_state.write(answer_state, move=False, align='left', font=('Arial', 8, 'normal'))





# guess state window shows up again while game is on

# title of guess state window updates when a correct state is put in
