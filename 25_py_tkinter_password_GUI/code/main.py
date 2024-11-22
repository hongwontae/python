import tkinter
import tkinter.messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password () : 
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_number = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_number
    print(password_list)
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save () :
    web_value = website_entry.get()
    email_value = email_username_entry.get()
    password_value = password_entry.get()

    new_dic = {
        web_value : {
            "email" : email_value,
            "password" : password_value
        }
    }

    if len(email_value) == 0 or len(web_value) == 0 or len(password_value) == 0 :
        tkinter.messagebox.showinfo(title='email password not', message='retry!')
    else :
        try :
            with open('./private_data.json', mode='r') as p_file :
                existing_data = json.load(p_file)
        except FileNotFoundError :
            with open('./private_data.json', mode='w') as p_file :
                json.dump(new_dic, p_file, indent=4)
        else :
            existing_data.update(new_dic)
            with open('./private_data.json', mode='w') as p_file :
                json.dump(existing_data, p_file, indent=4)
        finally :
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)

# ----------------Search Function ----------------------#
def search_handelr () :
    website_value = website_entry.get()

    with open('./private_data.json') as p_file :
        all_private_data_dict = json.load(p_file)
        if website_value in all_private_data_dict :
            email = all_private_data_dict[website_value]["email"]
            password = all_private_data_dict[website_value]["password"]
            tkinter.messagebox.showinfo(title='Your Private Data', message=f'website={website_value} \n email={email} password={password}')



# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Password Generator')
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=200, height=200)
my_image = tkinter.PhotoImage(file='./logo.png')
canvas.create_image(100, 100, image=my_image)
canvas.grid(column=1, row=0)

website_label = tkinter.Label(text='Website : ')
website_label.grid(column=0, row=1)
website_entry = tkinter.Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)
wensite_button = tkinter.Button(text='Search', width=10, command=search_handelr)
wensite_button.grid(row=1, column=2)

email_username_label = tkinter.Label(text='Email/Username : ')
email_username_label.grid(column=0, row=2)
email_username_entry = tkinter.Entry(width=35)
email_username_entry.insert(0, 'dnjsxoghd@naver.com')
email_username_entry.grid(row=2, column=1, columnspan=2)

password_label = tkinter.Label(text='Password : ')
password_label.grid(row=3, column=0)
password_entry = tkinter.Entry(width=21)
password_entry.grid(column=1, row=3)
generator_button = tkinter.Button(text='Generate Password', command=generate_password)
generator_button.grid(column=2, row=3)

add_button = tkinter.Button(text='Add' ,width=36, command=save)
add_button.grid(column=1, columnspan=2, row=4)



window.mainloop()
