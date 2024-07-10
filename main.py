from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_pass():
    website = web_entry.get()
    try:

        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="error", message="database empty")

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\nPassword: {password}")

        

        else:
            messagebox.showinfo(title="Error", message=f"{website} doesnt exist in the data base; check the spelling")




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_num = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_num

    random.shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_entry.get()
    emai = email_entry.get()
    pas = pass_entry.get()
    new_data = {
        web: {"email": emai,
              "password": pas,
              }
    }

    if len(web) == 0 or len(pas) == 0:
        messagebox.showinfo(title="oops", message="dont leave emtpy")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)


        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("password manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website = Label(text="website")
website.grid(row=1, column=0)
email = Label(text="email/username")
email.grid(row=2, column=0)
password = Label(text="password")
password.grid(row=3, column=0)

web_entry = Entry(width=21)
web_entry.grid(row=1, column=1,)
web_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "moiz@email.com")
pass_entry = Entry(width=18)
pass_entry.grid(row=3, column=1)

gen_pass = Button(text="generate password", command=password_generator)
gen_pass.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text = "search", command= find_pass)
search_button.grid(row = 1, column = 2)

window.mainloop()
