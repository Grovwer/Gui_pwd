from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_pwd():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]

    password_symbol = [choice(symbols) for _ in range(randint(2, 4))]

    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_letters + password_symbol
    shuffle(password_list)

    password = "".join(password_list)
    passwd_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = passwd_entry.get()
    passwd_entry.config()
    new_data = {
        website: {
            "email": email,
            "password": password

        }
    }


    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops", message="please make ")

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

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Pwd")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email:{email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No data for {website}")
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20)

canvas = Canvas(window, width=200, height=200, highlightthickness=0)

logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

label_web = Label(text="Website")
label_web.grid(column=0, row=1)

label_email= Label(text="Email/Username")
label_email.grid(column=0, row=2)

label_paswd = Label(text="Password")
label_paswd.grid(column=0, row=3)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "angel@86.ru")
passwd_entry = Entry(width=16)
passwd_entry.grid(column=1, row=3)

generate_pwd_button = Button(text="Generate Password", command=generate_pwd)
generate_pwd_button.grid(row=3, column= 2)

add_button = Button(text="add", width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=10, command=find_password)
search_button.grid(row=1, column=2)
window.mainloop()