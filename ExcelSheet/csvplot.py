import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg,NavigationToolbar2QT
import os
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget,QGridLayout
from PyQt5.QtGui import QImage, QPainter,QFont
from PyQt5.QtCore import Qt
import sys
import matplotlib.pyplot as plt
import sys
from matplotlib.ticker import AutoLocator
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, AutoMinorLocator
import sys
import mpltern
from PIL import ImageGrab
import io

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self,fig,ax,canvas,title, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle(title)
        sc=canvas
        self.fig=fig
        
        self.ax=ax
        self.canvas=canvas

        self.texts=[val for val in self.ax.get_children() if isinstance(val,matplotlib.text.Text) ]


        # Create buttons
        self.button_x_limits = QtWidgets.QPushButton("Adjust X Limits")
        self.button_y_limits = QtWidgets.QPushButton("Adjust Y Limits")
        self.button_z_limits = QtWidgets.QPushButton("Adjust Z Limits")
        self.button_reset_ticks = QtWidgets.QPushButton("Reset Ticks")
        self.button_rotate_vertical = QtWidgets.QPushButton("Rotate y-Axis vertical")
        self.button_rotate_horizontal = QtWidgets.QPushButton("Rotate y-Axis horizontal")
        self.button_clipboard = QtWidgets.QPushButton("Copy plot to clipboard")

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
        if hasattr(self.ax,"taxis"):
            self.zmin_label=QtWidgets.QLabel("zmin")
            self.zmax_label=QtWidgets.QLabel("zmax")
            self.zlast_label=QtWidgets.QLabel("zend")
            self.nzticks_label=QtWidgets.QLabel("nzticks")
            
            self.label_label=QtWidgets.QLabel("label")
            self.entry_label = QtWidgets.QLineEdit("mass fractions /-")

            self.tlabel_label=QtWidgets.QLabel("x label")
            self.tlabel_entry = QtWidgets.QLineEdit(self.ax.get_tlabel())
            self.llabel_label=QtWidgets.QLabel("y label")
            self.llabel_entry = QtWidgets.QLineEdit(self.ax.get_llabel())
            self.rlabel_label=QtWidgets.QLabel("z label")
            self.rlabel_entry = QtWidgets.QLineEdit(self.ax.get_rlabel())

            self.ax.set_tlabel("")
            self.ax.set_llabel("")
            self.ax.set_rlabel("")
            self.canvas.draw()
            self.bg = self.canvas.copy_from_bbox(self.fig.bbox)
            self.canvas.blit(self.fig.bbox)
            self.button_redraw = QtWidgets.QPushButton("Reset label positions")
            self.button_redraw.clicked.connect(lambda: self.canvas.draw())

            self.title_label=QtWidgets.QLabel("title")
            self.entry_title = QtWidgets.QPlainTextEdit("T = 298.15 K \np = 1 bar")
 
        self.xy_pos=QtWidgets.QLabel("x= ; y=")
        

        # Connect button signals to respective slots
        self.button_clipboard.clicked.connect(self.copy_to_clipboard)
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

        if hasattr(self.ax,"taxis"):
        #adjust zlim labels 
            zlim_label_layout = QtWidgets.QHBoxLayout()
            zlim_label_layout.addWidget(self.zmin_label)
            zlim_label_layout.addWidget(self.zmax_label)
            zlim_label_layout.addWidget(self.zlast_label)
            zlim_label_layout.addWidget(self.nzticks_label)
        
            button_layout.addLayout(zlim_label_layout)
            #adjust ylim entries
            zlim_layout = QtWidgets.QHBoxLayout()
            zlim_layout.addWidget(self.entry_z_min)
            zlim_layout.addWidget(self.entry_z_max)
            zlim_layout.addWidget(self.entry_z_last)
            zlim_layout.addWidget(self.entry_z_ticks)
            button_layout.addLayout(zlim_layout)
            button_layout.addWidget(self.button_z_limits)
            button_layout.addWidget(self.label_label)
            button_layout.addWidget(self.entry_label)
            button_layout.addWidget(self.title_label)
            button_layout.addWidget(self.entry_title)

            button_layout.addWidget(self.tlabel_label)
            button_layout.addWidget(self.tlabel_entry)
            button_layout.addWidget(self.llabel_label)
            button_layout.addWidget(self.llabel_entry)
            button_layout.addWidget(self.rlabel_label)
            button_layout.addWidget(self.rlabel_entry)

        button_layout.addWidget(self.button_reset_ticks)

        # add rotation
        if hasattr(self.ax,"taxis"):
            button_layout.addWidget(self.button_redraw)
        else:

            button_layout.addWidget(self.button_rotate_horizontal)
            button_layout.addWidget(self.button_rotate_vertical)
            button_layout.addWidget(self.xy_pos)
        #Stretch until the end of the layout
        button_layout.addWidget(self.button_clipboard)
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

        if hasattr(self.ax,"taxis"):
            self.entry_label.textChanged.connect(self.refresh_label_title)
            self.entry_title.textChanged.connect(self.refresh_label_title)
            self.tlabel_entry.textChanged.connect(self.refresh_label_title)
            self.llabel_entry.textChanged.connect(self.refresh_label_title)
            self.rlabel_entry.textChanged.connect(self.refresh_label_title)
            self.refresh_label_title()
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


    def copy_to_clipboard(self):    
        width, height = self.fig.get_size_inches() * self.fig.get_dpi()
        image = self.canvas.buffer_rgba()

        qimage = QImage(image, width, height,  QImage.Format_ARGB32).rgbSwapped()
        pixmap = QtGui.QPixmap.fromImage(qimage)
        QApplication.clipboard().setPixmap(pixmap)





    def reset_ticks(self):
        if hasattr(self.ax,"taxis"):
            self.ax.taxis.set_major_locator(AutoLocator())
            self.ax.laxis.set_major_locator(AutoLocator())
            self.ax.raxis.set_major_locator(AutoLocator())
        else: 
            self.ax.xaxis.set_major_locator(AutoLocator())
            self.ax.yaxis.set_major_locator(AutoLocator())
        
        self.canvas.draw()
        # self.bg = self.canvas.copy_from_bbox(self.fig.bbox)
        


    def vertical_ylabel(self):
        if hasattr(self.ax,"taxis"):
            pass
        else: 
            self.ax.yaxis.label.set(rotation=90)
            self.ax.yaxis.set_label_coords(-0.15,0.5)
        self.canvas.draw()
        # self.bg = self.canvas.copy_from_bbox(self.fig.bbox)
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
                self.ax.set_tlabel("")
                self.ax.set_llabel("")
                self.ax.set_rlabel("")
                self.ax.set_tlim(float(x_min), float(x_max))
                ticks=np.linspace(float(x_min), float(x_last), int(x_ticks))
                ticks_zero_one_less=ticks[np.logical_and(ticks!=0,ticks!=1)]
                self.ax.taxis.set_ticks(ticks_zero_one_less)
            else:
                self.ax.set_xlim(float(x_min), float(x_max))
                self.ax.xaxis.set_ticks(np.linspace(float(x_min), float(x_last), int(x_ticks)))
            # self.ax.xaxis.set_major_locator(AutoLocator())
            self.canvas.draw()
            
            self.bg = self.canvas.copy_from_bbox(self.fig.bbox)
            if hasattr(self.ax,"taxis"): self.refresh_label_title()
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Invalid Input", "Please enter valid x limits.")

    def adjust_y_limits(self):
        # Get the y limits from the entry box
        y_min, y_max = self.entry_y_min.text(),self.entry_y_max.text()
        y_last= self.entry_y_last.text()
        y_ticks = self.entry_y_ticks.text()
        try:
            if hasattr(self.ax,"taxis"):
                self.ax.set_tlabel("")
                self.ax.set_llabel("")
                self.ax.set_rlabel("")
                self.ax.set_llim(float(y_min), float(y_max))
                ticks=np.linspace(float(y_min), float(y_last), int(y_ticks))
                ticks_zero_one_less=ticks[np.logical_and(ticks!=0,ticks!=1)]
                self.ax.laxis.set_ticks(ticks_zero_one_less)
            else:
                self.ax.set_ylim(float(y_min), float(y_max))
                self.ax.yaxis.set_ticks(np.linspace(float(y_min), float(y_last) , int(y_ticks)))
            # self.ax.yaxis.set_major_locator(AutoLocator())
            self.canvas.draw()
            self.bg = self.canvas.copy_from_bbox(self.fig.bbox)
            if hasattr(self.ax,"taxis"): self.refresh_label_title()
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Invalid Input", "Please enter valid y limits.")
        

    def adjust_z_limits(self):
        # Get the y limits from the entry box
        z_min, z_max = self.entry_z_min.text(),self.entry_z_max.text()
        z_last= self.entry_z_last.text()
        z_ticks = self.entry_z_ticks.text()
        try:

            self.ax.set_tlabel("")
            self.ax.set_llabel("")
            self.ax.set_rlabel("")
            self.ax.set_rlim(float(z_min), float(z_max))
            ticks=np.linspace(float(z_min), float(z_last), int(z_ticks))
            ticks_zero_one_less=ticks[np.logical_and(ticks!=0,ticks!=1)]
            self.ax.raxis.set_ticks(ticks_zero_one_less)
            self.canvas.draw()
            self.bg = self.canvas.copy_from_bbox(self.fig.bbox)
            self.refresh_label_title()
        except ValueError:
            QtWidgets.QMessageBox.warning(self, "Invalid Input", "Please enter valid z limits.")

    
    def refresh_label_title(self):
        self.texts[0].set_text(self.entry_label.text())
        self.texts[1].set_text(self.entry_title.toPlainText())

        tlabel=self.ax.set_tlabel(self.tlabel_entry.text())
        llabel=self.ax.set_llabel(self.llabel_entry.text())
        rlabel=self.ax.set_rlabel(self.rlabel_entry.text())
        # tlabel=self.ax.set_tlabel(self.tlabel_entry.text())
        # llabel=self.ax.set_llabel(self.llabel_entry.text()+"         ")
        # rlabel=self.ax.set_rlabel("         "+self.rlabel_entry.text())

        self.canvas.restore_region(self.bg)
        ax.draw_artist(self.texts[0])
        ax.draw_artist(self.texts[1])
        ax.draw_artist(tlabel)
        ax.draw_artist(llabel)
        ax.draw_artist(rlabel)
        
        self.canvas.blit(self.fig.bbox)
        ax.figure.canvas.flush_events()
        # fig.canvas.draw_idle()
        # QtWidgets.QApplication.processEvents()


