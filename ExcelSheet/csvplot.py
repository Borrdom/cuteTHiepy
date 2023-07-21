import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg,NavigationToolbar2QT
import os
from PyQt5 import QtCore, QtWidgets


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self,fig,ax,canvas, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        sc=canvas
        self.fig=fig
        
        self.ax=ax
        self.canvas=canvas

        # Create buttons
        self.button_x_limits = QtWidgets.QPushButton("Adjust X Limits")
        self.button_y_limits = QtWidgets.QPushButton("Adjust Y Limits")
        self.button_x_ticks = QtWidgets.QPushButton("Adjust X Ticks")
        self.button_y_ticks = QtWidgets.QPushButton("Adjust Y Ticks")

        # Create entry boxes
        self.entry_x_limits = QtWidgets.QLineEdit()
        self.entry_y_limits = QtWidgets.QLineEdit()
        self.entry_x_ticks = QtWidgets.QLineEdit()
        self.entry_y_ticks = QtWidgets.QLineEdit()

        # Connect button signals to respective slots
        self.button_x_limits.clicked.connect(self.adjust_x_limits)
        self.button_y_limits.clicked.connect(self.adjust_y_limits)
        self.button_x_ticks.clicked.connect(self.adjust_x_ticks)
        self.button_y_ticks.clicked.connect(self.adjust_y_ticks)

        # Create the toolbar and add it to the layout
        toolbar = NavigationToolbar2QT(sc, self,coordinates=True)
        toolbar.setOrientation(QtCore.Qt.Vertical)
        button_layout = QtWidgets.QVBoxLayout()
        
        

        button_layout.addWidget(self.button_x_limits)
        button_layout.addWidget(self.entry_x_limits)
        button_layout.addWidget(self.button_y_limits)
        button_layout.addWidget(self.entry_y_limits)
        button_layout.addWidget(self.button_x_ticks)
        button_layout.addWidget(self.entry_x_ticks)
        button_layout.addWidget(self.button_y_ticks)
        button_layout.addWidget(self.entry_y_ticks)
        
        plot_layout = QtWidgets.QHBoxLayout()

        plot_layout.addWidget(toolbar)
        plot_layout.addWidget(sc)
        

        main_layout = QtWidgets.QHBoxLayout()
        main_layout.addLayout(button_layout)
        main_layout.addLayout(plot_layout)

        widget = QtWidgets.QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
        self.show()

    def adjust_x_limits(self):
        # Get the x limits from the entry box
        x_limits = self.entry_x_limits.text()
        try:
            x_min, x_max = map(float, x_limits.split(','))
            # Code for adjusting x limits
            self.ax.set_xlim(x_min, x_max)
            self.canvas.draw()
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Invalid Input", "Please enter valid x limits.")

    def adjust_y_limits(self):
        # Get the y limits from the entry box
        y_limits = self.entry_y_limits.text()
        try:
            y_min, y_max = map(float, y_limits.split(','))
            # Code for adjusting y limits
            self.ax.set_ylim(y_min, y_max)
            self.canvas.draw()
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Invalid Input", "Please enter valid y limits.")

    def adjust_x_ticks(self):
        # Get the x ticks from the entry box
        x_ticks = self.entry_x_ticks.text()
        start, end = ax.get_xlim()
        try:
            self.ax.xaxis.set_ticks(np.linspace(start, end, int(x_ticks)))
            self.canvas.draw()
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Invalid Input", "Please enter valid x ticks.")

    def adjust_y_ticks(self):
        # Get the y ticks from the entry box
        y_ticks = self.entry_y_ticks.text()
        start, end = ax.get_ylim()
        try:
            self.ax.yaxis.set_ticks(np.linspace(start, end, int(y_ticks)))
            self.canvas.draw()
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Invalid Input", "Please enter valid y ticks.")




class origin_like:
    def subplots():
        matplotlib.rcParams['mathtext.fontset'] = 'custom'
        matplotlib.rcParams['mathtext.rm'] = 'Calibri'
        matplotlib.rcParams['mathtext.it'] = 'Calibri'
        matplotlib.rcParams['mathtext.bf'] = 'Calibri'
        matplotlib.rcParams['xtick.major.pad']='5'
        matplotlib.rcParams['ytick.major.pad']='5'
        matplotlib.rcParams['axes.linewidth'] = 0.5
        # matplotlib.rcParams["toolbar"] = "toolmanager"
        plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
        
        font = {'weight' : 'normal',
                'size'   : 16,
                'family' : "calibri"}
        plt.rc('font', **font)
        fig=plt.figure(figsize=(4 , 4), dpi = 250)
        axs=fig.add_axes([0.2667,1-0.2042-0.5017,0.5908,0.5017])
        return fig,axs
    def set_xlabel(ax,xlabel1,xunit1=None):
        ax.set_xlabel(f'$\mathrm{{{xlabel1}}}$ / $\mathrm{{{xunit1}}}$') if xunit1 is not None else ax.set_xlabel(f'$\mathrm{{{xlabel1}}}$') 
    def set_ylabel(ax,ylabel1,yunit1=None):
        ax.set_ylabel(f'$\mathrm{{{ylabel1}}}$ \n / $\mathrm{{{yunit1}}}$',rotation=0,loc="top",linespacing=1.5) if yunit1 is not None else ax.set_ylabel(f'$\mathrm{{{ylabel1}}}$',linespacing=1.5)
    def plot(ax,x,y,Formatstring,label=None,order=1):
        ax.plot(x,y,Formatstring , zorder=order,linewidth = 1.5,label=label,markersize=5, markeredgecolor='k',markeredgewidth=0.5)
    def set_ticks(ax,x0=None,x1=None,y0=None,y1=None):
        ax.tick_params(labelbottom=True, labeltop=False, labelleft=True, labelright=False, bottom=True, top=True, left=True, right=True, direction="in",length=4, width=0.5)
        if x0 is not None: ax.axis([x0, x1, y0, y1]) 
        start, end = ax.get_xlim()
        ax.xaxis.set_ticks(np.linspace(start, end, 5))
        start, end = ax.get_ylim()
        ax.yaxis.set_ticks(np.linspace(start, end, 5))




# df=pd.read_csv("Werte2.txt", encoding = "utf-8", sep=",", header=None)
i=0
dfs=[]
while True:
    i+=1
    try:
        dfs.append(pd.read_excel("Werte.xlsx", sheet_name=f"Series_plot {i}",header=None))
    except:
        break


fig, ax = origin_like.subplots()
# Plotten
xlabel=dfs[0].values[0,0]
ylabel=dfs[0].values[0,1]
print(xlabel)
print(ylabel)
for df in dfs:
    x=df.values[3:,0]
    for i in range(1,df.columns.size):
        # x achse auslesen
        legend=df.values[1,i]
        Formatstring=df.values[2,i]
        y=df.values[3:,i]
            # Plotten mit Formatierung
        origin_like.plot(ax,x.astype(float),y.astype(float), Formatstring, label=legend)            
        origin_like.set_xlabel(ax,xlabel)
        origin_like.set_ylabel(ax,ylabel)
        origin_like.set_ticks(ax)
    # app = QApplication(sys.argv)
import sys
app = QtWidgets.QApplication(sys.argv)
canvas=FigureCanvasQTAgg(fig)
canvas.setFixedSize(1000,1000)
canvas.draw()
matplotlib_gui = MainWindow(fig,ax,canvas)


app.exec_()
