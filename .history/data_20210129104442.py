import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
df = pd.read_excel('Climat.xlsx', skiprows = 2,  nrows= 32, usecols = 'C:O')
df = df.drop(df.index[0])
df.drop(df.columns[0], axis=1, inplace=True)


def config_plot():
    fig, ax = plt.subplots()
    ax.set(xlabel='time (s)', ylabel='voltage (mV)',
           title='Graph One')
    return (fig, ax)

class matplotlibSwitchGraphs:
    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)
        self.fig, self.ax = config_plot()
        self.graphIndex = 0
        self.canvas = FigureCanvasTkAgg(self.fig, self.master)  
        self.config_window()
        self.draw_graph('janvier')
        self.frame.pack(expand=YES, fill=BOTH)

    def config_window(self):
        self.canvas.mpl_connect("key_press_event", self.on_key_press)
        toolbar = NavigationToolbar2Tk(self.canvas, self.master)
        toolbar.update()
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.button = Button(self.master, text="Quit", command=self._quit)
        self.button.pack(side=BOTTOM)
        self.button_back = Button(self.master, text="Graphique précédent", command=self.back_graph)
        self.button_back.pack(side=BOTTOM)
        self.button_next = Button(self.master, text="Graphique suivant", command=self.next_graph)
        self.button_next.pack(side=BOTTOM)
    def draw_graph(self, month):
        self.ax.clear()
        self.ax.plot(df[month])
        self.ax.set(title=month)
        self.canvas.draw()

    def on_key_press(event):
        key_press_handler(event, self.canvas, toolbar)

    def _quit(self):
        self.master.quit() 

    def next_graph(self):
        if self.graphIndex == 0:
            self.draw_graph('février')
            self.graphIndex = 1
        elif self.graphIndex == 1:
            self.draw_graph('mars')
            self.graphIndex = 2
        elif self.graphIndex == 2:
            self.draw_graph('avril')
            self.graphIndex = 3
        elif self.graphIndex == 3:
            self.draw_graph('mai')
            self.graphIndex = 4
        elif self.graphIndex == 4:
            self.draw_graph('juin')
            self.graphIndex = 5
        elif self.graphIndex == 5:
            self.draw_graph('juillet')
            self.graphIndex = 6
        elif self.graphIndex == 6:
            self.draw_graph('août')
            self.graphIndex = 7
        elif self.graphIndex == 7:
            self.draw_graph('septembre')
            self.graphIndex = 8
        elif self.graphIndex == 8:
            self.draw_graph('octobre')
            self.graphIndex = 9
        elif self.graphIndex == 9:
            self.draw_graph('novembre')
            self.graphIndex = 10
        elif self.graphIndex == 10:
            self.draw_graph('décembre')
            self.graphIndex = 11
        elif self.graphIndex == 11:
            self.draw_graph('janvier')
            self.graphIndex = 0

    def back_graph(self):
        if self.graphIndex == 0:
            self.draw_graph('décembre')
            self.graphIndex = 11
        elif self.graphIndex == 11:
            self.draw_graph('novembre')
            self.graphIndex = 10
        elif self.graphIndex == 10:
            self.draw_graph('octobre')
            self.graphIndex = 9
        elif self.graphIndex == 9:
            self.draw_graph('septembre')
            self.graphIndex = 8
        elif self.graphIndex == 8:
            self.draw_graph('août')
            self.graphIndex = 7
        elif self.graphIndex == 7:
            self.draw_graph('juillet')
            self.graphIndex = 6
        elif self.graphIndex == 6:
            self.draw_graph('juin')
            self.graphIndex = 5
        elif self.graphIndex == 5:
            self.draw_graph('mai')
            self.graphIndex = 4
        elif self.graphIndex == 4:
            self.draw_graph('avril')
            self.graphIndex = 3
        elif self.graphIndex == 3:
            self.draw_graph('mars')
            self.graphIndex = 2
        elif self.graphIndex == 2:
            self.draw_graph('février')
            self.graphIndex = 1
        elif self.graphIndex == 1:
            self.draw_graph('janvier')
            self.graphIndex = 0


def main():
    root = Tk()
    matplotlibSwitchGraphs(root)
    root.mainloop()

def show_graph():
    main()

fenetre = Tk()
fenetre.title("Data tp 1")
fenetre.geometry('800x800')
canvas=Canvas(fenetre,bg='#FFFFFF',width=800,height=800,scrollregion=(0,0,800,800))
hbar=Scrollbar(fenetre,orient=HORIZONTAL)
hbar.pack(side=BOTTOM,fill=X)
hbar.config(command=canvas.xview)
vbar=Scrollbar(fenetre,orient=VERTICAL)
vbar.pack(side=RIGHT,fill=Y)
vbar.config(command=canvas.yview)
canvas.config(width=800,height=800)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
canvas.pack(side=LEFT,expand=True,fill=BOTH)

for index, column in enumerate(df):
    labelMonth = Label(fenetre, text="Mois : "+str(column),background="white",foreground="black")
    labelMean = Label(fenetre, text="Moyenne : "+str(df[column].mean()),background="white",foreground="black")
    labelStd = Label(fenetre, text="Ecart type : "+str(df[column].std()),background="white",foreground="black")
    labelMin = Label(fenetre, text="Minimum : "+str(df[column].min()),background="white",foreground="black")
    labelMax = Label(fenetre, text="Maximum : "+str(df[column].max()),background="white",foreground="black")


    canvas.create_text(50,(index*120)+0,fill="black",font="Times 10",
                        text="Mois : "+str(column))
    canvas.create_text(50,(index*120)+20,fill="black",font="Times 10",
                            text="Moyenne : "+str(df[column].mean()))
    canvas.create_text(50,(index*120)+40,fill="black",font="Times 10",
    text="Ecart type : "+str(df[column].std()))
    canvas.create_text(50,(index*120)+60,fill="black",font="Times 10",
    text="Minimum : "+str(df[column].min()))
    canvas.create_text(50,(index*120)+80,fill="black",font="Times 10",
    text="Maximum : "+str(df[column].max()))









b = Button(fenetre, text="Afficher les graphiques", width=10, command=show_graph,background="white",foreground="black",activebackground="white",activeforeground="black")
b.place(x=0, y=20, anchor="nw", width=150, height=30)

fenetre.mainloop()