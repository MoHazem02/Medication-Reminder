from PyQt5 import QtCore, QtGui, QtWidgets
import sys, ApplicationManager

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1508, 780)
        MainWindow.setStyleSheet("background-image: url(\'Assets/img4.jpg\');\n"
"color: white;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 463))
        self.frame.setStyleSheet("background-color: none;\n"
"background-image: none;\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.frame)
        self.calendarWidget.setMinimumSize(QtCore.QSize(521, 0))
        self.calendarWidget.setStyleSheet("color:black;")
        self.calendarWidget.setObjectName("calendarWidget")
        self.horizontalLayout.addWidget(self.calendarWidget)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.listWidget = QtWidgets.QListWidget(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setStyleSheet("color: white;\n"
"background: transparent;")
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.verticalLayout.addWidget(self.frame)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet("QProgressBar{\n"
"text-align:center;\n"
"color:rgb(54, 163, 0);\n"
"border-radius:10px;\n"
"}\n"
"QProgressBar::chunk{\n"
"background-color:rgb(0, 170, 255);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.progressBar.setMaximum(6)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.textBrowser.setFont(font)
        self.textBrowser.setStyleSheet("background: transparent;\n"
"color: red;")
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1508, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_Transcription = QtWidgets.QAction(MainWindow)
        self.actionLoad_Transcription.setObjectName("actionLoad_Transcription")
        self.menuFile.addAction(self.actionLoad_Transcription)
        self.menubar.addAction(self.menuFile.menuAction())
        self.actionLoad_Transcription.triggered.connect(lambda: MAESTRO.Load_Transcription() )

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Medication Reminder"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        # item = self.listWidget.item(0)
        # item.setText(_translate("MainWindow", "Panadol (1 pill) 3:00 PM"))
        # item = self.listWidget.item(1)
        # item.setText(_translate("MainWindow", "Telfast (2 pills) 4:00 PM"))
        # item = self.listWidget.item(2)
        # item.setText(_translate("MainWindow", "Panadol (1 pill) 9:00 PM"))
        # item = self.listWidget.item(3)
        # item.setText(_translate("MainWindow", "Telfast (2 pills) 10:00 PM"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt; font-weight:600;\">  No Alerts</span></p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionLoad_Transcription.setText(_translate("MainWindow", "Load Prescription"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MAESTRO = ApplicationManager.ApplicationManager(ui)
    MainWindow.show()
    sys.exit(app.exec_())