class digitizer(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(digitizer, self).__init__(None, QtCore.Qt.WindowStaysOnTopHint,*args, **kwargs)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint )
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowTitle("Press enter key to snip")
        self.setGeometry(0, 0,300, 1)
        self.show()
    def start(self):
        screen = QtWidgets.QApplication.primaryScreen()
        size = screen.size()
        # screen_width = root.winfo_screenwidth()
        # screen_height = root.winfo_screenheight()
        self.setGeometry(0, 0,size.width(), size.height())
        self.setWindowTitle(' ')

        
    
        self.setWindowOpacity(0.3)
        QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        print('Capture the screen...')
        self.show()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor('black'), 3))
        qp.setBrush(QtGui.QColor(128, 128, 255, 128))
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.close()

        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())

        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        img.save('capture.png')
    def keyPressEvent(self, event):
        if event.key()==Qt.Key_Return:
            self.start()
            print("Hey")




class PlotWidget(QWidget):
    def __init__(self, image):
        super().__init__()
        self.image = image
        self.xaxis_points = []
        self.yaxis_points = []
        self.points=[]
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(0, 0, self.image)
        painter.setFont(QtGui.QFont("arial",22))
        i,j=0,0
        for point in self.xaxis_points:
            i+=1
            painter.setPen(Qt.blue)
            painter.drawText(point, f"x{i}")
            painter.drawEllipse(point, 2, 2)
        for point in self.yaxis_points:
            j+=1
            painter.setPen(Qt.red)
            painter.drawText(point, f"y{j}")
            painter.drawEllipse(point, 2, 2)
        for point in self.points:
            painter.setPen(Qt.green)
            painter.setBrush(Qt.green)
            painter.drawEllipse(point, 3, 3)
        
    def mousePressEvent(self, event):
        if event.buttons() & Qt.LeftButton:
            clicked_point = event.pos()

            # Check if the user is selecting an axis point
            if len(self.xaxis_points) < 2:
                self.xaxis_points.append(clicked_point)
                self.update()
            elif len(self.yaxis_points) < 2:
                self.yaxis_points.append(clicked_point)
                self.update()
            else:
                self.points.append(clicked_point)
                self.update()

class DigitizePlotGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.data = {}
        self.k=0
        self.setWindowTitle("Plot Digitizer")
        self.plot_widget = None
        self.image = None
        screen = QtWidgets.QApplication.primaryScreen()
        size = screen.size()
        self.setGeometry(0, 0,size.width()*0.9, size.height()*0.9)
        self.setCentralWidget(QWidget())
        self.layout = QVBoxLayout(self.centralWidget())

        self.hlayout = QGridLayout(self.centralWidget())
        self.load_plot_image("capture.png")
        # self.layout.addStretch(1)

        self.x1_entry = QtWidgets.QLineEdit()
        self.y1_entry = QtWidgets.QLineEdit()
        self.P1_label=QtWidgets.QLabel("x1")
        self.P1_label.setStyleSheet("color: blue")
        self.P1_label.setFont(QFont('Arial', 22))

        self.P2_label=QtWidgets.QLabel("y1")
        self.P2_label.setStyleSheet("color: red")
        self.P2_label.setFont(QFont('Arial', 22))


        self.x2_entry = QtWidgets.QLineEdit()
        self.y2_entry = QtWidgets.QLineEdit()
        self.P3_label=QtWidgets.QLabel("x2")
        self.P3_label.setStyleSheet("color: blue")
        self.P3_label.setFont(QFont('Arial', 22))

        self.P4_label=QtWidgets.QLabel("y2")
        self.P4_label.setStyleSheet("color: red")
        self.P4_label.setFont(QFont('Arial', 22))




        self.hlayout.addWidget(self.P1_label,1,0)
        self.hlayout.addWidget(self.x1_entry,1,1)
        self.hlayout.addWidget(self.P3_label,1,2)
        self.hlayout.addWidget(self.x2_entry,1,3)
        self.hlayout.addWidget(self.P2_label,2,0)
        self.hlayout.addWidget(self.y1_entry,2,1)
        self.hlayout.addWidget(self.P4_label,2,2)
        self.hlayout.addWidget(self.y2_entry,2,3)
        self.hlayout.addWidget(QtWidgets.QLabel("Click on 2 axis points for x values (blue) and y values (red). Then click on data points (green)"),1,4)
        self.hlayout.addWidget(QtWidgets.QLabel("Press enter to copy data points to clipboard. Press escape to remove all points. Press alt to copy all data points and close"),2,4)


        self.layout.addLayout(self.hlayout)
        


        self.show()
    def load_plot_image(self, image_path):
        self.image = QImage(image_path)
        self.plot_widget = PlotWidget(self.image)
        self.layout.addWidget(self.plot_widget)

    def keyPressEvent(self, event):
        
        if event.key()==Qt.Key_Return:
            self.k+=1
            x1,y1=float(self.x1_entry.text()),float(self.y1_entry.text())
            x2,y2=float(self.x2_entry.text()),float(self.y2_entry.text())
            P1x=self.plot_widget.xaxis_points[0].x()
            P2x=self.plot_widget.xaxis_points[1].x()
            P3y=self.plot_widget.yaxis_points[0].y()
            P4y=self.plot_widget.yaxis_points[1].y()
            xQ=[]
            yQ=[]
            for point in self.plot_widget.points:
                Qx,Qy=point.x(),point.y()
                xQ.append((x2-x1)/(P2x-P1x)*(Qx-P1x)+x1)
                yQ.append((y2-y1)/(P4y-P3y)*(Qy-P3y)+y1)
            newdata={f"x{self.k}":xQ , f"y{self.k}":yQ}
            self.data.update(newdata)
            pd.DataFrame.from_dict(self.data,orient='index').T.to_clipboard(excel=True, sep=None, index=False)
            self.plot_widget.points=[]
            self.plot_widget.update()
            

        if event.key()==Qt.Key_Alt:
            pd.DataFrame.from_dict(self.data,orient='index').T.to_excel("file.xlsx")
            pd.DataFrame.from_dict(self.data,orient='index').T.to_clipboard(excel=True, sep=None, index=False)
            self.close()

        if event.key()==Qt.Key_Escape:
            self.plot_widget.xaxis_points=[]
            self.plot_widget.yaxis_points=[]
            self.plot_widget.points=[]
            self.data = {}
            self.plot_widget.update()


            # self.points=[]
            # self.update()
            

