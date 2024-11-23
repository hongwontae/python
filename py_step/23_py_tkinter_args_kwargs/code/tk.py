import tkinter;

window = tkinter.Tk()
window.title('My First Program')
window.minsize(width=500, height=300)

my_label = tkinter.Label(text='This is my one', font=('Arial', 24, 'bold'))
# my_label.config(text='Chage the Text')
my_label.grid(column=0, row=0)

def click_text_change_handler () :
    print('Click yes')
    input_data = my_input.get()
    my_label.config(text=input_data)

my_button_2 = tkinter.Button(text='2button')
my_button_2.grid(column=2, row=0)

my_button = tkinter.Button(text='Click Me', command=click_text_change_handler)
my_button.grid(column=1, row=1)

my_input = tkinter.Entry()
my_input.grid(column=2, row=2)

window.mainloop()