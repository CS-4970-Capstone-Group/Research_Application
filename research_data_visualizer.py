import tkinter
import research_dbms
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implementing the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import numpy as np

#Created additional arrays to serve as the basis for the input to the pie graph
age = [0,0,0,0,0,0,0,0,0,0,0]
labels = ['0-10 years', '11-20 years', '21-30 years', '31-40 years', '41-50 years', '51-60 years', '61-70 years',
          '71-80 years', '81-90 years', '91-100 years', '101-110 years']
root = tkinter.Tk()
root.wm_title("Embedding in Tk")

#Call to the Research_DBMS class followed by its respective read_risk_and_age method
db = research_dbms.Research_DBMS()

#Grabbing data from data base as a multidimensional array: first array is a list of ages, second is heart failure
data = db.read_risk_and_age() #the data itself are just random entries I created in the db I'm working with
ages = np.asarray(data[0],dtype="int")
group=10; #Counter used for separating the data with respect to age groups
a = 0;
hf_group = 0

#Going through and filtering out only those ages that are associated with heart failure and getting a count of each
for i in range(len(age)):
    for j in range(len(data[0])):
        if data[1][j] == 1 and ages[j] <= group and ages[j] > group - 10:
            age[a] += 1
            hf_group += 1
    group += 10;
    a += 1

#Turning the counts into percentages of the dataset as input to the pie graph
for k in range(len(age)):
    age[k] = age[k]/hf_group * 100
    if age[k] == 0:
        labels[k] = '';

print(age) #just to see the data for testing purposes

fig = Figure(figsize=(5, 4), dpi=100)
#fig.add_subplot(111).plot(data[0], data[1])
#fig.add_subplot(111).scatter(data[0], data[1])

#Plotting of the pie graph based on the age array derived from the data pulled from the database
fig, ax = plt.subplots()
#Not sure how to avoid the display of 0% for those groups with no instances of heart failure.
ax.pie(age,labels=labels, startangle=90, autopct='%1.1f%%',)
ax.axis('equal')

canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#Toolbar relates to ability to act on the graph, whether it be to save it or have a different view of it.
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)

#You could probably ignore the rest as it is just a part of the tk frame I used to test out the pie graph

def _quit():
    root.quit()
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.