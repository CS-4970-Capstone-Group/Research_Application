from tkinter import *
from tkinter import ttk
from tkinter import font  as tkfont
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import filedialog
import pymysql
import string
import pandas as pd
#import gui_dbms as gdb

import sys
import os

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
        for F in (Home_Page, Research_Assistant, Data_Visualization, Data_Management, Analysis, Help, About, 
                    Age_Visualization, Weight_Visualization, BMI_Visualization,
                    Import, Query, Delete,
                    Individual_Classification, Cross_Analysis,
                    About_RA, CNN_Parameters, Medical):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.geometry('900x650')
        self.show_frame("Home_Page")

    def show_frame(self, page_name):
        #Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()

class Home_Page(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label_home_page_title = Label(self, text="Home Page", font=controller.title_font)
        label_home_page_title.pack(side="top", fill="x", pady=10)

        button_research_assistant_menu = Button(self, text="Research Assistant", command=lambda: controller.show_frame("Research_Assistant"), height = 2, width = 16)
        button_signal_classification_menu = Button(self, text="Data Visualization", command=lambda: controller.show_frame("Data_Visualization"), height = 2, width = 16)
        button_data_management_menu = Button(self, text="Data Management", command=lambda: controller.show_frame("Data_Management"), height = 2, width = 16)
        button_analysis_menu = Button(self, text="Analysis", command=lambda: controller.show_frame("Analysis"), height = 2, width = 16)
        button_help_menu = Button(self, text="Help", command=lambda: controller.show_frame("Help"), height = 2, width = 16)
        button_about_menu = Button(self, text="About", command=lambda: controller.show_frame("About"), height = 2, width = 16)

        button_research_assistant_menu.pack()
        button_research_assistant_menu.place(x = 0, y = 50)

        button_signal_classification_menu.pack()
        button_signal_classification_menu.place(x = 150, y = 50)

        button_data_management_menu.pack()
        button_data_management_menu.place(x = 300, y = 50)

        button_analysis_menu.pack()
        button_analysis_menu.place(x = 450, y = 50)

        button_help_menu.pack()
        button_help_menu.place(x = 600, y = 50)

        button_about_menu.pack()
        button_about_menu.place(x = 750, y = 50)
        '''
        load = Image.open("/Users/chulehou/Documents/Capstone_Mizzou/UI Design/Application_Home.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=150, y=200)
        '''
class Research_Assistant(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label_research_assistant_title = Label(self, text="Research Assistant", font=controller.title_font)
        label_research_assistant_title.pack(side="top", fill="x", pady=10)
        button_research_assistant_back = Button(self, text="Back to the home page", command=lambda: controller.show_frame("Home_Page"), height = 2, width = 16)
        button_research_assistant_back.pack()

class Data_Visualization(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label_data_visualization_title = Label(self, text="Data Visualization", font=controller.title_font)
        label_data_visualization_title.pack(side="top", fill="x", pady=10)

        button_individual_risk = Button(self, text="Age Visualization", command=lambda: controller.show_frame("Age_Visualization"), height = 2, width = 22)
        button_revised_classification = Button(self, text="Weight Visualization", command=lambda: controller.show_frame("Weight_Visualization"), height = 2, width = 22)
        button_accuracy_report = Button(self, text="BMI Visualization", command=lambda: controller.show_frame("BMI_Visualization"), height = 2, width = 22)
        button_signal_classification_back = Button(self, text="Back to the home page", command=lambda: controller.show_frame("Home_Page"), height = 2, width = 22)
        
        button_individual_risk.pack()
        button_individual_risk.place(x = 50, y = 50)

        button_revised_classification.pack()
        button_revised_classification.place(x = 255, y = 50)

        button_accuracy_report.pack()
        button_accuracy_report.place(x = 460, y = 50)

        button_signal_classification_back.pack()
        button_signal_classification_back.place(x = 665, y = 50)
        '''
        load = Image.open("/Users/chulehou/Documents/Capstone_Mizzou/UI Design/data_visualization.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=150, y=200)
        '''
class Data_Management(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label = Label(self, text="Data Management", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button_import = Button(self, text = "Import", command = lambda: controller.show_frame("Import"), height = 2, width = 22)
        button_query = Button(self, text = "Query", command = lambda: controller.show_frame("Query"), height = 2, width = 22)
        button_delete = Button(self, text = "Delete", command = lambda: controller.show_frame("Delete"), height = 2, width = 22)
        button_dm_back = Button(self, text = "Back to the home page", command=lambda: controller.show_frame("Home_Page"), height = 2, width = 22)

        button_import.pack()
        button_import.place(x = 50, y = 50)

        button_query.pack()
        button_query.place(x = 255, y = 50)
        
        button_delete.pack()
        button_delete.place(x = 460, y = 50)

        button_dm_back.pack()
        button_dm_back.place(x = 665, y = 50)

        load = Image.open("/Users/chulehou/Documents/Capstone_Mizzou/UI Design/Navicat.png")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=150, y=200)

class Analysis(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label_analysis_title = Label(self, text="Analysis", font=controller.title_font)
        label_analysis_title.pack(side="top", fill="x", pady=10)
        
        button_time_series_review = Button(self, text = "Individual Classification", command = lambda: controller.show_frame("Individual_Classification"), height = 2, width = 16)
        button_cross_analysis = Button(self, text = "Cross Analysis", command = lambda: controller.show_frame("Cross_Analysis"), height = 2, width = 16)
        button_analysis_back = Button(self, text="Back to the home page", command=lambda: controller.show_frame("Home_Page"), height = 2, width = 16)
        
        button_time_series_review.pack()
        button_time_series_review.place(x = 230, y = 50)

        button_cross_analysis.pack()
        button_cross_analysis.place(x = 380, y = 50)

        button_analysis_back.pack()
        button_analysis_back.place(x = 530, y = 50)


class Help(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label_help_title = Label(self, text="Help", font=controller.title_font)
        label_help_title.pack(side="top", fill="x", pady=10)
        
        button_about_ra = Button(self, text = "About RA", command = lambda: controller.show_frame("About_RA"), height = 2, width = 22)
        button_cnn_parameters = Button(self, text = "CNN Parameters", command = lambda: controller.show_frame("CNN_Parameters"), height = 2, width = 22)
        button_medical = Button(self, text = "Medical", command = lambda: controller.show_frame("Medical"), height = 2, width = 22)
        button_help_back = Button(self, text="Back to the home page", command=lambda: controller.show_frame("Home_Page"), height = 2, width = 22)
        
        button_about_ra.pack()
        button_about_ra.place(x = 50, y = 50)

        button_cnn_parameters.pack()
        button_cnn_parameters.place(x = 255, y = 50)

        button_medical.pack()
        button_medical.place(x = 460, y = 50)

        button_help_back.pack()
        button_help_back.place(x = 665, y = 50)

class About(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label_about_title = Label(self, text="About", font=controller.title_font)
        label_about_title.pack(side="top", fill="x", pady=10)

        button_about_back = Button(self, text="Back to the home page", command=lambda: controller.show_frame("Home_Page"), height = 2, width = 16)
        button_about_back.pack()
        
#Subpages of Data Visualization
class Age_Visualization(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label_age_visualization_title = Label(self, text="Age Visualization", font=controller.title_font)
        label_age_visualization_title.pack(side="top", fill="x", pady=10)

        button_age_visualization_update = Button(self, text="Update", height = 2, width = 16)
        button_age_visualization_update.pack()
        button_age_visualization_update.place(x = 370, y = 530)

        button_age_visualization_back = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Data_Visualization"), height = 2, width = 16)
        button_age_visualization_back.pack()
        button_age_visualization_back.place(x = 370, y = 580)

class Weight_Visualization(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label_weight_visualization_title = Label(self, text="Weight Visualization", font=controller.title_font)
        label_weight_visualization_title.pack(side="top", fill="x", pady=10)

        button_weight_visualization_update = Button(self, text="Update", height = 2, width = 16)
        button_weight_visualization_update.pack()
        button_weight_visualization_update.place(x = 370, y = 530)

        button_weight_visualization_back = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Data_Visualization"), height = 2, width = 16)
        button_weight_visualization_back.pack()
        button_weight_visualization_back.place(x = 370, y = 580)
        
class BMI_Visualization(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label_bmi_visualization_title = Label(self, text="Gender Visualization", font=controller.title_font)
        label_bmi_visualization_title.pack(side="top", fill="x", pady=10)

        button_bmi_visualization_update = Button(self, text="Update", height = 2, width = 16)
        button_bmi_visualization_update.pack()
        button_bmi_visualization_update.place(x = 370, y = 530)

        button_bmi_visualization_back = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Data_Visualization"), height = 2, width = 16)
        button_bmi_visualization_back.pack()   
        button_bmi_visualization_back.place(x = 370, y = 580)
  
#Subpages of Data Management
#Import 
class Import(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label_import_title = Label(self, text="Import", font=controller.title_font)
        label_import_title.pack(side="top", fill="x", pady=10)
        label_new_person = Label(self, text="New Person", font=controller.title_font)
        label_new_person.pack(side="top", fill="x", pady=15)
        #Label of name
        label_name = Label(self, text="Name")
        label_name.pack
        label_name.place(x = 220, y = 100)
        #Entry name
        entry_name = Entry(self, bd=1)
        entry_name.pack
        entry_name.focus_set()
        entry_name.place(x = 400, y = 100)
        #Label of height
        label_height = Label(self, text="Height(centimeters)")
        label_height.pack
        label_height.place(x = 220, y = 130)
        #entry height
        entry_height = Entry(self, bd=1)
        entry_height.pack
        entry_height.place(x = 400, y = 130)
        #Label of weight
        label_weight = Label(self, text="Weight(Kilograms)")
        label_weight.pack
        label_weight.place(x = 220, y = 160)
        #entry weight
        entry_weight = Entry(self, bd=1)
        entry_weight.pack
        entry_weight.place(x = 400, y = 160)
        #Label of age
        label_age = Label(self, text="Age")
        label_age.pack
        label_age.place(x = 220, y = 190)
        #entry age
        entry_age = Entry(self, bd=1)
        entry_age.pack
        entry_age.place(x = 400, y = 190)
        #Label of gender
        label_gender = Label(self, text="Gender")
        label_gender.pack
        label_gender.place(x = 220, y = 220)
        #entry gender
        gender = StringVar() 
        gender_choosen = ttk.Combobox(self, width = 18, textvariable = gender) 
        #Adding combobox drop down list 
        gender_choosen['values'] = ('MALE',  
                                                'FEMALE') 
        gender_choosen.place(x = 400, y = 220) 
        gender_choosen.current()
        #Label of blood pressure high
        label_blood_pressure_high = Label(self, text="Blood Pressure_high(mmHg)")
        label_blood_pressure_high.pack
        label_blood_pressure_high.place(x = 220, y = 250)
        #entry blood pressure high
        entry_blood_pressure_high = Entry(self, bd=1)
        entry_blood_pressure_high.pack
        entry_blood_pressure_high.place(x = 400, y = 250)
        #Label of blood pressure low
        label_blood_pressure_low = Label(self, text="Blood Pressure_low(mmHg)")
        label_blood_pressure_low.pack
        label_blood_pressure_low.place(x = 220, y = 280)
        #entry blood pressure low
        entry_blood_pressure_low = Entry(self, bd=1)
        entry_blood_pressure_low.pack
        entry_blood_pressure_low.place(x = 400, y = 280)
        #Label of hypertension
        label_hypertension = Label(self, text="Hypertension")
        label_hypertension.pack
        label_hypertension.place(x = 220, y = 310)
        #entry hypertension
        #Hypertension chose
        hypertension = StringVar() 
        hypertension_choosen = ttk.Combobox(self, width = 18, textvariable = hypertension) 
        # Adding combobox drop down list 
        hypertension_choosen['values'] = ('YES',  
                                                'NO') 
        hypertension_choosen.place(x = 400, y = 310) 
        hypertension_choosen.current()
        #Label of ground truth
        label_ground_truth = Label(self, text="Has Ground Truth Data")
        label_ground_truth.pack
        label_ground_truth.place(x = 220, y = 340)
        #Ground truth choose 
        ground_truth = StringVar() 
        ground_truth_choosen = ttk.Combobox(self, width = 18, textvariable = ground_truth) 
        # Adding combobox drop down list 
        ground_truth_choosen['values'] = ('YES',  
                                                'NO') 
        ground_truth_choosen.place(x = 400, y = 340) 
        ground_truth_choosen.current()
        #Label of ethnicity
        label_ethnicity = Label(self, text="Ethnicity")
        label_ethnicity.pack
        label_ethnicity.place(x = 220, y = 370)
        #Ethnicity choose
        ethnicity = StringVar() 
        ethnicitychoosen = ttk.Combobox(self, width = 18, textvariable = ethnicity) 
        #Adding combobox drop down list 
        ethnicitychoosen['values'] = ('African',  
                                    'Aboriginal American', 
                                    'Aboriginal Australian', 
                                    'East-Asian', 
                                    'Caucasian', 
                                    'Indian', 
                                    'Latinx', 
                                    'Middle-Eastern', 
                                    'Multi-Ethnic', 
                                    'Pacific-Islander') 
        ethnicitychoosen.place(x = 400, y = 370) 
        ethnicitychoosen.current() 
        #Label of upload the signal data
        label_upload_data = Label(self, text="Upload the Signal Data")
        label_upload_data.pack
        label_upload_data.place(x = 220, y = 400)
        #entry signal data file path
        pathtext = StringVar()
        entry_signal_file_path = Entry(self, textvariable=pathtext, bd=1, width = 50)
        entry_signal_file_path.pack
        entry_signal_file_path.place(x = 220, y = 430)
        #Set the CSV file path in entry
        def inputfilepath():
            temp_file = filedialog.askopenfilename()
            print(temp_file)
            pathtext.set(temp_file)
            gdb.convert_csv(self, temp_file)

        button_upload_data_to_db = Button(self, text="Upload Data to Database", height = 2, width = 25, command = lambda: [self.dbimport(entry_name.get().strip(),
                                                                                                                                         entry_weight.get().strip(),
                                                                                                                                         entry_weight.get().strip(),
                                                                                                                                         entry_age.get().strip(),
                                                                                                                                         entry_blood_pressure_high.get().strip(),
                                                                                                                                         entry_blood_pressure_low.get().strip(),
                                                                                                                                         ethnicitychoosen.get().strip(),
                                                                                                                                         gender_choosen.get().strip(),
                                                                                                                                         hypertension_choosen.get().strip(),
                                                                                                                                         ground_truth_choosen.get().strip()
                                                                                                                                         ),
                                                                                                                            self.clear(entry_name, 
                                                                                                                            entry_height, 
                                                                                                                            entry_weight, 
                                                                                                                            entry_age,
                                                                                                                            entry_blood_pressure_high, 
                                                                                                                            entry_blood_pressure_low,
                                                                                                                            ethnicitychoosen,
                                                                                                                            gender_choosen,
                                                                                                                            hypertension_choosen,
                                                                                                                            ground_truth_choosen)])
        button_upload_data_to_db.pack()
        button_upload_data_to_db.place(x = 340, y = 530)

        button_import_back = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Data_Management"), height = 2, width = 25)
        button_import_back.pack()
        button_import_back.place(x = 340, y = 580)

        button_choose_data = Button(self, text="Choose the Signal Data", height = 2, width = 25, command = inputfilepath)
        button_choose_data.pack()
        button_choose_data.place(x = 340, y = 480)
    '''
    def dbimportcsv(self,)
        gdb.db
    
    def dbimport(self, name, height, weight, age, bloodh, bloodl, ethnicity, gender, hypertension, ground_truth):
        gdb.dbimport(self, name, height, weight, age, bloodh, bloodl, ethnicity, gender, hypertension, ground_truth)
    
    def clear(self,entry_name, entry_height, entry_weight, entry_age,entry_blood_pressure_high, entry_blood_pressure_low,ethnicitychoosen,gender_choosen,hypertension_choosen,ground_truth_choosen):
        gdb.dbimportclear(self,entry_name, entry_height, entry_weight, entry_age,entry_blood_pressure_high, entry_blood_pressure_low,ethnicitychoosen,gender_choosen,hypertension_choosen,ground_truth_choosen)
    '''
#Query
class Query(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label_query_title = Label(self, text="Query", font=controller.title_font)
        label_query_title.pack(side="top", fill="x", pady=10)

        label_input_id_to_quert = Label(self, text="Input the id to query", font=controller.text_font)
        label_input_id_to_quert.pack()
        label_input_id_to_quert.place(x = 350, y = 50)
        #entry subject id
        entry_subject_id = Entry(self, bd=1)
        entry_subject_id.pack
        entry_subject_id.place(x = 100, y = 100, height = 35, width = 400)

        button_search = Button(self, text="Search", height = 2, width = 25, command = lambda: [self.dbsearch(entry_subject_id.get().strip()),self.clear(entry_subject_id)])
        button_search.pack()
        button_search.place(x = 500, y = 100)

        #Treeview widget
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
    '''
    def dbsearch(self, searchid):
        gdb.dbsearch(self, searchid)
    
    def clear(self,entry_subject_id):
        gdb.dbsearchclear(self,entry_subject_id)
    '''
#Delete
class Delete(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label_delete_title = Label(self, text="Delete", font=controller.title_font)
        label_delete_title.pack(side="top", fill="x", pady=10)

        label_input_id_to_delete = Label(self, text="Input the id to delete", font=controller.text_font)
        label_input_id_to_delete.pack()
        label_input_id_to_delete.place(x = 350, y = 50)

        entry_id_to_delete = Entry(self, bd=1)
        entry_id_to_delete.pack
        entry_id_to_delete.place(x = 100, y = 100, height = 35, width = 400)

        button_delete = Button(self, text="Delete", height = 2, width = 25, command = lambda:[self.dbdelete(entry_id_to_delete.get().strip()),self.clear(entry_id_to_delete)])
        button_delete.pack()
        button_delete.place(x = 500, y = 100)

        button_delete_back = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Data_Management"), height = 2, width = 16)
        button_delete_back.pack()
        button_delete_back.place(x = 375, y = 500)
    '''
    def dbdelete(self, inputid):
        gdb.dbdelete(self, inputid)

    def clear(self,entry_id_to_delete):
        gdb.dbdeleteclear(self,entry_id_to_delete)
    '''
#Subpages of Analysis
class Individual_Classification(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label_individual_classification_title = Label(self, text="Individual Classification", font=controller.title_font)
        label_individual_classification_title.pack(side="top", fill="x", pady=10)

        #entry subject id
        self.entry_subject_id = Entry(self, bd=1)
        self.entry_subject_id.pack
        self.entry_subject_id.place(x = 100, y = 50, height = 35, width = 400)

        button_search = Button(self, text="Search", height = 2, width = 25, command = lambda: [self.dbsearch(), self.clear()])
        button_search.pack()
        button_search.place(x = 500, y = 50)

        #Treeview widget
        self.treeAddressList = ttk.Treeview(self,
                                       columns=('c1', 'c2', 'c3','c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10', 'c11'),
                                       show="headings",
                                       height = 3)

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
        self.treeAddressList.place(x = 20, y = 150)

        button_individual_classification_back = Button(self, text="Determine Risk?", height = 2, width = 16)
        button_individual_classification_back.pack()
        button_individual_classification_back.place(x = 375, y = 250)

        label_result = Label(self, text="Results", font=controller.title_font)
        label_result.pack()
        label_result.place(x = 400, y =300)

        label_result = Label(self, text="Heart Failure Risk Percent", font=controller.title_font)
        label_result.pack()
        label_result.place(x = 330, y =350)

        entry_risk_percentile = Entry(self, bd=1, width = 10)
        entry_risk_percentile.pack
        entry_risk_percentile.place(x = 400, y = 400)

        button_individual_classification_back = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Analysis"), height = 2, width = 16)
        button_individual_classification_back.pack()
        button_individual_classification_back.place(x = 375, y = 550)
    '''
    def dbsearch(self):
        self.searchid = self.entry_subject_id.get().strip()
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
        self.entry_subject_id.delete(0,END)
    '''
class Cross_Analysis(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label_cross_analysis_title = Label(self, text="Cross Analysis", font=controller.title_font)
        label_cross_analysis_title.pack(side="top", fill="x", pady=10)
        button_cross_analysisi_back = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Analysis"), height = 2, width = 16)
        button_cross_analysisi_back.pack()

#Subpages of Help
class About_RA(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label_about_ra_title = Label(self, text="About RA", font=controller.title_font)
        label_about_ra_title.pack(side="top", fill="x", pady=10)
        button_about_ra_back = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Help"), height = 2, width = 16)
        button_about_ra_back.pack()

class CNN_Parameters(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label_cnn_parameters_title = Label(self, text="CNN Parameters", font=controller.title_font)
        label_cnn_parameters_title.pack(side="top", fill="x", pady=10)
        button_cnn_parameters_back = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Help"), height = 2, width = 16)
        button_cnn_parameters_back.pack()

class Medical(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        label_medical_title = Label(self, text="Medical", font=controller.title_font)
        label_medical_title.pack(side="top", fill="x", pady=10)
        button_medical_back = Button(self, text="Back to the last page", command=lambda: controller.show_frame("Help"), height = 2, width = 16)
        button_medical_back.pack()

if __name__ == "__main__":
    app = ghostriders()
    app.mainloop()