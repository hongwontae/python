import tkinter
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def count_start () :
    count_down(10)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down (count) :
    count_min = math.floor(count/60)
    count_sec = count % 60
    print(count_sec)
    print(type(count_sec))
    
    if count_sec == 0 or 00 :
        count_sec = '00'

    if count_sec < 10 :
        count_sec = f'0{count_sec}'
        print(count_sec)

    canvas.itemconfig(timer_text, text=f"{count_min} : {count_sec}")
    if count > 0 :
        window.after(1000, count_down, count-1)
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Pomodora')
window.config(padx=100, pady=50, bg=YELLOW)

my_label= tkinter.Label(text='Timer', fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW)
my_label.grid(column=1, row=0)


canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
created_image = tkinter.PhotoImage(file='./tomato.png')
canvas.create_image(100, 112, image=created_image)
timer_text = canvas.create_text(100, 130, text='00:00', font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)

start_button = tkinter.Button(text='Start', highlightthickness=0, command=count_start)
start_button.grid(column=0, row=2)

reset_button = tkinter.Button(text='Reset', highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = tkinter.Label(text='Check', fg=RED, bg=YELLOW, font=(FONT_NAME, 32, "bold"))
check_marks.grid(column=1, row=3)


window.mainloop()