import turtle;
import pandas

screen = turtle.Screen()
screen.title('U.S state_game')
image = './blank_states_img.gif'

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
state_data_list = data['state'].to_list()
guess_stats = []

while len(guess_stats) < 50 :
    print(guess_stats)
    answer_state = screen.textinput(title=f'{len(guess_stats)}/50 States Correct', prompt="what's your another state's name?").title()

    if answer_state == 'Exit' :
        missing_state = []
        for state in state_data_list :
            if state not in guess_stats :
                missing_state.append(state)
            new_data = pandas.DataFrame(missing_state)
            new_data.to_csv(f'/missing')

    if answer_state in state_data_list :
        if answer_state in guess_stats :
            continue
        guess_stats.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto((int(state_data.x), int(state_data.y)))
        t.write(answer_state)



turtle.mainloop()