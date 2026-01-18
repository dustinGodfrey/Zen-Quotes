import ast
import time
import random
import customtkinter
from PIL import Image



customtkinter.set_appearance_mode("light")
app = customtkinter.CTk()
app.title("Zen Quotes")
app.geometry('1024x600')
app.attributes("-fullscreen", True)


background_image = customtkinter.CTkImage(
    light_image=Image.open("zen_quotes.jpg"),
    dark_image=Image.open("zen_quotes.jpg"),
    size=(1024, 600)
)


background_label = customtkinter.CTkLabel(app, image=background_image, text="")
background_label.place(x=0, y=0, relwidth=1, relheight=1)


quote_box = customtkinter.CTkLabel(app, image=background_image, text="", wraplength=650, font=("URW Chancery L", 18, "italic"))
quote_box.pack(expand=True)

with open('zen_quotes.txt', 'r') as file:
    quotes = file.readlines()
    


def rand_quotes():
    rand_q = (ast.literal_eval(random.choice(quotes)))
    quote_box.configure(text=(rand_q))
    app.after(300000, rand_quotes) # 5 minutes


rand_quotes()

app.mainloop()



