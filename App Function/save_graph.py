import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw
import cv2
import numpy as np

root = tk.Tk()

def save_graph():
    filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg")
    if not filename:
        return
    edge.save(filename)

img = cv2.imread('/Users/chulehou/Desktop/Application_Home.jpg')
edge = Image.fromarray(img)

tk_edge = ImageTk.PhotoImage(edge)
label = tk.Label(root, image=tk_edge)
label.pack()

button = tk.Button(root, text = "save as", command = save_graph)
button.pack()

root.mainloop()