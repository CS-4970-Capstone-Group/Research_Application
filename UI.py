from tkinter import *
from tkinter import ttk
from tkinter import font  as tkfont
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql
import string
import pandas as pd
class ghostriders(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.text_font = tkfont.Font(family='Helvetica', size=18, weight="bold")
        self.title("Ghost Riders")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Home_Page, Research_Assistant, Signal_Classification, Data_Management, Analysis, Help, About, 
                    Individual_Risk, Revised_Classification, Accuracy_Report,
                    Import, Query, Delete,
                    Time_Series_Review, Cross_Analysis,
                    About_RA, CNN_Parameters, Medical):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        '''
        menubar = MenuBar(self)
        self.config(menu=menubar)
        '''
        self.geometry('900x650')
        self.show_frame("Home_Page")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()
'''
class MenuBar(Menu):
    def __init__(self, parent):
        Menu.__init__(self, parent)


        #Research Assistant
        research_assistant_menu = Menu(self, tearoff = False)
        self.add_cascade(label = "Research Assistant", menu = research_assistant_menu)
        research_assistant_menu.add_separator()
        research_assistant_menu.add_command(label = "Exit",command = self.quit)

        #Signal Classification
        signal_classification_menu = Menu(self, tearoff = False)
        self.add_cascade(label = "Signal Classification", menu = signal_classification_menu)
        signal_classification_menu.add_command(label = "Individual Risk", command = self.donothing)
        signal_classification_menu.add_command(label = "Revised Classification", command = self.donothing)
        signal_classification_menu.add_command(label = "Accuracy Report Risk", command = self.donothing)

        #Data Management
        data_management_menu = Menu(self, tearoff = False)
        self.add_cascade(label = "Data Management", menu = data_management_menu)
        data_management_menu.add_command(label = "Import", command = self.donothing)
        data_management_menu.add_command(label = "Review", command = self.donothing)
        data_management_menu.add_command(label = "Update", command = self.donothing)
        data_management_menu.add_command(label = "Delete", command = self.donothing)

        #Analysis
        anlysis_menu = Menu(self, tearoff = False)
        self.add_cascade(label = "Analysis", menu = anlysis_menu)
        anlysis_menu.add_command(label = "Time-Series Review", command = self.donothing)
        anlysis_menu.add_command(label = "Cross Analysis", command = self.donothing)

        #Help
        help_menu = Menu(self, tearoff = False)
        self.add_cascade(label = "Help", menu = help_menu)
        help_menu.add_command(label = "About RA", command = self.donothing)
        help_menu.add_command(label = "CNN Parameters", command = self.donothing)
        help_menu.add_command(label = "Medical", command = self.donothing)

        #About
        about_menu = Menu(self, tearoff = False)
        self.add_cascade(label = "About", menu = about_menu)
        about_menu.add_command(label = "About Developer", command = self.donothing)
        about_menu.add_command(label = "About Application", command = self.donothing)

        recordsmenu = Menu(self, tearoff=False)
        self.add_cascade(label="Records", underline=0, menu=recordsmenu)
        recordsmenu.add_command(label="Insert", command=lambda: ghostriders().show_frame("Insert_Page"))
        recordsmenu.add_command(label="Search", command=lambda: ghostriders().show_frame("PageTwo"))
    
    def quit(self):
        sys.exit(0)

    def donothing(self):
        filewin = Toplevel()
        button = Button(filewin, text="Do nothing button")
        button.pack()
'''
class Home_Page(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Home Page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = Button(self, text="Research Assistant", command=lambda: controller.show_frame("Research_Assistant"), height = 2, width = 16)
        button2 = Button(self, text="Signal Classification", command=lambda: controller.show_frame("Signal_Classification"), height = 2, width = 16)
        button3 = Button(self, text="Data Management", command=lambda: controller.show_frame("Data_Management"), height = 2, width = 16)
        button4 = Button(self, text="Analysis", command=lambda: controller.show_frame("Analysis"), height = 2, width = 16)
        button5 = Button(self, text="Help", command=lambda: controller.show_frame("Help"), height = 2, width = 16)
        button6 = Button(self, text="About", command=lambda: controller.show_frame("About"), height = 2, width = 16)
        button1.pack()
        button1.place(x = 0, y = 50)

        button2.pack()
        button2.place(x = 150, y = 50)

        button3.pack()
        button3.place(x = 300, y = 50)

        button4.pack()
        button4.place(x = 450, y = 50)

        button5.pack()
        button5.place(x = 600, y = 50)

        button6.pack()
        button6.place(x = 750, y = 50)

        load = Image.open("/Users/chulehou/Documents/Capstone_Mizzou/UI Design/Application_Home.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=150, y=200)

class Research_Assistant(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Research Assistant", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Back to the home page", command=lambda: controller.show_frame("Home_Page"), height = 2, width = 16)
        button.pack()

class Signal_Classification(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Signal Classification", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = Button(self, text="Individual Risk", command=lambda: controller.show_frame("Individual_Risk"), height = 2, width = 22)
        button2 = Button(self, text="Revised Classification", command=lambda: controller.show_frame("Revised_Classification"), height = 2, width = 22)
        button3 = Button(self, text="Accuracy Report", command=lambda: controller.show_frame("Accuracy_Report"), height = 2, width = 22)
        button4 = Button(self, text="Back to the home page", command=lambda: controller.show_frame("Home_Page"), height = 2, width = 22)
        button1.pack()
        button1.place(x = 50, y = 50)

        button2.pack()
        button2.place(x = 255, y = 50)

        button3.pack()
        button3.place(x = 460, y = 50)

        button4.pack()
        button4.place(x = 665, y = 50)

class Data_Management(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Data Management", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = Button(self, text = "Import", command = lambda: controller.show_frame("Import"), height = 2, width = 22)
        #button2 = Button(self, text = "Review", command = lambda: controller.show_frame("Review"), height = 2, width = 16)
        button3 = Button(self, text = "Query", command = lambda: controller.show_frame("Query"), height = 2, width = 22)
        button4 = Button(self, text = "Delete", command = lambda: controller.show_frame("Delete"), height = 2, width = 22)
        button5 = Button(self, text = "Back to the home page", command=lambda: controller.show_frame("Home_Page"), height = 2, width = 22)

        button1.pack()
        button1.place(x = 50, y = 50)

        #button2.pack()
        #button2.place(x = 230, y = 50)

        button3.pack()
        button3.place(x = 255, y = 50)
        
        button4.pack()
        button4.place(x = 460, y = 50)

        button5.pack()
        button5.place(x = 665, y = 50)

        load = Image.open("/Users/chulehou/Documents/Capstone_Mizzou/UI Design/Navicat.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=150, y=200)

class Analysis(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Analysis", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button1 = Button(self, text = "Time-Series Review", command = lambda: controller.show_frame("Time_Series_Review"), height = 2, width = 16)
        button2 = Button(self, text = "Cross Analysis", command = lambda: controller.show_frame("Cross_Analysis"), height = 2, width = 16)
        button3 = Button(self, text="Back to the home page", command=lambda: controller.show_frame("Home_Page"), height = 2, width = 16)
        button1.pack()
        button1.place(x = 230, y = 50)

        button2.pack()
        button2.place(x = 380, y = 50)

        button3.pack()
        button3.place(x = 530, y = 50)


class Help(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Help", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        
        button1 = Button(self, text = "About RA", command = lambda: controller.show_frame("About_RA"), height = 2, width = 22)
        button2 = Button(self, text = "CNN Parameters", command = lambda: controller.show_frame("CNN_Parameters"), height = 2, width = 22)
        button3 = Button(self, text = "Medical", command = lambda: controller.show_frame("Medical"), height = 2, width = 22)
        button4 = Button(self, text="Back to the home page", command=lambda: controller.show_frame("Home_Page"), height = 2, width = 22)
        button1.pack()
        button1.place(x = 50, y = 50)

        button2.pack()
        button2.place(x = 255, y = 50)

        button3.pack()
        button3.place(x = 460, y = 50)

        button4.pack()
        button4.place(x = 665, y = 50)

class About(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="About", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button = Button(self, text="Back to the home page", command=lambda: controller.show_frame("Home_Page"), height = 2, width = 16)
        button.pack()
        
#Subpages of Siganl Classification
class Individual_Risk(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Individual Risk", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        entry1 = Entry(self, bd=1)
        entry1.pack
        entry1.place(x = 100, y = 100, height = 35, width = 400)

        button1 = Button(self, text="Search", height = 2, width = 25)
        button1.pack()
        button1.place(x = 500, y = 100)

        button1 = Button(self, text="New Person", height = 2, width = 25)
        button1.pack()
        button1.place(x = 320, y = 170)

        button1 = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Signal_Classification"), height = 2, width = 16)
        button1.pack()
        button1.place(x = 370, y = 550)

class Revised_Classification(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Revised Classification", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Signal_Classification"), height = 2, width = 16)
        button.pack()
        
class Accuracy_Report(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Accuracy Report", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Signal_Classification"), height = 2, width = 16)
        button.pack()   
  
#Subpages of Data Management
class Import(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label1 = Label(self, text="Import", font=controller.title_font)
        label1.pack(side="top", fill="x", pady=10)
        label2 = Label(self, text="New Person", font=controller.title_font)
        label2.pack(side="top", fill="x", pady=15)

        label3 = Label(self, text="Name")
        label3.pack
        label3.place(x = 220, y = 100)

        self.entry1 = Entry(self, bd=1)
        self.entry1.pack
        self.entry1.focus_set()
        self.entry1.place(x = 400, y = 100)


        label4 = Label(self, text="Height(centimeters)")
        label4.pack
        label4.place(x = 220, y = 130)

        self.entry2 = Entry(self, bd=1)
        self.entry2.pack
        self.entry2.place(x = 400, y = 130)

        label5 = Label(self, text="Weight(Kilograms)")
        label5.pack
        label5.place(x = 220, y = 160)

        self.entry3 = Entry(self, bd=1)
        self.entry3.pack
        self.entry3.place(x = 400, y = 160)

        label6 = Label(self, text="Age")
        label6.pack
        label6.place(x = 220, y = 190)

        self.entry4 = Entry(self, bd=1)
        self.entry4.pack
        self.entry4.place(x = 400, y = 190)

        label7 = Label(self, text="Gender")
        label7.pack
        label7.place(x = 220, y = 220)

        # gender chose
        self.gender = StringVar() 
        self.gender_choosen = ttk.Combobox(self, width = 18, textvariable = self.gender) 
        # Adding combobox drop down list 
        self.gender_choosen['values'] = ('MALE',  
                                                'FEMALE') 
        self.gender_choosen.place(x = 400, y = 220) 
        self.gender_choosen.current()

        label8 = Label(self, text="Blood Pressure_high(mmHg)")
        label8.pack
        label8.place(x = 220, y = 250)

        self.entry6 = Entry(self, bd=1)
        self.entry6.pack
        self.entry6.place(x = 400, y = 250)

        label11 = Label(self, text="Blood Pressure_low(mmHg)")
        label11.pack
        label11.place(x = 220, y = 280)

        self.entry7 = Entry(self, bd=1)
        self.entry7.pack
        self.entry7.place(x = 400, y = 280)
        
        label8 = Label(self, text="Hypertension")
        label8.pack
        label8.place(x = 220, y = 310)

        # Hypertension chose
        self.hypertension = StringVar() 
        self.hypertension_choosen = ttk.Combobox(self, width = 18, textvariable = self.hypertension) 
        # Adding combobox drop down list 
        self.hypertension_choosen['values'] = ('YES',  
                                                'NO') 
        self.hypertension_choosen.place(x = 400, y = 310) 
        self.hypertension_choosen.current()

        label9 = Label(self, text="Has Ground Truth Data")
        label9.pack
        label9.place(x = 220, y = 340)

        self.ground_truth = StringVar() 
        self.ground_truth_choosen = ttk.Combobox(self, width = 18, textvariable = self.ground_truth) 
        # Adding combobox drop down list 
        self.ground_truth_choosen['values'] = ('YES',  
                                                'NO') 
        self.ground_truth_choosen.place(x = 400, y = 340) 
        self.ground_truth_choosen.current()

        label10 = Label(self, text="Ethnicity")
        label10.pack
        label10.place(x = 220, y = 370)

        self.ethnicity = StringVar() 
        self.ethnicitychoosen = ttk.Combobox(self, width = 18, textvariable = self.ethnicity) 
        # Adding combobox drop down list 
        self.ethnicitychoosen['values'] = ('African',  
                                    'Aboriginal American', 
                                    'Aboriginal Australian', 
                                    'East-Asian', 
                                    'Caucasian', 
                                    'Indian', 
                                    'Latinx', 
                                    'Middle-Eastern', 
                                    'Multi-Ethnic', 
                                    'Pacific-Islander') 
        self.ethnicitychoosen.place(x = 400, y = 370) 
        self.ethnicitychoosen.current() 
        
        button1 = Button(self, text="Upload Data to Database", height = 2, width = 25, command = lambda: [self.dbimport(),self.clear()])
        button1.pack()
        button1.place(x = 340, y = 500)

        button2 = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Data_Management"), height = 2, width = 25)
        button2.pack()
        button2.place(x = 340, y = 550)


    def dbimport(self):
        self.name = self.entry1.get().strip()
        self.height = self.entry2.get().strip()
        self.weight = self.entry3.get().strip()
        self.age = self.entry4.get().strip()
        self.bloodh = self.entry6.get().strip()
        self.bloodl = self.entry7.get().strip()
        self.ethnicity = self.ethnicitychoosen.get().strip()
        self.gender = self.gender_choosen.get().strip()
        self.hypertension = self.hypertension_choosen.get().strip()
        self.ground_truth = self.ground_truth_choosen.get().strip()

        db = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='12345678',
            db='GhostRiders',
            charset='utf8'
            )
        # get cursor
        cursor = db.cursor()
        # SQL insert command
        sql = "INSERT INTO subject(name,height,weight,age,blood_pressure_high,blood_pressure_low,ethnicity,gender,hypertension,ground_truth) VALUES ('%s','%s','%s', '%s', '%s','%s','%s', '%s','%s','%s')" % (self.name, self.height, self.weight, self.age, self.bloodh, self.bloodl, self.ethnicity,self.gender, self.hypertension, self.ground_truth)
        try:
            # execute the sql command
            cursor.execute(sql)
            print("Insert the data successfully")
            messagebox.showinfo("INFO", "Insert the Data Successfully")
            # submit to the database
            db.commit()
        except:
            print("Insert the data fail")
            # Rollback in case there is any error
            db.rollback()

        # Close the database
        db.close()

    def clear(self):
        self.entry1.delete(0,END)
        self.entry2.delete(0,END)
        self.entry3.delete(0,END)
        self.entry4.delete(0,END)
        self.entry6.delete(0,END)
        self.entry7.delete(0,END)
'''
class Review(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label1 = Label(self, text="Review", font=controller.title_font)
        label1.pack(side="top", fill="x", pady=10)

        label2 = Label(self, text="This is the recent data", font=controller.text_font)
        label2.pack()
        label2.place(x = 350, y = 50)

        button1 = Button(self, text="Show Recent Data", height = 2, width = 16)
        button1.pack()
        button1.place(x = 375, y = 450)

        button2 = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Data_Management"), height = 2, width = 16)
        button2.pack()
        button2.place(x = 375, y = 500)
'''
class Query(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Query", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        label2 = Label(self, text="Input the id to update", font=controller.text_font)
        label2.pack()
        label2.place(x = 350, y = 50)

        self.entry1 = Entry(self, bd=1)
        self.entry1.pack
        self.entry1.place(x = 100, y = 100, height = 35, width = 400)

        button1 = Button(self, text="Search", height = 2, width = 25, command = lambda: [self.dbsearch(), self.clear()])
        button1.pack()
        button1.place(x = 500, y = 100)

        #Treeview组件
        self.treeAddressList = ttk.Treeview(self,
                                       columns=('c1', 'c2', 'c3','c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11'),
                                       show="headings",
                                       )

        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=(None, 13))

        self.treeAddressList.column('c1', width=40, anchor='center')
        self.treeAddressList.column('c2', width=30, anchor='center')
        self.treeAddressList.column('c3', width=50, anchor='center')
        self.treeAddressList.column('c4', width=50, anchor='center')
        self.treeAddressList.column('c5', width=50, anchor='center')
        self.treeAddressList.column('c6', width=130, anchor='center')
        self.treeAddressList.column('c7', width=130, anchor='center')
        self.treeAddressList.column('c8', width=80, anchor='center')
        self.treeAddressList.column('c9', width=80, anchor='center')
        self.treeAddressList.column('c10', width=130, anchor='center')
        self.treeAddressList.column('c11', width=60, anchor='center')

        self.treeAddressList.heading('c1', text='name')
        self.treeAddressList.heading('c2', text='age')
        self.treeAddressList.heading('c3', text='gender')
        self.treeAddressList.heading('c4', text='height')
        self.treeAddressList.heading('c5', text='weight')
        self.treeAddressList.heading('c6', text='blood_pressure_hight')
        self.treeAddressList.heading('c7', text='blood_pressure_low')
        self.treeAddressList.heading('c8', text='hypertension')
        self.treeAddressList.heading('c9', text='ground_truth')
        self.treeAddressList.heading('c10', text='heart_failure_risk')
        self.treeAddressList.heading('c11', text='ethnicity')

        self.treeAddressList.pack()
        self.treeAddressList.place(x = 20, y = 180)
    
        button = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Data_Management"), height = 2, width = 16)
        button.pack()
        button.place(x = 375, y = 500)

    def dbsearch(self):
        self.searchid = self.entry1.get().strip()
        db = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='12345678',
            db='GhostRiders',
            charset='utf8'
            )
        # get cursor
        cursor = db.cursor()
        # SQL insert command
        sql = "SELECT * FROM  subject WHERE subject_id = '%s' " % (self.searchid)

        try:
            # execute the sql command
            cursor.execute(sql)
            temp = cursor.fetchall()
            # submit to the database
            db.commit()
            for i, item in enumerate(temp):
                self.treeAddressList.insert('', i, values=item[1:])
            print("search the data successfully")
        except:
            print("search the data fail")
            # Rollback in case there is any error
            messagebox.showinfo("INFO", "Failed to Search")
            db.rollback()
        # Close the database
        db.close()
    def clear(self):
        self.entry1.delete(0,END)


class Delete(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Delete", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        label2 = Label(self, text="Input the id to delete", font=controller.text_font)
        label2.pack()
        label2.place(x = 350, y = 50)

        self.entry1 = Entry(self, bd=1)
        self.entry1.pack
        self.entry1.place(x = 100, y = 100, height = 35, width = 400)

        button1 = Button(self, text="Delete", height = 2, width = 25, command = lambda:[self.dbdelete(), self.clear()])
        #button1 = Button(self, text="Delete", height = 2, width = 25, command = self.dbdelete)
        button1.pack()
        button1.place(x = 500, y = 100)

        button = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Data_Management"), height = 2, width = 16)
        button.pack()
        button.place(x = 375, y = 500)

    def dbdelete(self):
        self.inputid = self.entry1.get().strip()
        db = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            passwd='12345678',
            db='GhostRiders',
            charset='utf8'
            )
        # get cursor
        cursor = db.cursor()
        # SQL insert command
        sql = "DELETE FROM subject WHERE subject_id = '%s' " % (self.inputid)
        try:
            # execute the sql command
            cursor.execute(sql)
            print("delete the data successfully")
            # submit to the database
            db.commit()
            messagebox.showinfo("INFO", "Successfully delete")
        except:
            print("delete the data fail")
            # Rollback in case there is any error
            messagebox.showinfo("INFO", "Failed to delete")
            db.rollback()
        # Close the database
        db.close()
    def clear(self):
        self.entry1.delete(0,END)

#Subpages of Analysis
class Time_Series_Review(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Time-Series Review", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Analysis"), height = 2, width = 16)
        button.pack()

class Cross_Analysis(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Cross Analysis", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Analysis"), height = 2, width = 16)
        button.pack()

#Subpages of Help
class About_RA(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="About RA", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Help"), height = 2, width = 16)
        button.pack()

class CNN_Parameters(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Time-Series Review", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Help"), height = 2, width = 16)
        button.pack()

class Medical(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Medical", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Help"), height = 2, width = 16)
        button.pack()

if __name__ == "__main__":
    app = ghostriders()
    app.mainloop()