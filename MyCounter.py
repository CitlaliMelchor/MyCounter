# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import csv
import time

class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("MyCounter ")

        # setting geometry
        self.setGeometry(2700, 100, 600, 200)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

    # method for widgets
    def UiComponents(self):

        # variables
        self.week           = ''
        self.today_date     = ''
        self.start_hour     = ''
        self.finish_hour    = ''
        self.task_A         = ''
        self.task_B         = ''
        self.task_C         = ''


        # START DAY BUTTON
        start_day_button = QPushButton("Start my day", self)
        # setting geometry to the push button
        start_day_button.setGeometry(100, 100, 150, 50)
        # adding action to the button
        start_day_button.clicked.connect(self.start_day)
        # creating a label object
        # self.label = QLabel("something",self)
        # self.label.setGeometry(50, 50, 50, 50)


        # FINISH DAY BUTTON
        finish_day_button = QPushButton("Finish my day", self)
        # setting geometry to the push button
        finish_day_button.setGeometry(250, 100, 150, 50)
        # adding action to the button
        finish_day_button.clicked.connect(self.finish_day)
        # creating a label object
        # self.label = QLabel("something",self)
        # self.label.setGeometry(50, 50, 50, 50)


    # method called by the start_day push button
    def start_day(self):

        # getting current time
        current_time = QTime.currentTime()

        # converting QTime object to string
        self.start_hour = current_time.toString('hh:mm:ss')

        # save it in the start time variable
        # self.label.setText(start_hour)

    # method called by the finish_day push button
    def finish_day(self):

        # getting current time
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        # converting QTime object to string
        self.finish_hour = current_time.toString('hh:mm:ss')

        self.week = str(current_date.weekNumber)
        self.today_date = str(current_date)
        self.task_A = 'ddd'
        self.task_B = 'sss'
        self.task_C = 'kkk'

        # save it in the start time variable
        # self.label.setText(finish_hour)

        # add a new row with the start and finish day into my csv data
        newRow = "\n%s,%s,%s,%s,%s,%s,%s\n" % (self.week, self.today_date, self.start_hour, self.finish_hour, self.task_A, self.task_B, self.task_C)
        with open("C:/Users/670273766/source/clarity_data.csv", "a") as f:
            f.write(newRow)


# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

# showing all the widgets
window.show()

# start the app
App.exit(App.exec_())






# import time
# import csv


# today = (time.strftime("%d-%m-%Y"))
# newRow = "\n%s,%s,%s,%s,%s,%s\n" % (today, yes, ok, war, leg, noag)
# with open("clarity_data.csv", "a") as f:
    # f.write(newRow)