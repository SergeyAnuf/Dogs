from cProfile import label
from tkinter import *
from tkinter import Label

import requests
from PIL import  Image, ImageTk
from io import BytesIO

from bron import window

window = Tk()
window.title("Картинки с собачками")
window.geometry("360x420")

label = Label()
label.pack(pady=10)

button = Button(text="Загрузить изображение", command=show_image)
button.pack(pady=10)

window.mainloop()
