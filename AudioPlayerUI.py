# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'audioplayerdemo.ui'
#
# Created: Fri Jan 30 22:34:39 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AudioPlayerDemo(object):
    def setupUi(self, AudioPlayerDemo):
        AudioPlayerDemo.setObjectName("AudioPlayerDemo")
        AudioPlayerDemo.resize(580, 500)
        self.centralWidget = QtGui.QWidget(AudioPlayerDemo)
        self.centralWidget.setObjectName("centralWidget")
        self.label = QtGui.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 580, 385))
        self.label.setStyleSheet("background: url(\"img2.jpg\")")
        self.label.setText("")
        self.label.setObjectName("label")
        self.button = QtGui.QPushButton(self.centralWidget)
        self.button.setGeometry(QtCore.QRect(10, 393, 84, 41))
        self.button.setObjectName("button")
        self.horizontalSlider = QtGui.QSlider(self.centralWidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(110, 400, 451, 20))
        self.horizontalSlider.setProperty("value", 24)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        AudioPlayerDemo.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(AudioPlayerDemo)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 580, 30))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtGui.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        AudioPlayerDemo.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(AudioPlayerDemo)
        self.mainToolBar.setObjectName("mainToolBar")
        AudioPlayerDemo.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(AudioPlayerDemo)
        self.statusBar.setObjectName("statusBar")
        AudioPlayerDemo.setStatusBar(self.statusBar)
        self.actionOpen = QtGui.QAction(AudioPlayerDemo)
        self.actionOpen.setObjectName("actionOpen")
        self.actionQuit = QtGui.QAction(AudioPlayerDemo)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionQuit)
        self.menuBar.addAction(self.menuFile.menuAction())

        self.retranslateUi(AudioPlayerDemo)
        QtCore.QMetaObject.connectSlotsByName(AudioPlayerDemo)

    def retranslateUi(self, AudioPlayerDemo):
        AudioPlayerDemo.setWindowTitle(QtGui.QApplication.translate("AudioPlayerDemo", "AudioPlayerDemo", None, QtGui.QApplication.UnicodeUTF8))
        self.button.setText(QtGui.QApplication.translate("AudioPlayerDemo", "Play", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("AudioPlayerDemo", "Fi&le", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("AudioPlayerDemo", "&Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("AudioPlayerDemo", "&Quit", None, QtGui.QApplication.UnicodeUTF8))

