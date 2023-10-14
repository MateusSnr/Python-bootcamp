import turtle
import pandas

IMAGE = "gif_map.gif"

screen = turtle.Screen()
screen.title("Brazil States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pandas.read_csv("states.csv")
states_list = data.state.to_list()
guessed_states_list = []

while len(guessed_states_list) < 26:
    answer_state = screen.textinput(title=f"{len(guessed_states_list)}/26 States Correct",
                                    prompt="What's another state's name ?")
    if answer_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_states_list:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Estados_a_serem_estudados.csv")
        break

    if answer_state in states_list:
        guessed_states_list.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

#def get_mouse_click_coor(x,y):
#   print(x,y )

#turtle.onscreenclick(get_mouse_click_coor)

#turtle.mainloop()


