from tkinter import *
from tkinter import ttk
from tkinter import font  as tkfont

class ghostriders(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
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
                    Import, Review, Update, Delete,
                    Time_Series_Review, Cross_Analysis,
                    About_RA, CNN_Parameters, Medical):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
        menubar = MenuBar(self)
        self.config(menu=menubar)

        self.geometry('900x650')
        self.show_frame("Home_Page")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

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
        '''
        photo = PhotoImage("/Users/chulehou/Documents/Capstone_Mizzou/UI Design/heartbeat.gif")

        label = Label(image=photo)
        label.image = photo # keep a reference!
        label.pack()
        label.place(x = 50, y = 200)
        '''
class Insert_Page(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        label = Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        page = ttk.Notebook(self)
        tab1 = ttk.Frame(page)
        tab2 = ttk.Frame(page)
        tab3 = ttk.Frame(page)

        page.add(tab1, text='One')
        page.add(tab2, text='Two')
        page.add(tab3, text='three')

        page.pack(fill=BOTH, expand=1)

        day_label = Label(tab1, text="Tab1:")
        day_label.pack()
        day_label.place(x=0, y=30)
        day_label = Label(tab2, text="Tab2:")
        day_label.pack()
        day_label.place(x=0, y=30)
        day_label = Label(tab3, text="Tab3:")
        day_label.pack()
        day_label.place(x=0, y=30)

        button = Button(self, text="Back to the home page", command=lambda: controller.show_frame("Home_Page"), height = 2, width = 16)
        button.pack()

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
        button1 = Button(self, text = "Import", command = lambda: controller.show_frame("Import"), height = 2, width = 16)
        button2 = Button(self, text = "Review", command = lambda: controller.show_frame("Review"), height = 2, width = 16)
        button3 = Button(self, text = "Update", command = lambda: controller.show_frame("Update"), height = 2, width = 16)
        button4 = Button(self, text = "Delete", command = lambda: controller.show_frame("Delete"), height = 2, width = 16)
        button5 = Button(self, text = "Back to the home page", command=lambda: controller.show_frame("Home_Page"), height = 2, width = 16)

        button1.pack()
        button1.place(x = 80, y = 50)

        button2.pack()
        button2.place(x = 230, y = 50)

        button3.pack()
        button3.place(x = 380, y = 50)
        
        button4.pack()
        button4.place(x = 530, y = 50)

        button5.pack()
        button5.place(x = 680, y = 50)

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
        label3.place(x = 250, y = 100)

        entry1 = Entry(self, bd=1)
        entry1.pack
        entry1.place(x = 400, y = 100)


        label4 = Label(self, text="Height(centimeters)")
        label4.pack
        label4.place(x = 250, y = 130)

        entry2 = Entry(self, bd=1)
        entry2.pack
        entry2.place(x = 400, y = 130)

        label5 = Label(self, text="Weight(Kilograms)")
        label5.pack
        label5.place(x = 250, y = 160)

        entry3 = Entry(self, bd=1)
        entry3.pack
        entry3.place(x = 400, y = 160)

        label6 = Label(self, text="Age")
        label6.pack
        label6.place(x = 250, y = 190)

        entry4 = Entry(self, bd=1)
        entry4.pack
        entry4.place(x = 400, y = 190)

        label7 = Label(self, text="Gender")
        label7.pack
        label7.place(x = 250, y = 220)

        # 定义变量
        v1 = IntVar()
        # 设置第二个未默认
        v1.set(1)
        # 单选框
        r1 = Radiobutton(self, text="Male", value=1, variable=v1)
        r1.pack()
        r1.place(x = 400, y = 220)
        r2 = Radiobutton(self, text="Female", value=2, variable=v1)
        r2.pack()
        r2.place(x = 480, y = 220)

        label8 = Label(self, text="Blood Pressure(mmHg)")
        label8.pack
        label8.place(x = 250, y = 250)

        entry6 = Entry(self, bd=1)
        entry6.pack
        entry6.place(x = 400, y = 250)
        
        label8 = Label(self, text="Hypertension")
        label8.pack
        label8.place(x = 250, y = 280)

        # 定义变量
        v2 = IntVar()
        # 设置第二个未默认
        v2.set(3)
        # 单选框
        r3 = Radiobutton(self, text="Yes", value=3, variable=v2)
        r3.pack()
        r3.place(x = 400, y = 280)
        r4 = Radiobutton(self, text="No", value=4, variable=v2)
        r4.pack()
        r4.place(x = 480, y = 280)

        label9 = Label(self, text="Has Ground Truth Data")
        label9.pack
        label9.place(x = 250, y = 310)

        # 定义变量
        v3 = IntVar()
        # 设置第二个未默认
        v3.set(3)
        # 单选框
        r5 = Radiobutton(self, text="Yes", value=5, variable=v3)
        r5.pack()
        r5.place(x = 400, y = 310)
        r6 = Radiobutton(self, text="No", value=6, variable=v3)
        r6.pack()
        r6.place(x = 480, y = 310)

        label10 = Label(self, text="Ethncity")
        label10.pack
        label10.place(x = 250, y = 340)

        ethncity = StringVar() 
        ethncityhoosen = ttk.Combobox(self, width = 18, textvariable = ethncity) 
  
        # Adding combobox drop down list 
        ethncityhoosen['values'] = ('African',  
                                    'Aboriginal American', 
                                    'Aboriginal Australian', 
                                    'East-Asian', 
                                    'Caucasian', 
                                    'Indian', 
                                    'Latinx', 
                                    'Middle-Eastern', 
                                    'Multi-Ethnic', 
                                    'Pacific-Islander') 
        ethncityhoosen.place(x = 400, y = 340) 
        ethncityhoosen.current() 
        
        button1 = Button(self, text="Upload Data file format: CSV", height = 2, width = 25)
        button1.pack()
        button1.place(x = 340, y = 500)

        button2 = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Data_Management"), height = 2, width = 25)
        button2.pack()
        button2.place(x = 340, y = 550)


class Review(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Review", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Data_Management"), height = 2, width = 16)
        button.pack()

class Update(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Update", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Data_Management"), height = 2, width = 16)
        button.pack()

class Delete(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Delete", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Data_Management"), height = 2, width = 16)
        button.pack()

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
