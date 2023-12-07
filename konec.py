from PyQt5 import QtCore, QtGui, QtWidgets


class Kon_MainWindow(object):
    def __init__(self, konec):
        konec.setObjectName("konec")
        konec.resize(1090, 850)
        self.centralwidget = QtWidgets.QWidget(konec)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -10, 801, 591))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("zakat.jpg"))
        self.label.setObjectName("label")
        self.tb1 = QtWidgets.QTextBrowser(self.centralwidget)
        self.tb1.setGeometry(QtCore.QRect(100, 10, 651, 101))
        self.tb1.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                                       "border: none;")
        self.tb1.setObjectName("tb1")
        self.tb2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.tb2.setGeometry(QtCore.QRect(10, 250, 321, 61))
        self.tb2.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                               "border: none;")
        self.tb2.setObjectName("tb2")
        self.tb3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.tb3.setGeometry(QtCore.QRect(0, 350, 581, 101))
        self.tb3.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                               "border: none;")
        self.tb3.setObjectName("tb3")
        self.tb4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.tb4.setGeometry(QtCore.QRect(540, 510, 256, 141))
        self.tb4.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
                               "border: none;")
        self.tb4.setObjectName("tb4")
        konec.setCentralWidget(self.centralwidget)