def basic_colors(Formatstring):
    if "g" in Formatstring: return "#99CC00" #green
    if "c" in Formatstring: return "#99CDE9" #cyan
    if "b" in Formatstring: return "#246FE2" #blue
    if "r" in Formatstring: return "#FF8500" #orange
    if "m" in Formatstring: return "#FFCCCC" #magenta
    if "y" in Formatstring: return "#FFD67E" #yellow
    if "a" in Formatstring: return "#666666" #gray
    if "k" in Formatstring: return "#000000" #black
    return "#000000"

class origin_like:
    def subplots(sharex=False):
        matplotlib.rcParams['mathtext.fontset'] = 'custom'
        matplotlib.rcParams['mathtext.rm'] = 'Calibri'
        matplotlib.rcParams['mathtext.it'] = 'Calibri'
        matplotlib.rcParams['mathtext.bf'] = 'Calibri'
        matplotlib.rcParams['xtick.major.pad']='5'
        matplotlib.rcParams['ytick.major.pad']='5'
        matplotlib.rcParams['axes.linewidth'] = 0.5
        matplotlib.rcParams['axes.axisbelow'] = True
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
    def plot(ax,x,y,Formatstring,label=None,order=1,yerr=None,z=None):
        if z is not None:
            ax.plot(x,y,z,Formatstring , zorder=order,linewidth = 1.5,label=label,markersize=5, markeredgecolor='k',markeredgewidth=0.5,color=basic_colors(Formatstring)) 
        else:
            ax.plot(x,y,Formatstring , zorder=order,linewidth = 1.5,label=label,markersize=5, markeredgecolor='k',markeredgewidth=0.5,color=basic_colors(Formatstring))
            if yerr is not None:
                if sum(yerr)==0 : yerr=None
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
        ax.taxis.set_minor_locator(AutoMinorLocator(2))
        ax.laxis.set_minor_locator(AutoMinorLocator(2))
        ax.raxis.set_minor_locator(AutoMinorLocator(2))

    def filled_line(ax,x,y,z,Formatstring,legend):
        p=ax.plot(x, y, z,Formatstring,linewidth=1,label=legend+"_filled",color=basic_colors(Formatstring))
        color = p[0].get_color()
        ax.fill(x, y, z, alpha=0.2,color=color,label=legend+"_filled")

    def conodes(ax,RBx,RBy,RBz,LBx,LBy,LBz,Formatstring,legend):
        ax.plot(RBx,RBy,RBz,Formatstring,linewidth=1,label=legend,color=basic_colors(Formatstring))
        ax.plot(LBx,LBy,LBz,Formatstring,linewidth=1,label=legend,color=basic_colors(Formatstring))
        
        for i,(rt,rl,rr,lt,ll,lr) in enumerate(zip(RBx,RBy,RBz,LBx,LBy,LBz)):
                ax.plot([rt,lt],[rl,ll],[rr,lr],"-",linewidth=0.5,label=f"Konode {i}",color=basic_colors(Formatstring))



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




