from tkinter import *
from tkinter import messagebox
import random
import pyperclip

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
           'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
CAPITAL_LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
PASSWORD_LENGTH = 24
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    password_list = []
    password_name.delete(0, END)

    choice_list = [LETTERS, CAPITAL_LETTERS, NUMBERS, SYMBOLS]
    choice_list = [x for xs in choice_list for x in xs]

    for char in range(PASSWORD_LENGTH):
        password_list.append(random.choice(choice_list))

    random.shuffle(password_list)

    password = "".join(password_list)
    password_name.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    if not website_name.get():
        messagebox.showinfo(message="Please specify a website.")
    elif not password_name.get():
        messagebox.showinfo(message='Please enter a password, or press "Generate Password" to generate one.')
    else:
        with open('passwords.txt', 'a') as f:
            f.write(f"{website_name.get()}  |  {email_name.get()}  |  {password_name.get()}\n")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

Label(window, text="Website:", font=("Arial", 10, "bold")).grid(row=1, column=0)
website_name = Entry(width=52)
website_name.grid(row=1, column=1, columnspan=2, sticky="w")
website_name.focus()

Label(window, text="Email/Username:", font=("Arial", 10, "bold")).grid(row=2, column=0)
email_name = Entry(width=52)
email_name.grid(row=2, column=1, columnspan=2, sticky="w")
email_name.insert(0, "henrik.std@gmail.com")

Label(window, text="Password:", font=("Arial", 10, "bold")).grid(row=3, column=0)
password_name = Entry(width=33)
password_name.grid(row=3, column=1, sticky="w")

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()
