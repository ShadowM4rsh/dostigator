from PyQt5 import QtCore, QtGui, QtWidgets


class Main_Screen(object):
    def setupUiii(self, Goals):
        Goals.setObjectName("Goals")
        Goals.resize(791, 720)
        Goals.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(Goals)
        self.centralwidget.setObjectName("centralwidget")
        self.Backgr = QtWidgets.QLabel(self.centralwidget)
        self.Backgr.setGeometry(QtCore.QRect(-10, -10, 801, 731))
        self.Backgr.setText("")
        self.Backgr.setPixmap(QtGui.QPixmap("space.jpg"))
        self.Backgr.setObjectName("Backgr")
        self.golllllllll = QtWidgets.QTextBrowser(self.centralwidget)
        self.golllllllll.setGeometry(QtCore.QRect(230, 280, 111, 41))
        self.golllllllll.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.golllllllll.setObjectName("golllllllll")
        self.tm_mark = QtWidgets.QPushButton(self.centralwidget)
        self.tm_mark.setGeometry(QtCore.QRect(240, 330, 91, 23))
        self.tm_mark.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border: none;")
        self.tm_mark.setObjectName("tm_mark")
        self.gol = QtWidgets.QTextBrowser(self.centralwidget)
        self.gol.setGeometry(QtCore.QRect(10, 20, 101, 51))
        self.gol.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.gol.setObjectName("gol")
        self.gollllllllll = QtWidgets.QTextEdit(self.centralwidget)
        self.gollllllllll.setGeometry(QtCore.QRect(0, 50, 131, 61))
        self.gollllllllll.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.gollllllllll.setObjectName("gollllllllll")
        self.golll = QtWidgets.QTextBrowser(self.centralwidget)
        self.golll.setGeometry(QtCore.QRect(0, 170, 171, 61))
        self.golll.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.golll.setObjectName("golll")
        self.create = QtWidgets.QPushButton(self.centralwidget)
        self.create.setGeometry(QtCore.QRect(10, 630, 191, 41))
        self.create.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border: none;")
        self.create.setObjectName("create")
        self.lisst = QtWidgets.QTableWidget(self.centralwidget)
        self.lisst.setGeometry(QtCore.QRect(530, 50, 256, 561))
        self.lisst.setStyleSheet("")
        self.lisst.setObjectName("lisst")
        self.lisst.setColumnCount(1)
        self.lisst.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        item.setFont(font)
        self.lisst.setHorizontalHeaderItem(0, item)
        self.gollll = QtWidgets.QTextBrowser(self.centralwidget)
        self.gollll.setGeometry(QtCore.QRect(0, 240, 171, 41))
        self.gollll.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.gollll.setObjectName("gollll")
        self.golllllll = QtWidgets.QTextBrowser(self.centralwidget)
        self.golllllll.setGeometry(QtCore.QRect(0, 280, 101, 41))
        self.golllllll.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.golllllll.setObjectName("golllllll")
        self.to_mark = QtWidgets.QPushButton(self.centralwidget)
        self.to_mark.setGeometry(QtCore.QRect(110, 330, 91, 23))
        self.to_mark.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border: none;")
        self.to_mark.setObjectName("to_mark")
        self.goll = QtWidgets.QTextBrowser(self.centralwidget)
        self.goll.setGeometry(QtCore.QRect(0, 100, 131, 61))
        self.goll.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.goll.setObjectName("goll")
        self.ye_mark = QtWidgets.QPushButton(self.centralwidget)
        self.ye_mark.setGeometry(QtCore.QRect(10, 330, 91, 23))
        self.ye_mark.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border: none;")
        self.ye_mark.setObjectName("ye_mark")
        self.gollllllll = QtWidgets.QTextBrowser(self.centralwidget)
        self.gollllllll.setGeometry(QtCore.QRect(110, 280, 111, 41))
        self.gollllllll.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.gollllllll.setObjectName("gollllllll")
        self.gollllll = QtWidgets.QTextBrowser(self.centralwidget)
        self.gollllll.setGeometry(QtCore.QRect(530, 10, 256, 61))
        self.gollllll.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.gollllll.setObjectName("gollllll")
        self.change = QtWidgets.QPushButton(self.centralwidget)
        self.change.setGeometry(QtCore.QRect(10, 670, 191, 41))
        self.change.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border: none;")
        self.change.setObjectName("change")
        self.Name = QtWidgets.QLabel(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(100, 20, 220, 31))
        self.Name.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 15pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border: none;")
        self.Name.setText("")
        self.Name.setObjectName("Name")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 360, 141, 41))
        self.textBrowser.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.textBrowser.setObjectName("textBrowser")
        self.start = QtWidgets.QLabel(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(120, 70, 320, 31))
        self.start.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt \"MS Shell Dlg 2\";")
        self.start.setText("")
        self.start.setObjectName("start")
        self.finish = QtWidgets.QLabel(self.centralwidget)
        self.finish.setGeometry(QtCore.QRect(110, 120, 341, 31))
        self.finish.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt \"MS Shell Dlg 2\";")
        self.finish.setText("")
        self.finish.setObjectName("finish")
        self.days_left = QtWidgets.QLabel(self.centralwidget)
        self.days_left.setGeometry(QtCore.QRect(160, 190, 320, 31))
        self.days_left.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;\n"
