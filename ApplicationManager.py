from pymata4 import pymata4
import Medicine
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QColor
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
        self.Opened = False
        self.board = pymata4.Pymata4()
        self.board.set_pin_mode_sonar(self.trig_pin, self.echo_pin, self.process)
        self.taken_pills = 0

    def process(self, data):
        if data[2] > 100:
            return
        if data[2] > 30 and not self.Opened:
            self.Opened = True
            self.took_medicine()
        else:
            if data[2] < 15:
                self.Opened = False
        print(f"Distance: {data[2]} cm")

    def Load_Transcription(self):
        file_path, _ = QFileDialog.getOpenFileName(None, "Browse Signal", "", "All Files (*)")
        if file_path:
            with open(file_path, "r") as transcription:
                self.CreatListItems(transcription)



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
        item.setText(f"{medicine} || {dose} || {ind}:00")
        self.ui_window.listWidget.addItem(item)

    def sort_medicines(self):
        for medicine in self.medicines:
            index = 0
            times = int((24 / medicine.time) % 24)
            for time in range(medicine.time):
                self.TIMES[self.medicine_count + index] = medicine
                index += times
            self.medicine_count += 1

    def took_medicine(self):
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(True)
        self.ui_window.listWidget.item(self.taken_pills).setFont(font)
        self.ui_window.listWidget.item(self.taken_pills).setForeground(QColor("red"))
        self.taken_pills += 1
        self.ui_window.progressBar.setValue(self.taken_pills)
