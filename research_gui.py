import tkinter as tk
frame = tk.Frame

#Just a lot of basic code used to help me get familiarized with the tkinter library.
class Research_Interface(frame):
    def __init__(self, root=None):
        frame.__init__(self, root)
        self.root = root
        self.init_interface()

    def init_interface(self):
        self.root.title("Heart Failure Research Assistant")
        self.pack(fill=tk.BOTH, expand=1)
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)
        file = tk.Menu(menu)
        file.add_command(label="Exit", command=self.client_exit)
        menu.add_cascade(label="File", menu=file)
        edit = tk.Menu(menu)
        edit.add_command(label="Undo")
        menu.add_cascade(label="Edit", menu=edit)
        im = tk.PhotoImage(file="brain_and_heart.png", master=self.root)
        im = im.subsample(9)
        introduction = tk.Label(self.root, text="Heart Failure Research Assistant").pack(side="left")
        greeting = ""
        logo = tk.Label(self.root, justify=tk.LEFT, compound=tk.LEFT, padx=5, text=greeting, image=im).pack(side="left")
        upload_button = tk.Button(self.root, text="Upload", command="").pack()
        self.root.mainloop()

    def client_exit(self):
        exit()



root = tk.Tk()
interface = Research_Interface(root)

#interface.start_interface()
