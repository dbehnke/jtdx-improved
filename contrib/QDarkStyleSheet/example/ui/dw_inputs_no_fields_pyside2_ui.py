# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dw_inputs_no_fields.ui'
#
# Created: Thu Dec 13 17:14:06 2018
#      by: pyside2-uic 2.0.0 running on PySide2 5.6.0~a1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName("DockWidget")
        DockWidget.resize(402, 405)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.dial = QtWidgets.QDial(self.dockWidgetContents)
        self.dial.setMinimumSize(QtCore.QSize(0, 0))
        self.dial.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dial.setProperty("value", 50)
        self.dial.setObjectName("dial")
        self.gridLayout.addWidget(self.dial, 2, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_25.setMinimumSize(QtCore.QSize(0, 0))
        self.label_25.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 7, 0, 1, 1)
        self.horizontalScrollBarDis = QtWidgets.QScrollBar(self.dockWidgetContents)
        self.horizontalScrollBarDis.setEnabled(False)
        self.horizontalScrollBarDis.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalScrollBarDis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalScrollBarDis.setProperty("value", 50)
        self.horizontalScrollBarDis.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBarDis.setObjectName("horizontalScrollBarDis")
        self.gridLayout.addWidget(self.horizontalScrollBarDis, 3, 2, 1, 1)
        self.verticalSlider = QtWidgets.QSlider(self.dockWidgetContents)
        self.verticalSlider.setMinimumSize(QtCore.QSize(0, 70))
        self.verticalSlider.setMaximumSize(QtCore.QSize(16777215, 70))
        self.verticalSlider.setProperty("value", 50)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.gridLayout.addWidget(self.verticalSlider, 7, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_24.setMinimumSize(QtCore.QSize(0, 0))
        self.label_24.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 4, 0, 1, 1)
        self.horizontalSlider = QtWidgets.QSlider(self.dockWidgetContents)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalSlider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalSlider.setProperty("value", 50)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 4, 1, 2, 1)
        self.horizontalSliderDis = QtWidgets.QSlider(self.dockWidgetContents)
        self.horizontalSliderDis.setEnabled(False)
        self.horizontalSliderDis.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalSliderDis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalSliderDis.setProperty("value", 50)
        self.horizontalSliderDis.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderDis.setObjectName("horizontalSliderDis")
        self.gridLayout.addWidget(self.horizontalSliderDis, 4, 2, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_23.setMinimumSize(QtCore.QSize(0, 0))
        self.label_23.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 6, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.verticalScrollBarDis = QtWidgets.QScrollBar(self.dockWidgetContents)
        self.verticalScrollBarDis.setEnabled(False)
        self.verticalScrollBarDis.setMinimumSize(QtCore.QSize(0, 70))
        self.verticalScrollBarDis.setMaximumSize(QtCore.QSize(16777215, 70))
        self.verticalScrollBarDis.setProperty("value", 50)
        self.verticalScrollBarDis.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBarDis.setObjectName("verticalScrollBarDis")
        self.gridLayout.addWidget(self.verticalScrollBarDis, 5, 2, 2, 1)
        self.label_21 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_21.setMinimumSize(QtCore.QSize(0, 0))
        self.label_21.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 8, 0, 1, 1)
        self.verticalScrollBar = QtWidgets.QScrollBar(self.dockWidgetContents)
        self.verticalScrollBar.setMinimumSize(QtCore.QSize(0, 70))
        self.verticalScrollBar.setMaximumSize(QtCore.QSize(16777215, 70))
        self.verticalScrollBar.setProperty("value", 50)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.gridLayout.addWidget(self.verticalScrollBar, 6, 1, 1, 1)
        self.comboBoxDis = QtWidgets.QComboBox(self.dockWidgetContents)
        self.comboBoxDis.setEnabled(False)
        self.comboBoxDis.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBoxDis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBoxDis.setObjectName("comboBoxDis")
        self.comboBoxDis.addItem("")
        self.comboBoxDis.addItem("")
        self.comboBoxDis.addItem("")
        self.gridLayout.addWidget(self.comboBoxDis, 1, 2, 1, 1)
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.dockWidgetContents)
        self.horizontalScrollBar.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalScrollBar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalScrollBar.setProperty("value", 50)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.gridLayout.addWidget(self.horizontalScrollBar, 3, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.dockWidgetContents)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_22.setMinimumSize(QtCore.QSize(0, 0))
        self.label_22.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_50 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName("label_50")
        self.gridLayout.addWidget(self.label_50, 9, 0, 1, 3)
        self.label_11 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_11.setMinimumSize(QtCore.QSize(0, 0))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)
        self.dialDis = QtWidgets.QDial(self.dockWidgetContents)
        self.dialDis.setEnabled(False)
        self.dialDis.setMinimumSize(QtCore.QSize(0, 0))
        self.dialDis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dialDis.setProperty("value", 50)
        self.dialDis.setObjectName("dialDis")
        self.gridLayout.addWidget(self.dialDis, 2, 2, 1, 1)
        self.verticalSliderDis = QtWidgets.QSlider(self.dockWidgetContents)
        self.verticalSliderDis.setEnabled(False)
        self.verticalSliderDis.setMinimumSize(QtCore.QSize(0, 70))
        self.verticalSliderDis.setMaximumSize(QtCore.QSize(16777215, 70))
        self.verticalSliderDis.setProperty("value", 50)
        self.verticalSliderDis.setOrientation(QtCore.Qt.Vertical)
        self.verticalSliderDis.setObjectName("verticalSliderDis")
        self.gridLayout.addWidget(self.verticalSliderDis, 7, 2, 1, 1)
        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)
        QtCore.QObject.connect(self.dial, QtCore.SIGNAL("sliderMoved(int)"), self.dialDis.setValue)
        QtCore.QObject.connect(self.horizontalScrollBar, QtCore.SIGNAL("sliderMoved(int)"), self.horizontalScrollBarDis.setValue)
        QtCore.QObject.connect(self.horizontalSlider, QtCore.SIGNAL("sliderMoved(int)"), self.horizontalSliderDis.setValue)
        QtCore.QObject.connect(self.verticalScrollBar, QtCore.SIGNAL("sliderMoved(int)"), self.verticalScrollBarDis.setValue)
        QtCore.QObject.connect(self.verticalSlider, QtCore.SIGNAL("sliderMoved(int)"), self.verticalSliderDis.setValue)
        QtCore.QObject.connect(self.comboBox, QtCore.SIGNAL("currentIndexChanged(int)"), self.comboBoxDis.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QtWidgets.QApplication.translate("DockWidget", "Inputs - No Fields", None, -1))
        self.dial.setToolTip(QtWidgets.QApplication.translate("DockWidget", "This is a tool tip", None, -1))
        self.dial.setStatusTip(QtWidgets.QApplication.translate("DockWidget", "This is a status tip", None, -1))
        self.dial.setWhatsThis(QtWidgets.QApplication.translate("DockWidget", "This is \"what is this\"", None, -1))
        self.label_25.setToolTip(QtWidgets.QApplication.translate("DockWidget", "This is a tool tip", None, -1))
        self.label_25.setStatusTip(QtWidgets.QApplication.translate("DockWidget", "This is a status tip", None, -1))
        self.label_25.setWhatsThis(QtWidgets.QApplication.translate("DockWidget", "This is \"what is this\"", None, -1))
        self.label_25.setText(QtWidgets.QApplication.translate("DockWidget", "VerticalSlider", None, -1))
        self.horizontalScrollBarDis.setToolTip(QtWidgets.QApplication.translate("DockWidget", "This is a tool tip", None, -1))
        self.horizontalScrollBarDis.setStatusTip(QtWidgets.QApplication.translate("DockWidget", "This is a status tip", None, -1))
        self.horizontalScrollBarDis.setWhatsThis(QtWidgets.QApplication.translate("DockWidget", "This is \"what is this\"", None, -1))
        self.verticalSlider.setToolTip(QtWidgets.QApplication.translate("DockWidget", "This is a tool tip", None, -1))
        self.verticalSlider.setStatusTip(QtWidgets.QApplication.translate("DockWidget", "This is a status tip", None, -1))
        self.verticalSlider.setWhatsThis(QtWidgets.QApplication.translate("DockWidget", "This is \"what is this\"", None, -1))
        self.label_24.setToolTip(QtWidgets.QApplication.translate("DockWidget", "This is a tool tip", None, -1))
        self.label_24.setStatusTip(QtWidgets.QApplication.translate("DockWidget", "This is a status tip", None, -1))
        self.label_24.setWhatsThis(QtWidgets.QApplication.translate("DockWidget", "This is \"what is this\"", None, -1))
        self.label_24.setText(QtWidgets.QApplication.translate("DockWidget", "HorizontalSlider", None, -1))
        self.horizontalSlider.setToolTip(QtWidgets.QApplication.translate("DockWidget", "This is a tool tip", None, -1))
        self.horizontalSlider.setStatusTip(QtWidgets.QApplication.translate("DockWidget", "This is a status tip", None, -1))
        self.horizontalSlider.setWhatsThis(QtWidgets.QApplication.translate("DockWidget", "This is \"what is this\"", None, -1))
        self.horizontalSliderDis.setToolTip(QtWidgets.QApplication.translate("DockWidget", "This is a tool tip", None, -1))
        self.horizontalSliderDis.setStatusTip(QtWidgets.QApplication.translate("DockWidget", "This is a status tip", None, -1))
        self.horizontalSliderDis.setWhatsThis(QtWidgets.QApplication.translate("DockWidget", "This is \"what is this\"", None, -1))
        self.label_23.setToolTip(QtWidgets.QApplication.translate("DockWidget", "This is a tool tip", None, -1))
        self.label_23.setStatusTip(QtWidgets.QApplication.translate("DockWidget", "This is a status tip", None, -1))
        self.label_23.setWhatsThis(QtWidgets.QApplication.translate("DockWidget", "This is \"what is this\"", None, -1))
        self.label_23.setText(QtWidgets.QApplication.translate("DockWidget", "VerticalScroolBar", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("DockWidget", "Disabled", None, -1))
        self.verticalScrollBarDis.setToolTip(QtWidgets.QApplication.translate("DockWidget", "This is a tool tip", None, -1))
        self.verticalScrollBarDis.setStatusTip(QtWidgets.QApplication.translate("DockWidget", "This is a status tip", None, -1))
        self.verticalScrollBarDis.setWhatsThis(QtWidgets.QApplication.translate("DockWidget", "This is \"what is this\"", None, -1))
        self.label_21.setToolTip(QtWidgets.QApplication.translate("DockWidget", "This is a tool tip", None, -1))
        self.label_21.setStatusTip(QtWidgets.QApplication.translate("DockWidget", "This is a status tip", None, -1))
        self.label_21.setWhatsThis(QtWidgets.QApplication.translate("DockWidget", "This is \"what is this\"", None, -1))
        self.label_21.setText(QtWidgets.QApplication.translate("DockWidget", "Dial", None, -1))
        self.verticalScrollBar.setToolTip(QtWidgets.QApplication.translate("DockWidget", "This is a tool tip", None, -1))
        self.verticalScrollBar.setStatusTip(QtWidgets.QApplication.translate("DockWidget", "This is a status tip", None, -1))
        self.verticalScrollBar.setWhatsThis(QtWidgets.QApplication.translate("DockWidget", "This is \"what is this\"", None, -1))
        self.comboBoxDis.setToolTip(QtWidgets.QApplication.translate("DockWidget", "This is a tool tip", None, -1))
        self.comboBoxDis.setStatusTip(QtWidgets.QApplication.translate("DockWidget", "This is a status tip", None, -1))
        self.comboBoxDis.setWhatsThis(QtWidgets.QApplication.translate("DockWidget", "This is \"what is this\"", None, -1))
        self.comboBoxDis.setItemText(0, QtWidgets.QApplication.translate("DockWidget", "ComboBox A", None, -1))
        self.comboBoxDis.setItemText(1, QtWidgets.QApplication.translate("DockWidget", "ComboBox B", None, -1))
        self.comboBoxDis.setItemText(2, QtWidgets.QApplication.translate("DockWidget", "ComboBox C", None, -1))
        self.horizontalScrollBar.setToolTip(QtWidgets.QApplication.translate("DockWidget", "This is a tool tip", None, -1))
        self.horizontalScrollBar.setStatusTip(QtWidgets.QApplication.translate("DockWidget", "This is a status tip", None, -1))
        self.horizontalScrollBar.setWhatsThis(QtWidgets.QApplication.translate("DockWidget", "This is \"what is this\"", None, -1))
        self.comboBox.setToolTip(QtWidgets.QApplication.translate("DockWidget", "This is a tool tip", None, -1))
        self.comboBox.setStatusTip(QtWidgets.QApplication.translate("DockWidget", "This is a status tip", None, -1))
        self.comboBox.setWhatsThis(QtWidgets.QApplication.translate("DockWidget", "This is \"what is this\"", None, -1))
        self.comboBox.setItemText(0, QtWidgets.QApplication.translate("DockWidget", "ComboBox A", None, -1))
        self.comboBox.setItemText(1, QtWidgets.QApplication.translate("DockWidget", "ComboBox B", None, -1))
        self.comboBox.setItemText(2, QtWidgets.QApplication.translate("DockWidget", "ComboBox C", None, -1))
        self.label_22.setToolTip(QtWidgets.QApplication.translate("DockWidget", "This is a tool tip", None, -1))
        self.label_22.setStatusTip(QtWidgets.QApplication.translate("DockWidget", "This is a status tip", None, -1))
        self.label_22.setWhatsThis(QtWidgets.QApplication.translate("DockWidget", "This is \"what is this\"", None, -1))
        self.label_22.setText(QtWidgets.QApplication.translate("DockWidget", "HorizontalScroolBar", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("DockWidget", "Enabled", None, -1))
        self.label_50.setToolTip(QtWidgets.QApplication.translate("DockWidget", "This is a tool tip", None, -1))
        self.label_50.setStatusTip(QtWidgets.QApplication.translate("DockWidget", "This is a status tip", None, -1))
        self.label_50.setWhatsThis(QtWidgets.QApplication.translate("DockWidget", "This is \"what is this\"", None, -1))
        self.label_50.setText(QtWidgets.QApplication.translate("DockWidget", "Inside DockWidget", None, -1))
        self.label_11.setToolTip(QtWidgets.QApplication.translate("DockWidget", "This is a tool tip", None, -1))
        self.label_11.setStatusTip(QtWidgets.QApplication.translate("DockWidget", "This is a status tip", None, -1))
        self.label_11.setWhatsThis(QtWidgets.QApplication.translate("DockWidget", "This is \"what is this\"", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("DockWidget", "ComboBox", None, -1))
        self.dialDis.setToolTip(QtWidgets.QApplication.translate("DockWidget", "This is a tool tip", None, -1))
        self.dialDis.setStatusTip(QtWidgets.QApplication.translate("DockWidget", "This is a status tip", None, -1))
        self.dialDis.setWhatsThis(QtWidgets.QApplication.translate("DockWidget", "This is \"what is this\"", None, -1))
        self.verticalSliderDis.setToolTip(QtWidgets.QApplication.translate("DockWidget", "This is a tool tip", None, -1))
        self.verticalSliderDis.setStatusTip(QtWidgets.QApplication.translate("DockWidget", "This is a status tip", None, -1))
        self.verticalSliderDis.setWhatsThis(QtWidgets.QApplication.translate("DockWidget", "This is \"what is this\"", None, -1))

