# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import csv
import time

# class Window(QMainWindow):
# class Ui_MainWindow(object):
class Ui_MainWindow(QtWidgets.QMainWindow):

############################ UI construction ##############################
    def setupUi(self, MainWindow):
        # Variables
        self.week           = ''
        self.today_date     = ''
        self.start_hour     = ''
        self.finish_hour    = ''
        self.task_A         = ''
        self.task_B         = ''
        self.task_C         = ''

        self.count_A = 0
        self.count_B = 0
        self.count_C = 0
        self.flagA = False    
        self.flagB = False    
        self.flagC = False    


        self.timer_A = QTimer()
        self.timer_A.timeout.connect(self.countTimeA)
        self.timer_A.start(100)

        self.timer_B = QTimer()
        self.timer_B.timeout.connect(self.countTimeB)
        self.timer_B.start(100)

        self.timer_C = QTimer()
        self.timer_C.timeout.connect(self.countTimeC)
        self.timer_C.start(100)


        MainWindow.setObjectName("MyCounter")
        MainWindow.resize(300, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        # 'Select your task' label 
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 211, 20))
        MainWindow.setCentralWidget(self.centralwidget)

        # Radio button for taskA
        self.radioButton_taskA = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_taskA.setGeometry(QtCore.QRect(50, 50, 95, 20))
        self.radioButton_taskA.toggled.connect(self.taskAselected)
         
        # Radio button for taskB
        self.radioButton_taskB = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_taskB.setGeometry(QtCore.QRect(50, 80, 95, 20))
        self.radioButton_taskB.toggled.connect(self.taskBselected)

        # Radio button for taskC
        self.radioButton_taskC = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_taskC.setGeometry(QtCore.QRect(50, 110, 95, 20))
        self.radioButton_taskC.toggled.connect(self.taskCselected)

        # EDIT TASKS BUTTON
        self.edit_tasks_button = QtWidgets.QPushButton(self.centralwidget)
        self.edit_tasks_button.setGeometry(QtCore.QRect(50, 135, 50, 20))
        self.edit_tasks_button.clicked.connect(self.edit_tasks)
         
        # START DAY BUTTON
        self.start_day_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_day_button.setGeometry(QtCore.QRect(150, 30, 100, 50))
        self.start_day_button.clicked.connect(self.start_day)

       # FINISH DAY BUTTON
        self.finish_day_button = QtWidgets.QPushButton(self.centralwidget)
        self.finish_day_button.setGeometry(QtCore.QRect(150, 100, 100, 50))
        self.finish_day_button.clicked.connect(self.finish_day)

       # WEEK REPORT BUTTON
        self.week_report_button = QtWidgets.QPushButton(self.centralwidget)
        self.week_report_button.setGeometry(QtCore.QRect(100, 170, 100, 20))
        self.week_report_button.clicked.connect(self.week_report)

 
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

############################ Functions ##############################          
    def countTimeA(self):
        if self.flagA:
            self.count_A+= 1

    def countTimeB(self):
        if self.flagB:
            self.count_B+= 1

    def countTimeC(self):
        if self.flagC:
            self.count_C+= 1   


    def taskAselected(self, selected):
        if selected:
            self.flagA = True
            self.flagB = False
            self.flagC = False
            self.countTimeA()

    def taskBselected(self, selected):
        if selected:
            self.flagB = True
            self.flagA = False
            self.flagC = False
            self.countTimeB()

    def taskCselected(self, selected):
        if selected:
            self.flagC = True
            self.flagA = False
            self.flagB = False
            self.countTimeC()
         

    def start_day(self):
        current_time = QTime.currentTime()
        self.start_hour = current_time.toString('hh:mm:ss')


    def finish_day(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        self.finish_hour = current_time.toString('hh:mm:ss')
        self.week = QDate.weekNumber(current_date)
        self.week = self.week[0]
        self.today_date = current_date.toString('dd-MM-yyyy')
        self.task_A = time_A = str(self.count_A / 10)
        self.task_B = time_B = str(self.count_B / 10)
        self.task_C = time_C = str(self.count_C / 10)
        newRow = "\n%d,%s,%s,%s,%s,%s,%s" % (self.week, self.today_date, self.start_hour, self.finish_hour, self.task_A, self.task_B, self.task_C)
        with open("./clarity_data.csv", "a") as f:
            f.write(newRow)
        # self.close()

    def week_report(self):
        print('report done')

    def edit_tasks(self):    
        newtaskA, done1 = QtWidgets.QInputDialog.getText(
             self, 'Task editor', 'Task A:')
        newtaskB, done2 = QtWidgets.QInputDialog.getText(
             self, 'Task editor', 'Task B:')
        newtaskC, done3 = QtWidgets.QInputDialog.getText(
             self, 'Task editor', 'Task C:')                     



############################ Translate to UI #########################          
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MyCounter", "MyCounter"))
        self.label.setText(_translate("MyCounter", "Select your task"))
        self.radioButton_taskA.setText(_translate("MyCounter", "taskA"))
        self.radioButton_taskB.setText(_translate("MyCounter", "taskB"))
        self.radioButton_taskC.setText(_translate("MyCounter", "taskC"))
        self.start_day_button.setText(_translate("MyCounter", "Start Day"))
        self.finish_day_button.setText(_translate("MyCounter", "Finish Day"))
        self.week_report_button.setText(_translate("MyCounter", "Weekly Report"))
        self.edit_tasks_button.setText(_translate("MyCounter", "Edit tasks"))

############################ Driver Code #########################
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
   
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
