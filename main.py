from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
data_list= data.to_dict(orient='records') # [list of dictionaries{keys: 'French', 'English}]

#-------------------Change canvas items----------------------#

def replace_canvas_items(transition_image, transition_lang, transition_word, text_color = "black"):
    flash_card.itemconfig(canvas_image, image=transition_image)
    flash_card.itemconfig(language,text=transition_lang, fill=text_color)
    flash_card.itemconfig(word, text=transition_word, fill=text_color)

def show_answer():
    replace_canvas_items(flash_back_img, "English", data_list[0]["English"], text_color="white")

def right():
    data_list.remove(data_list[0])
    replace_canvas_items(flash_front_img, "French", data_list[0]["French"])
    timer = window.after(3000, func=show_answer)

def wrong():
    random.shuffle(data_list)
    replace_canvas_items(flash_front_img, "French", data_list[0]["French"])
    timer = window.after(3000, func=show_answer)
    

#--------------------------UI Setup--------------------------#
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady= 50, bg=BACKGROUND_COLOR)

# flash card
flash_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_front_img = PhotoImage(file="images/card_front.png")
flash_back_img = PhotoImage(file="images/card_back.png")
canvas_image = flash_card.create_image(410, 270,image=flash_front_img)
language = flash_card.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
word = flash_card.create_text(400, 263, text="trouve", font=("Ariel", 60, "bold"))
flash_card.grid(column=0, row=0, columnspan=2)


# buttons
cross_img = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=wrong)
cross_button.grid(column=0, row=1)

tick_img = PhotoImage(file="images/right.png")
tick_button = Button(image=tick_img, highlightthickness=0, bg=BACKGROUND_COLOR, command=right)
tick_button.grid(column=1, row=1)


timer = window.after(3000, func=show_answer)




window.mainloop()