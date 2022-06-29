from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(800, 600)

# Label

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.pack(side="top")

my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button


def button_clicked():
    my_label["text"] = input_player.get()


button = Button(text="Click me", command=button_clicked)
button.pack()

# Entry

input_player = Entry(width=10)
input_player.pack()
print(input_player.get())

window.mainloop()