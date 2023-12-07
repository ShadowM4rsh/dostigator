from PyQt5 import QtCore, QtGui, QtWidgets


class GoalMainWindow(object):
    def setupUii(self, GoalEdit):
        GoalEdit.setObjectName("GoalEdit")
        GoalEdit.resize(789, 550)
        self.centralwidget = QtWidgets.QWidget(GoalEdit)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 791, 551))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("kosmos-planeta-neobyatnye-prostory-kosmosa-wny2.jpg"))
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 101, 51))
        self.textBrowser.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 60, 121, 61))
        self.textEdit.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.textEdit.setObjectName("textEdit")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(0, 130, 121, 61))
        self.textBrowser_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(0, 200, 161, 51))
        self.textBrowser_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.error_marker = QtWidgets.QLabel(self.centralwidget)
        self.error_marker.setGeometry(QtCore.QRect(10, 480, 641, 71))
        self.error_marker.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 0, 0);\n"
"font: 75 8pt \"MS Shell Dlg 2\";\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"border: none;")
        self.error_marker.setText("")
        self.error_marker.setObjectName("error_marker")
        self.name_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.name_edit.setGeometry(QtCore.QRect(90, 20, 201, 31))
        self.name_edit.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.name_edit.setObjectName("name_edit")
        self.iteration_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.iteration_edit.setGeometry(QtCore.QRect(150, 200, 511, 31))
        self.iteration_edit.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.iteration_edit.setObjectName("iteration_edit")
        self.date_start = QtWidgets.QDateEdit(self.centralwidget)
        self.date_start.setGeometry(QtCore.QRect(120, 70, 131, 41))
        self.date_start.setObjectName("date_start")
        self.date_finish = QtWidgets.QDateEdit(self.centralwidget)
        self.date_finish.setGeometry(QtCore.QRect(120, 140, 131, 41))
        self.date_finish.setObjectName("date_finish")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(0, 240, 131, 41))
        self.textBrowser_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.description_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.description_edit.setGeometry(QtCore.QRect(140, 240, 601, 161))
        self.description_edit.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.description_edit.setObjectName("description_edit")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_6.setGeometry(QtCore.QRect(0, 440, 131, 41))
        self.textBrowser_6.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.goal_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.goal_edit.setGeometry(QtCore.QRect(100, 440, 511, 31))
        self.goal_edit.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border: none;")
        self.goal_edit.setObjectName("goal_edit")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(630, 10, 151, 41))
        self.submit.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgba(255, 255, 255, 0);\n"
"")
        self.submit.setObjectName("submit")
        GoalEdit.setCentralWidget(self.centralwidget)

        self.retranslateUi(GoalEdit)
        QtCore.QMetaObject.connectSlotsByName(GoalEdit)

    def retranslateUi(self, GoalEdit):
        _translate = QtCore.QCoreApplication.translate
        GoalEdit.setWindowTitle(_translate("GoalEdit", "MainWindow"))
        self.textBrowser.setHtml(_translate("GoalEdit", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Имя:</span></p></body></html>"))
        self.textEdit.setHtml(_translate("GoalEdit", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Дата начала:</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("GoalEdit", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Дата конца:</span></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("GoalEdit", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Дни недели:</span></p></body></html>"))
        self.name_edit.setText(_translate("GoalEdit", "Введите название."))
        self.iteration_edit.setText(_translate("GoalEdit", "Понедельник,Вторник"))
        self.textBrowser_5.setHtml(_translate("GoalEdit", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Описание:</span></p></body></html>"))
        self.description_edit.setText(_translate("GoalEdit", "Введите описание."))
        self.textBrowser_6.setHtml(_translate("GoalEdit", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Цель:</span></p></body></html>"))
        self.goal_edit.setText(_translate("GoalEdit", "Введите название."))
        self.submit.setText(_translate("GoalEdit", "Подтвердить"))