# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow_jeu.ui'
#
# Created: Sun Jan 08 19:00:56 2012
#      by: pyside-uic 0.2.13 running on PySide 1.0.9
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(899, 673)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_4 = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(40, 30, 821, 509))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.phraseLabel = QtGui.QLabel(self.verticalLayoutWidget_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phraseLabel.sizePolicy().hasHeightForWidth())
        self.phraseLabel.setSizePolicy(sizePolicy)
        self.phraseLabel.setObjectName("phraseLabel")
        self.verticalLayout_4.addWidget(self.phraseLabel)
        self.labelMessage = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.labelMessage.setText("")
        self.labelMessage.setObjectName("labelMessage")
        self.verticalLayout_4.addWidget(self.labelMessage)
        self.textEditEntry = QtGui.QTextEdit(self.verticalLayoutWidget_4)
        self.textEditEntry.setMaximumSize(QtCore.QSize(1000, 30))
        self.textEditEntry.setBaseSize(QtCore.QSize(0, 0))
        self.textEditEntry.setObjectName("textEditEntry")
        self.verticalLayout_4.addWidget(self.textEditEntry)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.label = QtGui.QLabel(self.verticalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4.addLayout(self.gridLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.passerButton = QtGui.QPushButton(self.verticalLayoutWidget_4)
        self.passerButton.setObjectName("passerButton")
        self.horizontalLayout.addWidget(self.passerButton)
        self.indiceButton = QtGui.QPushButton(self.verticalLayoutWidget_4)
        self.indiceButton.setObjectName("indiceButton")
        self.horizontalLayout.addWidget(self.indiceButton)
        self.validerButton = QtGui.QPushButton(self.verticalLayoutWidget_4)
        self.validerButton.setObjectName("validerButton")
        self.horizontalLayout.addWidget(self.validerButton)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.scoreLabel = QtGui.QLabel(self.verticalLayoutWidget_4)
        self.scoreLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.scoreLabel.setObjectName("scoreLabel")
        self.verticalLayout_3.addWidget(self.scoreLabel)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 899, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.phraseLabel.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Indices", None, QtGui.QApplication.UnicodeUTF8))
        self.passerButton.setText(QtGui.QApplication.translate("MainWindow", "Passer", None, QtGui.QApplication.UnicodeUTF8))
        self.indiceButton.setText(QtGui.QApplication.translate("MainWindow", "Indice", None, QtGui.QApplication.UnicodeUTF8))
        self.validerButton.setText(QtGui.QApplication.translate("MainWindow", "Valider", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Score", None, QtGui.QApplication.UnicodeUTF8))
        self.scoreLabel.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))

