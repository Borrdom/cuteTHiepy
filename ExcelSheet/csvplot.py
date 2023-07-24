import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg,NavigationToolbar2QT
import os
from PyQt5 import QtCore, QtWidgets
import sys
from matplotlib.ticker import AutoLocator
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import sys
import mpltern


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self,fig,ax,canvas,title, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle(title)
        sc=canvas
        self.fig=fig
        
        self.ax=ax
        self.canvas=canvas

        # Create buttons
        self.button_x_limits = QtWidgets.QPushButton("Adjust X Limits")
        self.button_y_limits = QtWidgets.QPushButton("Adjust Y Limits")
        self.button_z_limits = QtWidgets.QPushButton("Adjust Z Limits")
        self.button_reset_ticks = QtWidgets.QPushButton("Reset Ticks")
        self.button_rotate_vertical = QtWidgets.QPushButton("Rotate y-Axis vertical")
        self.button_rotate_horizontal = QtWidgets.QPushButton("Rotate y-Axis horizontal")

        # Create entry boxes
        self.entry_x_min = QtWidgets.QLineEdit()
        self.entry_x_max = QtWidgets.QLineEdit()
        self.entry_x_last = QtWidgets.QLineEdit()
        self.entry_x_ticks = QtWidgets.QLineEdit()

        self.entry_y_min = QtWidgets.QLineEdit()
        self.entry_y_max = QtWidgets.QLineEdit()
        self.entry_y_last = QtWidgets.QLineEdit()
        self.entry_y_ticks = QtWidgets.QLineEdit()
        #Create x limit info

        self.entry_z_min = QtWidgets.QLineEdit()
        self.entry_z_max = QtWidgets.QLineEdit()
        self.entry_z_last = QtWidgets.QLineEdit()
        self.entry_z_ticks = QtWidgets.QLineEdit()
        
        self.xmin_label=QtWidgets.QLabel("xmin")
        self.xmax_label=QtWidgets.QLabel("xmax")
        self.xlast_label=QtWidgets.QLabel("xend")
        self.nxticks_label=QtWidgets.QLabel("nxticks")
        #Create y limit info
        self.ymin_label=QtWidgets.QLabel("ymin")
        self.ymax_label=QtWidgets.QLabel("ymax")
        self.ylast_label=QtWidgets.QLabel("yend")
        self.nyticks_label=QtWidgets.QLabel("nyticks")

        self.zmin_label=QtWidgets.QLabel("zmin")
        self.zmax_label=QtWidgets.QLabel("zmax")
        self.zlast_label=QtWidgets.QLabel("zend")
        self.nzticks_label=QtWidgets.QLabel("nzticks")

        self.xy_pos=QtWidgets.QLabel("x= ; y=")
        

        # Connect button signals to respective slots
        self.button_x_limits.clicked.connect(self.adjust_x_limits)
        self.button_y_limits.clicked.connect(self.adjust_y_limits)
        self.button_z_limits.clicked.connect(self.adjust_z_limits)
        self.button_reset_ticks.clicked.connect(self.reset_ticks)
        self.button_rotate_vertical.clicked.connect(self.vertical_ylabel)
        self.button_rotate_horizontal.clicked.connect(self.horizontal_ylabel)



        #Create Button Layout
        button_layout = QtWidgets.QVBoxLayout()

        #adjust xlim labels 
        xlim_label_layout = QtWidgets.QHBoxLayout()
        xlim_label_layout.addWidget(self.xmin_label)
        xlim_label_layout.addWidget(self.xmax_label)
        xlim_label_layout.addWidget(self.xlast_label)
        xlim_label_layout.addWidget(self.nxticks_label)
        button_layout.addLayout(xlim_label_layout)
        #adjust xlim entries
        xlim_layout = QtWidgets.QHBoxLayout()
        xlim_layout.addWidget(self.entry_x_min)
        xlim_layout.addWidget(self.entry_x_max)
        xlim_layout.addWidget(self.entry_x_last)
        xlim_layout.addWidget(self.entry_x_ticks)
        button_layout.addLayout(xlim_layout)
        #adjust xlim button
        button_layout.addWidget(self.button_x_limits)
        
        #adjust ylim labels 
        ylim_label_layout = QtWidgets.QHBoxLayout()
        ylim_label_layout.addWidget(self.ymin_label)
        ylim_label_layout.addWidget(self.ymax_label)
        ylim_label_layout.addWidget(self.ylast_label)
        ylim_label_layout.addWidget(self.nyticks_label)
        button_layout.addLayout(ylim_label_layout)
        #adjust ylim entries
        ylim_layout = QtWidgets.QHBoxLayout()
        ylim_layout.addWidget(self.entry_y_min)
        ylim_layout.addWidget(self.entry_y_max)
        ylim_layout.addWidget(self.entry_y_last)
        ylim_layout.addWidget(self.entry_y_ticks)
        button_layout.addLayout(ylim_layout)
        #adjust ylim button
        button_layout.addWidget(self.button_y_limits)


        #adjust zlim labels 
        zlim_label_layout = QtWidgets.QHBoxLayout()
        zlim_label_layout.addWidget(self.zmin_label)
        zlim_label_layout.addWidget(self.zmax_label)
        zlim_label_layout.addWidget(self.zlast_label)
        zlim_label_layout.addWidget(self.nzticks_label)
        
        if hasattr(self.ax,"taxis"): button_layout.addLayout(zlim_label_layout)
        #adjust ylim entries
        zlim_layout = QtWidgets.QHBoxLayout()
        zlim_layout.addWidget(self.entry_z_min)
        zlim_layout.addWidget(self.entry_z_max)
        zlim_layout.addWidget(self.entry_z_last)
        zlim_layout.addWidget(self.entry_z_ticks)
        if hasattr(self.ax,"taxis"): button_layout.addLayout(zlim_layout)
        #adjust ylim button
        if hasattr(self.ax,"taxis"): button_layout.addWidget(self.button_z_limits)
        #add a reset button
        button_layout.addWidget(self.button_reset_ticks)

        # add rotation
        button_layout.addWidget(self.button_rotate_horizontal)
        button_layout.addWidget(self.button_rotate_vertical)
        button_layout.addWidget(self.xy_pos)
        #Stretch until the end of the layout
        button_layout.addStretch(1)

        # Create the toolbar and add it to the layout
        plot_layout = QtWidgets.QHBoxLayout()
        toolbar = NavigationToolbar2QT(sc, self,coordinates=False)
        toolbar.setOrientation(QtCore.Qt.Vertical)
        plot_layout.addWidget(toolbar)
        plot_layout.addWidget(sc)


        main_layout = QtWidgets.QHBoxLayout()
        main_layout.addLayout(button_layout)
        main_layout.addLayout(plot_layout)
        
        # self.scene = QGraphicsScene(self)
        # self.view = QGraphicsView(self.scene)
        # main_layout.addWidget(self.view)

        widget = QtWidgets.QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

        if hasattr(self.ax,"taxis"):
            pass
        else:
            def update_mouse_coordinates(event):
                if  event.xdata==None or event.ydata==None:
                    self.xy_pos.setText("x=; y=")
                    self.canvas.draw()
                    return
                self.xy_pos.setText(f"x={event.xdata:.4f}; y={event.ydata:.4f}")
                # self.ax.xaxis.set_label_coords(event.x, event.y)
                self.canvas.draw()
            plt.connect('motion_notify_event', update_mouse_coordinates)





        self.show()

    def reset_ticks(self):
        if hasattr(self.ax,"taxis"):
            self.ax.taxis.set_major_locator(AutoLocator())
            self.ax.laxis.set_major_locator(AutoLocator())
            self.ax.raxis.set_major_locator(AutoLocator())
        else: 
            self.ax.xaxis.set_major_locator(AutoLocator())
            self.ax.yaxis.set_major_locator(AutoLocator())
        self.canvas.draw()
        


    def vertical_ylabel(self):
        if hasattr(self.ax,"taxis"):
            pass
        else: 
            self.ax.yaxis.label.set(rotation=90)
            self.ax.yaxis.set_label_coords(-0.15,0.5)
        self.canvas.draw()
    def horizontal_ylabel(self):
        if hasattr(self.ax,"taxis"):
            pass
        else: 
            self.ax.yaxis.label.set(rotation=0)
            self.ax.yaxis.set_label_coords(-0.1,1)
            self.canvas.draw()

    def adjust_x_limits(self):
        # Get the x limits from the entry box
        x_min, x_max = self.entry_x_min.text(),self.entry_x_max.text()
        x_last= self.entry_x_last.text()
        x_ticks = self.entry_x_ticks.text()

        
        try:
            if hasattr(self.ax,"taxis"):
                self.ax.set_tlim(float(x_min), float(x_max))
                self.ax.taxis.set_ticks(np.linspace(float(x_min), float(x_last), int(x_ticks)))
            else:
                self.ax.set_xlim(float(x_min), float(x_max))
                self.ax.xaxis.set_ticks(np.linspace(float(x_min), float(x_last), int(x_ticks)))
            # self.ax.xaxis.set_major_locator(AutoLocator())
            self.canvas.draw()
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Invalid Input", "Please enter valid x limits.")

    def adjust_y_limits(self):
        # Get the y limits from the entry box
        y_min, y_max = self.entry_y_min.text(),self.entry_y_max.text()
        y_last= self.entry_y_last.text()
        y_ticks = self.entry_y_ticks.text()
        try:
            if hasattr(self.ax,"taxis"):
                self.ax.set_llim(float(y_min), float(y_max))
                self.ax.laxis.set_ticks(np.linspace(float(y_min), float(y_last), int(y_ticks)))
            else:
                self.ax.set_ylim(float(y_min), float(y_max))
                self.ax.yaxis.set_ticks(np.linspace(float(y_min), float(y_last) , int(y_ticks)))
            # self.ax.yaxis.set_major_locator(AutoLocator())
            self.canvas.draw()
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Invalid Input", "Please enter valid y limits.")
    def adjust_z_limits(self):
        # Get the y limits from the entry box
        z_min, z_max = self.entry_z_min.text(),self.entry_z_max.text()
        z_last= self.entry_z_last.text()
        z_ticks = self.entry_z_ticks.text()
        try:
            self.ax.set_rlim(float(z_min), float(z_max))
            self.ax.raxis.set_ticks(np.linspace(float(z_min), float(z_last), int(z_ticks)))
            self.canvas.draw()
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Invalid Input", "Please enter valid y limits.")




