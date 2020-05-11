import seaborn
import matplotlib.pyplot as plt
from research_dbms import Research_DBMS as db
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
import sys
import os

def piegraph(sizes = [], label = ['50-55','55-60','60-65','65-70']):
    explode = (0, 0.1, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=label, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')

    plt.savefig('age_distribution.png')
    

def refresh():
    age_distribution()

    load = Image.open("age_distribution.png")
    render = ImageTk.PhotoImage(load)
    img = Label(self, image=render)
    img.image = render
    img.place(x=100, y=50)
    print('use1')

def piegraph_weight(sizes = [], label = ['60-70','70-80','80-90','Over 90']):
    explode = (0, 0.1, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=label, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')

    plt.savefig('weight_distribution.png')

def refresh():
    age_distribution()
    
    load = Image.open("weight_distribution.png")
    render = ImageTk.PhotoImage(load)
    img = Label(self, image=render)
    img.image = render
    img.place(x=100, y=50)
    print('use1')

def piegraph_bmi(sizes = [], label = ['Underweight','Normal or Healthy','Overweight','Obese']):
    explode = (0, 0.1, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=label, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')

    plt.savefig('bmi_distribution.png')




