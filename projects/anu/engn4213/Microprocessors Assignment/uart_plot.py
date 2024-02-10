import serial
from serial.tools import list_ports
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt, QTimer
import pyqtgraph as pg
import numpy as np
import datetime as dt
import re

resolution = 500
# ensure a valid resolution is used
if ((4096//resolution)%2): 
    while ((4096//resolution)%2):
        resolution+=1
count = 0
xs = []
ys = []

ser = serial.Serial(timeout=10)
ser.baudrate = 115200
ports = list_ports.comports()
for port in ports: 
    if re.search('STM32', port.description):
        device_name = port.description
        port_name = port.device
        print(f'\nPort found! Opening connection with "{device_name}" through "{port_name}"...\n')
        ser.port = port_name
ser.open()

class RealTimePlotWidget(QWidget):
    def __init__(self, parent=None):
        super(RealTimePlotWidget, self).__init__(parent)
        
        # Set up the plot widget
        self.plot_widget = pg.PlotWidget()
        self.plot_curve = self.plot_widget.plot()
        
        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.plot_widget)
        self.setLayout(layout)
        
        # Set up the data
        self.x_data = np.array([])
        self.y_data = np.array([])
        
        # Set up the update timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_plot)
        self.timer.start(100)  # Update every 100 milliseconds
    
    def update_plot(self):
        # Generate new data
        data = ser.read(4096)
        if len(data)==0: 
            print('No data recieved in last 10 seconds. Terminating connection...')
            sys.exit()
        # format and append to lists
        for i in range(0,4095,4096//resolution):
            y = (data[i]<<8) | data[i+1]
            # filtering operation to fix uart stuffups
            if (y>4095): 
                y = (data[i+1]<<8) | data[i+2]
            self.y_data = np.append(self.y_data, y)
        
        # get rid of everything stored except two most recent samples
        self.y_data = self.y_data[-resolution*4:]
        # format x_data appropriately
        self.x_data = np.arange(0,self.y_data.shape[0],1)

        # Update the plot curve
        self.plot_curve.setData([], []) # added
        self.plot_curve.setData(self.x_data, self.y_data)
        
        # Set the x-axis range to show only the last 2 buffers
        self.plot_widget.setXRange(max(self.x_data) - resolution*4, max(self.x_data))
        self.plot_widget.setYRange(0,4096)

    def closeEvent(self, event):
        self.serial_port.close()  # Close the serial port
        event.accept()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle(f"{device_name}")
        
        # Set up the central widget
        self.central_widget = RealTimePlotWidget()
        self.setCentralWidget(self.central_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


    