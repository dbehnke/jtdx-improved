# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dw_inputs_no_fields.ui'
#
# Created: Thu Dec 13 17:14:06 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName("DockWidget")
        DockWidget.resize(402, 405)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.dial = QtGui.QDial(self.dockWidgetContents)
        self.dial.setMinimumSize(QtCore.QSize(0, 0))
        self.dial.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dial.setProperty("value", 50)
        self.dial.setObjectName("dial")
        self.gridLayout.addWidget(self.dial, 2, 1, 1, 1)
        self.label_25 = QtGui.QLabel(self.dockWidgetContents)
        self.label_25.setMinimumSize(QtCore.QSize(0, 0))
        self.label_25.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 7, 0, 1, 1)
        self.horizontalScrollBarDis = QtGui.QScrollBar(self.dockWidgetContents)
        self.horizontalScrollBarDis.setEnabled(False)
        self.horizontalScrollBarDis.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalScrollBarDis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalScrollBarDis.setProperty("value", 50)
        self.horizontalScrollBarDis.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBarDis.setObjectName("horizontalScrollBarDis")
        self.gridLayout.addWidget(self.horizontalScrollBarDis, 3, 2, 1, 1)
        self.verticalSlider = QtGui.QSlider(self.dockWidgetContents)
        self.verticalSlider.setMinimumSize(QtCore.QSize(0, 70))
        self.verticalSlider.setMaximumSize(QtCore.QSize(16777215, 70))
        self.verticalSlider.setProperty("value", 50)
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.gridLayout.addWidget(self.verticalSlider, 7, 1, 1, 1)
        self.label_24 = QtGui.QLabel(self.dockWidgetContents)
        self.label_24.setMinimumSize(QtCore.QSize(0, 0))
        self.label_24.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 4, 0, 1, 1)
        self.horizontalSlider = QtGui.QSlider(self.dockWidgetContents)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalSlider.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalSlider.setProperty("value", 50)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 4, 1, 2, 1)
        self.horizontalSliderDis = QtGui.QSlider(self.dockWidgetContents)
        self.horizontalSliderDis.setEnabled(False)
        self.horizontalSliderDis.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalSliderDis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalSliderDis.setProperty("value", 50)
        self.horizontalSliderDis.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSliderDis.setObjectName("horizontalSliderDis")
        self.gridLayout.addWidget(self.horizontalSliderDis, 4, 2, 1, 1)
        self.label_23 = QtGui.QLabel(self.dockWidgetContents)
        self.label_23.setMinimumSize(QtCore.QSize(0, 0))
        self.label_23.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 6, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.verticalScrollBarDis = QtGui.QScrollBar(self.dockWidgetContents)
        self.verticalScrollBarDis.setEnabled(False)
        self.verticalScrollBarDis.setMinimumSize(QtCore.QSize(0, 70))
        self.verticalScrollBarDis.setMaximumSize(QtCore.QSize(16777215, 70))
        self.verticalScrollBarDis.setProperty("value", 50)
        self.verticalScrollBarDis.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBarDis.setObjectName("verticalScrollBarDis")
        self.gridLayout.addWidget(self.verticalScrollBarDis, 5, 2, 2, 1)
        self.label_21 = QtGui.QLabel(self.dockWidgetContents)
        self.label_21.setMinimumSize(QtCore.QSize(0, 0))
        self.label_21.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 2, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 0, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 8, 0, 1, 1)
        self.verticalScrollBar = QtGui.QScrollBar(self.dockWidgetContents)
        self.verticalScrollBar.setMinimumSize(QtCore.QSize(0, 70))
        self.verticalScrollBar.setMaximumSize(QtCore.QSize(16777215, 70))
        self.verticalScrollBar.setProperty("value", 50)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.gridLayout.addWidget(self.verticalScrollBar, 6, 1, 1, 1)
        self.comboBoxDis = QtGui.QComboBox(self.dockWidgetContents)
        self.comboBoxDis.setEnabled(False)
        self.comboBoxDis.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBoxDis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBoxDis.setObjectName("comboBoxDis")
        self.comboBoxDis.addItem("")
        self.comboBoxDis.addItem("")
        self.comboBoxDis.addItem("")
        self.gridLayout.addWidget(self.comboBoxDis, 1, 2, 1, 1)
        self.horizontalScrollBar = QtGui.QScrollBar(self.dockWidgetContents)
        self.horizontalScrollBar.setMinimumSize(QtCore.QSize(0, 0))
        self.horizontalScrollBar.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalScrollBar.setProperty("value", 50)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.gridLayout.addWidget(self.horizontalScrollBar, 3, 1, 1, 1)
        self.comboBox = QtGui.QComboBox(self.dockWidgetContents)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 1, 1, 1)
        self.label_22 = QtGui.QLabel(self.dockWidgetContents)
        self.label_22.setMinimumSize(QtCore.QSize(0, 0))
        self.label_22.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 3, 0, 1, 1)
        self.label = QtGui.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.label_50 = QtGui.QLabel(self.dockWidgetContents)
        self.label_50.setAlignment(QtCore.Qt.AlignCenter)
        self.label_50.setObjectName("label_50")
        self.gridLayout.addWidget(self.label_50, 9, 0, 1, 3)
        self.label_11 = QtGui.QLabel(self.dockWidgetContents)
        self.label_11.setMinimumSize(QtCore.QSize(0, 0))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)
        self.dialDis = QtGui.QDial(self.dockWidgetContents)
        self.dialDis.setEnabled(False)
        self.dialDis.setMinimumSize(QtCore.QSize(0, 0))
        self.dialDis.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dialDis.setProperty("value", 50)
        self.dialDis.setObjectName("dialDis")
        self.gridLayout.addWidget(self.dialDis, 2, 2, 1, 1)
        self.verticalSliderDis = QtGui.QSlider(self.dockWidgetContents)
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
        DockWidget.setWindowTitle(QtGui.QApplication.translate("DockWidget", "Inputs - No Fields", None, QtGui.QApplication.UnicodeUTF8))
        self.dial.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.dial.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.dial.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("DockWidget", "VerticalSlider", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalScrollBarDis.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalScrollBarDis.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalScrollBarDis.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalSlider.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalSlider.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalSlider.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("DockWidget", "HorizontalSlider", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalSlider.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalSlider.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalSlider.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalSliderDis.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalSliderDis.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalSliderDis.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("DockWidget", "VerticalScroolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DockWidget", "Disabled", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalScrollBarDis.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalScrollBarDis.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalScrollBarDis.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("DockWidget", "Dial", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalScrollBar.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalScrollBar.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalScrollBar.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDis.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDis.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDis.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDis.setItemText(0, QtGui.QApplication.translate("DockWidget", "ComboBox A", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDis.setItemText(1, QtGui.QApplication.translate("DockWidget", "ComboBox B", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBoxDis.setItemText(2, QtGui.QApplication.translate("DockWidget", "ComboBox C", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalScrollBar.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalScrollBar.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.horizontalScrollBar.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("DockWidget", "ComboBox A", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("DockWidget", "ComboBox B", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("DockWidget", "ComboBox C", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("DockWidget", "HorizontalScroolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DockWidget", "Enabled", None, QtGui.QApplication.UnicodeUTF8))
        self.label_50.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_50.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_50.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_50.setText(QtGui.QApplication.translate("DockWidget", "Inside DockWidget", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("DockWidget", "ComboBox", None, QtGui.QApplication.UnicodeUTF8))
        self.dialDis.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.dialDis.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.dialDis.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalSliderDis.setToolTip(QtGui.QApplication.translate("DockWidget", "This is a tool tip", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalSliderDis.setStatusTip(QtGui.QApplication.translate("DockWidget", "This is a status tip", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalSliderDis.setWhatsThis(QtGui.QApplication.translate("DockWidget", "This is \"what is this\"", None, QtGui.QApplication.UnicodeUTF8))