class origin_like:
    def basic_colors(shorthand="g"):
        if shorthand=="g": return "99CC00"
        if shorthand=="o": return "FF8500"
        if shorthand=="gray": return "666666"
    def subplots(sharex=False):
        matplotlib.rcParams['mathtext.fontset'] = 'custom'
        matplotlib.rcParams['mathtext.rm'] = 'Calibri'
        matplotlib.rcParams['mathtext.it'] = 'Calibri'
        matplotlib.rcParams['mathtext.bf'] = 'Calibri'
        matplotlib.rcParams['xtick.major.pad']='5'
        matplotlib.rcParams['ytick.major.pad']='5'
        matplotlib.rcParams['axes.linewidth'] = 0.5
        # matplotlib.rcParams["toolbar"] = "toolmanager"
        # plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
        
        font = {'weight' : 'normal',
                'size'   : 16,
                'family' : "calibri"}
        plt.rc('font', **font)
        fig=plt.figure(figsize=(4 , 4), dpi = 250)
        
        if sharex :
            ax=fig.add_axes([0.2667,1-0.2042-0.5017,0.5908,0.5017/2]) 
            ax2=fig.add_axes([0.2667,1-0.2042-0.5017,0.5908,0.5017/2])
            ax.get_shared_x_axes().join(ax, ax2) 

        else:
            ax=fig.add_axes([0.2667,1-0.2042-0.5017,0.5908,0.5017])
        ax.tick_params(labelbottom=True, labeltop=False, labelleft=True, labelright=False, bottom=True, top=True, left=True, right=True, direction="in",length=4, width=0.5)
        return fig,ax
    def set_xlabel(ax,xlabel1,xunit1=None):
        ax.set_xlabel(f'$\mathrm{{{xlabel1}}}$ / $\mathrm{{{xunit1}}}$') if xunit1 is not None else ax.set_xlabel(f'$\mathrm{{{xlabel1}}}$') 
    def set_ylabel(ax,ylabel1,yunit1=None):
        ax.set_ylabel(f'$\mathrm{{{ylabel1}}}$ \n / $\mathrm{{{yunit1}}}$',rotation=0,loc="top",linespacing=1.5) if yunit1 is not None else ax.set_ylabel(f'$\mathrm{{{ylabel1}}}$',linespacing=1.5)
    def plot(ax,x,y,yerr,Formatstring,label=None,order=1,z=None):
        if sum(yerr)==0 : yerr=None
        if z is not None:
            ax.plot(x,y,z,Formatstring , zorder=order,linewidth = 1.5,label=label,markersize=5, markeredgecolor='k',markeredgewidth=0.5) 
        else:
            ax.plot(x,y,Formatstring , zorder=order,linewidth = 1.5,label=label,markersize=5, markeredgecolor='k',markeredgewidth=0.5)
            ax.errorbar(x,y,yerr,None,"ko" , zorder=order-1,label=label,markersize=0, markeredgecolor='k',markeredgewidth=0.5,capsize=5, elinewidth=0.5,ecolor="k")
        
        # ax.plot(x,y,Formatstring , zorder=order,linewidth = 1.5,label=label,markersize=5, markeredgecolor='k',markeredgewidth=0.5)
    def set_ticks(ax,x0=None,x1=None,y0=None,y1=None):
        if x0 is not None: ax.axis([x0, x1, y0, y1]) 
        start, end = ax.get_xlim()
        ax.xaxis.set_ticks(np.linspace(start, end, 5))
        start, end = ax.get_ylim()
        ax.yaxis.set_ticks(np.linspace(start, end, 5))

    def ternary():
        matplotlib.rcParams['mathtext.fontset'] = 'custom'
        matplotlib.rcParams['mathtext.rm'] = 'Calibri'
        matplotlib.rcParams['mathtext.it'] = 'Calibri'
        matplotlib.rcParams['mathtext.bf'] = 'Calibri'
        # matplotlib.rcParams['xtick.major.pad']='5'
        # matplotlib.rcParams['ytick.major.pad']='5'
        matplotlib.rcParams['axes.linewidth'] = 0.5
        # matplotlib.rcParams["toolbar"] = "toolmanager"
        # plt.rcParams['axes.autolimit_mode'] = 'round_numbers'

        font = {'weight' : 'normal',
                'size'   : 16,
                'family' : "calibri"}
        plt.rc('font', **font)

        fig = plt.figure(figsize=(6, 5),dpi=200)
        fig.subplots_adjust( wspace=0,hspace=0)
        ax = fig.add_axes(projection="ternary",rect=[0.18,1-0.1416-0.6603,0.6803,0.6803])
        ax.tick_params(labelbottom=True, labeltop=False, labelleft=True, labelright=False, bottom=True, top=False, left=True, right=True, direction="in",length=4, width=0.5,labelrotation='horizontal')
        ax.tick_params(labelbottom=True, labeltop=False, labelleft=True, labelright=False, bottom=True, top=False, left=True, right=True, direction="in",length=2, width=0.5,labelrotation='horizontal',which="minor")
        ax.tick_params(axis="t",pad=10)
        ax.tick_params(axis="l",pad=10)
        ax.tick_params(axis="r",pad=10)
        ax.taxis.set_label_rotation_mode( 'horizontal')
        ax.laxis.set_label_rotation_mode( 'horizontal')
        ax.raxis.set_label_rotation_mode( 'horizontal')
        return fig,ax
    def set_labels(ax,label="mass fractions / -",title="T = 298.15 K \np = 1 bar",xlabel='solvent',ylabel='polymer',zlabel="API"):
        ax.text(s=label,x=470, y=80)
        ax.text(s=title ,x=50, y=700)
        ax.set_tlabel(xlabel)
        ax.set_llabel(ylabel)
        ax.set_rlabel(zlabel)
        # ax.taxis.set_minor_locator(MultipleLocator(0.1))
        # ax.laxis.set_minor_locator(MultipleLocator(0.1))
        # ax.raxis.set_minor_locator(MultipleLocator(0.1))


