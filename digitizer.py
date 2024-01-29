import pandas as pd
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget,QGridLayout
from PyQt5.QtGui import QImage, QPainter,QFont
from PyQt5.QtCore import Qt
import sys
import sys
from PIL import ImageGrab

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
        self.setGeometry(0, 0,int(size.width()*0.9), int(size.height()*0.9))
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
            

app = QApplication(sys.argv)
GUI=digitizer()
app.exec_()
window = DigitizePlotGUI()
app.exec_()