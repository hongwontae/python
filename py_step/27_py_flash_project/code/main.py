import tkinter
import pandas
import random
import time
BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv('./data/french_words.csv')
to_learn = data.to_dict(orient="records")

current_card = {}

#-----------------Flash card create ------------------#
def next_card () :
    global current_card, file_timer
    window.after_cancel(file_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text='French', fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_image)
    file_timer = window.after(3000, flip_card)


def flip_card () :
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill='white')
    canvas.itemconfig(card_background, image = card_back_image)

def is_known () :
    to_learn.remove(current_card)
    next_card()

    


window = tkinter.Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

file_timer = window.after(3000, flip_card)

canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = tkinter.PhotoImage(file='./images/card_front.png')
card_back_image = tkinter.PhotoImage(file='./images/card_back.png')
card_background = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text='', font=('Ariel', 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=('Ariel', 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross_image = tkinter.PhotoImage(file='./images/wrong.png')
unknown_button = tkinter.Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = tkinter.PhotoImage(file='./images/right.png')
know_button = tkinter.Button(image=check_image, highlightthickness=0, command=is_known)
know_button.grid(row=1, column=1)

next_card()

window.mainloop()