# df=pd.read_csv("Werte2.txt", encoding = "utf-8", sep=",", header=None)
i=0
dfs=[]
titles=[]
excel_sheet=pd.read_excel("Werte.xlsx", sheet_name=None,header=None)
for name, sheet in excel_sheet.items():
    if "Series_plot" in name:
        titles.append(name)
        dfs.append(sheet)
    

# Plotten




app = QtWidgets.QApplication(sys.argv)

def extract_data(df,title):

    xlabel=df.values[0,0]
    ylabel=df.values[0,1]

    xlst=[]
    ylst=[]
    yerrlst=[]
    Formatstringlst=[]
    legendlst=[]
    for i in range(df.columns.size):
        if i%3==0:
            x=df.values[4:,i].astype(float)
            xlst.append(x)
        if i%3==1:
            legend=df.values[2,i]
            legendlst.append(legend)
            Formatstring=df.values[3,i]
            Formatstringlst.append(Formatstring)
            y=df.values[4:,i].astype(float)
            ylst.append(y)
        if i%3==2:
            yerr=df.values[4:,i].astype(float)
            yerrlst.append(yerr)
    
    return xlst,ylst,yerrlst,Formatstringlst,legendlst,xlabel,ylabel

def extract_ternary_data(df,title):

    xlabel=df.values[0,0]
    ylabel=df.values[0,1]
    zlabel=df.values[0,2]

    xlst=[]
    ylst=[]
    zlst=[]
    Formatstringlst=[]
    legendlst=[]
    for i in range(df.columns.size):
        if i%3==0:
            x=df.values[4:,i].astype(float)
            xlst.append(x)
        if i%3==1:
            legend=df.values[2,i]
            legendlst.append(legend)
            Formatstring=df.values[3,i]
            Formatstringlst.append(Formatstring)
            y=df.values[4:,i].astype(float)
            ylst.append(y)
        if i%3==2:
            z=df.values[4:,i].astype(float)
            zlst.append(z)
    
    return xlst,ylst,zlst,Formatstringlst,legendlst,xlabel,ylabel,zlabel

