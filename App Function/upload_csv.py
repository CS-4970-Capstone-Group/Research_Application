import tkinter as tk
from tkinter import filedialog
import pandas as pd

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def upload_csv ():
    global df
    
    import_file_path = filedialog.askopenfilename()
    df = pd.read_csv (import_file_path)
    print (df)
    
browseButton_CSV = tk.Button(text="      Import CSV     ", command=upload_csv, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 150, window=browseButton_CSV)

root.mainloop()