# app = QtWidgets.QApplication(sys.argv)

def extract_data(df,title):

    xlabel=df.values[0,0]
    ylabel=df.values[0,1]
    zlabel=df.values[0,2]

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
    
    return xlst,ylst,yerrlst,Formatstringlst,legendlst,xlabel,ylabel,zlabel

# def extract_ternary_data(df,title):

#     xlabel=df.values[0,0]
#     ylabel=df.values[0,1]
#     zlabel=df.values[0,2]

#     xlst=[]
#     ylst=[]
#     zlst=[]
#     Formatstringlst=[]
#     legendlst=[]
#     for i in range(df.columns.size):
#         if i%3==0:
#             x=df.values[4:,i].astype(float)
#             xlst.append(x)
#         if i%3==1:
#             legend=df.values[2,i]
#             legendlst.append(legend)
#             Formatstring=df.values[3,i]
#             Formatstringlst.append(Formatstring)
#             y=df.values[4:,i].astype(float)
#             ylst.append(y)
#         if i%3==2:
#             z=df.values[4:,i].astype(float)
#             zlst.append(z)
    
#     return xlst,ylst,zlst,Formatstringlst,legendlst,xlabel,ylabel,zlabel

def plot_GUI(fig,ax):
    canvas=FigureCanvasQTAgg(fig)
    canvas.setFixedSize(*fig.get_size_inches()*fig.get_dpi())
    canvas.draw()
    matplotlib_gui = MainWindow(fig,ax,canvas,title)
    return matplotlib_gui



 
