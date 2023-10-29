from pymata4 import pymata4
from datetime import datetime
import Medicine
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
import csv

   
class ApplicationManager:
    def __init__(self, ui_window):
        self.trig_pin = 3
        self.echo_pin = 2
        self.ui_window = ui_window
        self.TIMES = [0] * 25
        self.medicines = []
        self.medicine_count = 0
        # self.board = pymata4.Pymata4()
        # self.board.set_pin_mode_sonar(self.trig_pin, self.echo_pin, self.process)

    def process(self, data):
        if data[2] > 100:
            return 
        print(f"Distance: {data[2]} cm")
        # lw mfe4 7aga 5als mn 150 le 250 lw fe mn 5 cm le 50 cm

    def Load_Transcription(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Browse Signal", "", "All Files (*)")
        if file_path:
            with open(file_path, "r") as transcription:
                self.CreatListItems(transcription)
                self.SetProgressBarLimits()
                # self.Check_Timings_and_Progress()



    def CreatListItems(self, transcription):
        self.ui_window.listWidget.clear()
        for row in csv.reader(transcription):
            medicine = Medicine.Medicine(row[0], row[1], row[2])
            self.medicines.append(medicine)
        self.sort_medicines()
        for med in range(len(self.TIMES)):
            if self.TIMES[med]:

                self.CreateItem(self.TIMES[med].name, self.TIMES[med].dose, med)

    def CreateItem(self, medicine, dose, ind):
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/pill.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        item.setText(f"{medicine} || {dose} || {ind}")
        self.ui_window.listWidget.addItem(item)

    def sort_medicines(self):
        for medicine in self.medicines:
            index = 0
            times = int((24 / medicine.time) % 24)
            for time in range(medicine.time):
                self.TIMES[self.medicine_count + index] = medicine
                index += times
            self.medicine_count += 1


    def Check_Timings_and_Progress(self):
        # all_strikeout = False
        # while not all_strikeout:
        #     all_strikeout = True
            index = 0
            for times in self.timings_list:
                if times == self.current_time:
                    self.ui_window.listWidget.item(index).setStrikeOut(True)
                    index += 1

            # if self.ui_window.listWidget.item(index)[2] == timings_list[index]:
            #     self.ui_window.listWidget.item(index).setStrikeOut(True)
            #     self.ui_window.progressBar