"color: rgb(255, 255, 255);\n"
"font: 15pt \"MS Shell Dlg 2\";")
        self.days_left.setText("")
        self.days_left.setObjectName("days_left")
        self.weekdays = QtWidgets.QLabel(self.centralwidget)
        self.weekdays.setGeometry(QtCore.QRect(155, 242, 320, 31))
        self.weekdays.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.weekdays.setText("")
        self.weekdays.setObjectName("weekdays")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 360, 371, 171))
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;\n"
"color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.golllllllllll = QtWidgets.QTextBrowser(self.centralwidget)
        self.golllllllllll.setGeometry(QtCore.QRect(220, 640, 171, 61))
        self.golllllllllll.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.golllllllllll.setObjectName("golllllllllll")
        self.Index = QtWidgets.QLineEdit(self.centralwidget)
        self.Index.setGeometry(QtCore.QRect(420, 620, 81, 81))
        self.Index.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.Index.setText("")
        self.Index.setObjectName("Index")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(-20, 600, 141, 41))
        self.textBrowser_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.Name_2 = QtWidgets.QLabel(self.centralwidget)
        self.Name_2.setGeometry(QtCore.QRect(100, 600, 220, 31))
        self.Name_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 15pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border: none;")
        self.Name_2.setText("")
        self.Name_2.setObjectName("Name_2")
        Goals.setCentralWidget(self.centralwidget)

        self.retranslateUi(Goals)
        QtCore.QMetaObject.connectSlotsByName(Goals)

    def retranslateUi(self, Goals):
        _translate = QtCore.QCoreApplication.translate
        Goals.setWindowTitle(_translate("Goals", "MainWindow"))
        self.golllllllll.setHtml(_translate("Goals", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Завтра</span></p></body></html>"))
        self.tm_mark.setText(_translate("Goals", "Отметить"))
        self.gol.setHtml(_translate("Goals", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Имя:</span></p></body></html>"))
        self.gollllllllll.setHtml(_translate("Goals", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Дата начала:</span></p></body></html>"))
        self.golll.setHtml(_translate("Goals", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Количество дней:</span></p></body></html>"))
        self.create.setText(_translate("Goals", "Создать новую цель"))
        item = self.lisst.horizontalHeaderItem(0)
        item.setText(_translate("Goals", "Название цели:"))
        self.gollll.setHtml(_translate("Goals", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Дни недели:</span></p></body></html>"))
        self.golllllll.setHtml(_translate("Goals", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Вчера</span></p></body></html>"))
        self.to_mark.setText(_translate("Goals", "Отметить"))
        self.goll.setHtml(_translate("Goals", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Дата конца:</span></p></body></html>"))
        self.ye_mark.setText(_translate("Goals", "Отметить"))
        self.gollllllll.setHtml(_translate("Goals", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Сегодня</span></p></body></html>"))
        self.gollllll.setHtml(_translate("Goals", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#000000;\">Все цели:</span></p></body></html>"))
        self.change.setText(_translate("Goals", "Редактировать цель"))
        self.textBrowser.setHtml(_translate("Goals", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Описание:</span></p></body></html>"))
        self.label.setText(_translate("Goals", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.golllllllllll.setHtml(_translate("Goals", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Перейти к цели номер:</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Goals", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Цель:</span></p></body></html>"))
