from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")

words_to_learn = df.to_dict(orient="records")

current_card = {}


def new_french_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words_to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_text, text=current_card["French"])
    canvas.itemconfig(canvas_image, image=card_img_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=current_card["English"], fill="white")
    canvas.itemconfig(canvas_image, image=card_img_back)


def known_word():
    words_to_learn.remove(current_card)
    data = pd.DataFrame(words_to_learn)

    data.to_csv("data/words_to_learn.csv", index=False)

    new_french_card()


def unknown_word():
    new_french_card()


window = Tk()
window.title("Flash Card Game")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img_front = PhotoImage(file="images/card_front.png")
card_img_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_img_front)
card_title = canvas.create_text(400, 150, font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
canvas.grid(row=1, column=1, columnspan=2)

new_french_card()
yes_image = PhotoImage(file="images/right.png")
yes_button = Button(image=yes_image, relief="ridge", command=known_word)
yes_button.grid(row=2, column=2)

no_image = PhotoImage(file="images/wrong.png")
no_button = Button(image=no_image, relief="ridge", command=unknown_word)
no_button.grid(row=2, column=1)

window.mainloop()