matplotlib_guis=[]

# if "ternary" in sys.argv:
#     for title, df in zip(titles, dfs):
#         # xlst,ylst,zlst,Formatstringlst,legendlst,xlabel,ylabel,zlabel=extract_ternary_data(df,title)
#         fig, ax = origin_like.ternary()
#         origin_like.set_labels(ax,label="mass fractions / -",title="T = 298.15 K \np = 1 bar",xlabel=xlabel,ylabel=ylabel,zlabel=zlabel)
#     for i,val in enumerate(xlst):
#         origin_like.plot(ax,xlst[i],ylst[i],np.zeros_like(ylst[i]),Formatstringlst[i], z=zlst[i],label=legendlst[i],order=i)
#         origin_like.filled_line(ax,xlst[i],ylst[i],zlst[i],Formatstringlst[i])     
#     origin_like.conodes(ax,xlst[0],ylst[0],zlst[0],xlst[1],ylst[1],zlst[1],Formatstringlst[i])           
#     matplotlib_guis.append(plot_GUI(fig, ax))

# else:
app = QApplication(sys.argv)
if "digitizer" in sys.argv:
    GUI=digitizer()
    app.exec_()
    window = DigitizePlotGUI()

else:
    for title, df in zip(titles, dfs):
        xlst,ylst,yerrlst,Formatstringlst,legendlst,xlabel,ylabel,zlabel=extract_data(df,title)
        if "ternary" in sys.argv:
            fig, ax = origin_like.ternary()
            origin_like.set_labels(ax,label="",title="",xlabel=xlabel,ylabel=ylabel,zlabel=zlabel)
            zlst=[]
            for i,val in enumerate(xlst):
                zlst.append(1-xlst[i]-ylst[i])
                origin_like.plot(ax,xlst[i],ylst[i],Formatstringlst[i], z=zlst[i],label=legendlst[i],order=i)
                origin_like.filled_line(ax,xlst[i],ylst[i],zlst[i],Formatstringlst[i],legendlst[i])     
            origin_like.conodes(ax,xlst[0],ylst[0],zlst[0],xlst[1],ylst[1],zlst[1],Formatstringlst[i],legendlst[i])

        else:
            fig, ax = origin_like.subplots()
            origin_like.set_xlabel(ax,xlabel)
            origin_like.set_ylabel(ax,ylabel)
            for i,val in enumerate(xlst):
                origin_like.plot(ax,xlst[i],ylst[i],Formatstringlst[i], yerr=yerrlst[i],label=legendlst[i],order=i)        
        matplotlib_guis.append(plot_GUI(fig, ax))
plt.close('all')
app.exec_()
