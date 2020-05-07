from tkinter import *
from tkinter import ttk
from research_dbms import Research_DBMS as db

class Research_Interface():


    def init_interface(self):
        #Establish Main Frame
        root = Tk()
        root.title("Research Subject")
        root.geometry("800x600")

        name_label = Label(root, text="Name")
        name_label.pack
        name_label.place(x=250, y=100)

        name_entry = Entry(root)
        name_entry.pack
        name_entry.place(x=400, y=100)

        height_label = Label(root, text="Height(centimeters)")
        height_label.pack
        height_label.place(x=250, y=130)

        height_entry = Entry(root, bd=1)
        height_entry.pack
        height_entry.place(x=400, y=130)

        weight_label = Label(root, text="Weight(Kilograms)")
        weight_label.pack
        weight_label.place(x=250, y=160)

        weight_entry = Entry(root, bd=1)
        weight_entry.pack
        weight_entry.place(x=400, y=160)

        age_label = Label(root, text="Age")
        age_label.pack
        age_label.place(x=250, y=190)

        age_entry = Entry(root, bd=1)
        age_entry.pack
        age_entry.place(x=400, y=190)

        gender_label = Label(root, text="Gender")
        gender_label.pack
        gender_label.place(x=250, y=220)

        gender_var = IntVar()
        gender_var.set(1)
        male_radio = Radiobutton(root, text="Male", value=1, variable=gender_var)
        male_radio.pack()
        male_radio.place(x=400, y=220)
        female_radio = Radiobutton(root, text="Female", value=2, variable=gender_var)
        female_radio.pack()
        female_radio.place(x=480, y=220)
        unspecified_radio = Radiobutton(root, text="Unspecified", value=3, variable=gender_var)
        unspecified_radio.pack()
        unspecified_radio.place(x=560, y=220)

        bp_label = Label(root, text="Blood Pressure(mmHg)")
        bp_label.pack
        bp_label.place(x=250, y=250)

        bp_entry = Entry(root, bd=1)
        bp_entry.pack
        bp_entry.place(x=400, y=250)

        ht_label = Label(root, text="Hypertension")
        ht_label.pack
        ht_label.place(x=250, y=280)

        ht_val = IntVar()
        ht_val.set(3)
        ht_yes_radio = Radiobutton(root, text="Yes", value=1, variable=ht_val)
        ht_yes_radio.pack()
        ht_yes_radio.place(x=400, y=280)
        ht_no_radio = Radiobutton(root, text="No", value=0, variable=ht_val)
        ht_no_radio.pack()
        ht_no_radio.place(x=480, y=280)

        gt_label = Label(root, text="Has Ground Truth Data")
        gt_label.pack
        gt_label.place(x=250, y=310)

        gt_val = IntVar()

        gt_val.set(3)

        gt_yes_radio = Radiobutton(root, text="Yes", value=5, variable=gt_val)
        gt_yes_radio.pack()
        gt_yes_radio.place(x=400, y=310)
        gt_no_radio = Radiobutton(root, text="No", value=6, variable=gt_val)
        gt_no_radio.pack()
        gt_no_radio.place(x=480, y=310)

        ethnicity_label = Label(root, text="Ethnicity")
        ethnicity_label.pack
        ethnicity_label.place(x=250, y=340)

        ethncity = StringVar()
        ethnicity_val = ttk.Combobox(root, width=18, textvariable=ethncity)

        # Adding combobox drop down list
        ethnicity_val['values'] = ('African',
                                    'Aboriginal American',
                                    'Aboriginal Australian',
                                    'East-Asian',
                                    'Caucasian',
                                    'Indian',
                                    'Latinx',
                                    'Middle-Eastern',
                                    'Multi-Ethnic',
                                    'Pacific-Islander')
        ethnicity_val.place(x=400, y=340)
        ethnicity_val.current()

        insert_person_button = Button(root, text="Add Subject", height=2, width=25, command=lambda: self.insert_person(
            name_entry.get(), age_entry.get(), height_entry.get(), weight_entry.get(), gender_var.get(), bp_entry.get(),
            ht_val.get(), gt_val.get(), ethnicity_val.get()))
        insert_person_button.pack()
        insert_person_button.place(x=340, y=400)

        upload_data_button = Button(root, text="Upload Data file format: CSV", height=2, width=25)
        upload_data_button.pack()
        upload_data_button.place(x=340, y=500)


        root.mainloop()

    def client_exit(self):
        exit()

    def insert_person(self, name, age, height, weight, gender, bp, ht, gt, ethnicity):
        db.insert_person(self, age, gender, height, weight, bp, ht, gt, ethnicity, name)

#root = tk.Tk()
#interface = Research_Interface(root)

#interface.start_interface()
if __name__ == '__main__':
    print("hello")
    interface = Research_Interface()
    interface.init_interface()





    '''self.root.title("Heart Failure Research Assistant")
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
            self.root.mainloop()'''