def plot_GUI(fig,ax):
    canvas=FigureCanvasQTAgg(fig)
    canvas.setFixedSize(1000,1000)
    canvas.draw()
    matplotlib_gui = MainWindow(fig,ax,canvas,title)
    return matplotlib_gui



 
matplotlib_guis=[]

if "ternary" in sys.argv:
    for title, df in zip(titles, dfs):
        xlst,ylst,zlst,Formatstringlst,legendlst,xlabel,ylabel,zlabel=extract_ternary_data(df,title)
        fig, ax = origin_like.ternary()
        origin_like.set_labels(ax,label="mass fractions / -",title="T = 298.15 K \np = 1 bar",xlabel=xlabel,ylabel=ylabel,zlabel=zlabel)
    for i,val in enumerate(xlst):
        origin_like.plot(ax,xlst[i],ylst[i],np.zeros_like(ylst[i]),Formatstringlst[i], z=zlst[i],label=legendlst[i],order=i)        
    matplotlib_guis.append(plot_GUI(fig, ax))

else:
    for title, df in zip(titles, dfs):
        xlst,ylst,yerrlst,Formatstringlst,legendlst,xlabel,ylabel=extract_data(df,title)
        fig, ax = origin_like.subplots()
        origin_like.set_xlabel(ax,xlabel)
        origin_like.set_ylabel(ax,ylabel)
        for i,val in enumerate(xlst):
            origin_like.plot(ax,xlst[i],ylst[i],yerrlst[i],Formatstringlst[i], label=legendlst[i],order=i)        
        matplotlib_guis.append(plot_GUI(fig, ax))
plt.close('all')
app.exec_()
