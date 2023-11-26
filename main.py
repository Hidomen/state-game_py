import turtle
import pandas

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guessed_states = []
missed_states = []

while len(guessed_states) < 50:
    try:
        answer_state = screen.textinput(f"Guess the State {len(guessed_states)}/50", 
                                    "Guess another state's name")
    except AttributeError:
        break
    #
    if answer_state != "":
        answer_state = answer_state.title()
    else:
        break
    
    if answer_state in all_states and answer_state not in guessed_states: # and not guessed before
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state) # or state_data.state.item()
        guessed_states.append(answer_state)

    if answer_state == "Exit":
        missed_states = [state for state in all_states if state not in guessed_states]
        

        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("missed_states.csv")
        break
#

