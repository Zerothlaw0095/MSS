# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_sideview_options.ui'
#
# Created: Wed Feb 23 14:54:17 2011
#      by: PyQt4 UI code generator 4.6.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


class Ui_SideViewOptionsDialog(object):
    def setupUi(self, SideViewOptionsDialog):
        SideViewOptionsDialog.setObjectName("SideViewOptionsDialog")
        SideViewOptionsDialog.resize(460, 519)
        self.verticalLayout_4 = QtGui.QVBoxLayout(SideViewOptionsDialog)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox = QtGui.QGroupBox(SideViewOptionsDialog)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.sbPbot = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbPbot.sizePolicy().hasHeightForWidth())
        self.sbPbot.setSizePolicy(sizePolicy)
        self.sbPbot.setMinimum(30)
        self.sbPbot.setMaximum(1100)
        self.sbPbot.setProperty("value", 1050)
        self.sbPbot.setObjectName("sbPbot")
        self.horizontalLayout.addWidget(self.sbPbot)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.sbPtop = QtGui.QSpinBox(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sbPtop.sizePolicy().hasHeightForWidth())
        self.sbPtop.setSizePolicy(sizePolicy)
        self.sbPtop.setMinimum(20)
        self.sbPtop.setMaximum(1050)
        self.sbPtop.setProperty("value", 200)
        self.sbPtop.setObjectName("sbPtop")
        self.horizontalLayout.addWidget(self.sbPtop)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(SideViewOptionsDialog)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cbDrawFlightLevels = QtGui.QCheckBox(self.groupBox_2)
        self.cbDrawFlightLevels.setObjectName("cbDrawFlightLevels")
        self.verticalLayout_2.addWidget(self.cbDrawFlightLevels)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidget = QtGui.QTableWidget(self.groupBox_2)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.horizontalLayout_3.addWidget(self.tableWidget)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.btAdd = QtGui.QPushButton(self.groupBox_2)
        self.btAdd.setObjectName("btAdd")
        self.verticalLayout.addWidget(self.btAdd)
        self.btDelete = QtGui.QPushButton(self.groupBox_2)
        self.btDelete.setObjectName("btDelete")
        self.verticalLayout.addWidget(self.btDelete)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(SideViewOptionsDialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cbDrawFlightTrack = QtGui.QCheckBox(self.groupBox_3)
        self.cbDrawFlightTrack.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbDrawFlightTrack.sizePolicy().hasHeightForWidth())
        self.cbDrawFlightTrack.setSizePolicy(sizePolicy)
        self.cbDrawFlightTrack.setMinimumSize(QtCore.QSize(140, 0))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(173, 173, 173))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.cbDrawFlightTrack.setPalette(palette)
        self.cbDrawFlightTrack.setChecked(True)
        self.cbDrawFlightTrack.setObjectName("cbDrawFlightTrack")
        self.horizontalLayout_4.addWidget(self.cbDrawFlightTrack)
        self.btWaypointsColour = QtGui.QPushButton(self.groupBox_3)
        self.btWaypointsColour.setMinimumSize(QtCore.QSize(140, 0))
        self.btWaypointsColour.setObjectName("btWaypointsColour")
        self.horizontalLayout_4.addWidget(self.btWaypointsColour)
        self.btVerticesColour = QtGui.QPushButton(self.groupBox_3)
        self.btVerticesColour.setMinimumSize(QtCore.QSize(140, 0))
        self.btVerticesColour.setObjectName("btVerticesColour")
        self.horizontalLayout_4.addWidget(self.btVerticesColour)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cbFillFlightTrack = QtGui.QCheckBox(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbFillFlightTrack.sizePolicy().hasHeightForWidth())
        self.cbFillFlightTrack.setSizePolicy(sizePolicy)
        self.cbFillFlightTrack.setMinimumSize(QtCore.QSize(140, 0))
        self.cbFillFlightTrack.setObjectName("cbFillFlightTrack")
        self.horizontalLayout_5.addWidget(self.cbFillFlightTrack)
        self.btFillColour = QtGui.QPushButton(self.groupBox_3)
        self.btFillColour.setMinimumSize(QtCore.QSize(140, 0))
        self.btFillColour.setObjectName("btFillColour")
        self.horizontalLayout_5.addWidget(self.btFillColour)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.cbLabelFlightTrack = QtGui.QCheckBox(self.groupBox_3)
        self.cbLabelFlightTrack.setObjectName("cbLabelFlightTrack")
        self.horizontalLayout_6.addWidget(self.cbLabelFlightTrack)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.buttonBox = QtGui.QDialogButtonBox(SideViewOptionsDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_4.addWidget(self.buttonBox)

        self.retranslateUi(SideViewOptionsDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), SideViewOptionsDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), SideViewOptionsDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SideViewOptionsDialog)

    def retranslateUi(self, SideViewOptionsDialog):
        SideViewOptionsDialog.setWindowTitle(
            QtGui.QApplication.translate("SideViewOptionsDialog", "Side View Options", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("SideViewOptionsDialog", "Vertical Extent", None,
                                                            QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("SideViewOptionsDialog", "Vertical extent:", None,
                                                          QtGui.QApplication.UnicodeUTF8))
        self.sbPbot.setSuffix(
            QtGui.QApplication.translate("SideViewOptionsDialog", " hPa", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(
            QtGui.QApplication.translate("SideViewOptionsDialog", "to", None, QtGui.QApplication.UnicodeUTF8))
        self.sbPtop.setSuffix(
            QtGui.QApplication.translate("SideViewOptionsDialog", " hPa", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("SideViewOptionsDialog", "Flight Levels", None,
                                                              QtGui.QApplication.UnicodeUTF8))
        self.cbDrawFlightLevels.setText(
            QtGui.QApplication.translate("SideViewOptionsDialog", "draw the following flight levels:", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.tableWidget.horizontalHeaderItem(0).setText(
            QtGui.QApplication.translate("SideViewOptionsDialog", "flight levels", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.btAdd.setText(
            QtGui.QApplication.translate("SideViewOptionsDialog", "add", None, QtGui.QApplication.UnicodeUTF8))
        self.btDelete.setText(QtGui.QApplication.translate("SideViewOptionsDialog", "delete selected", None,
                                                           QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("SideViewOptionsDialog", "Flight Track Colours", None,
                                                              QtGui.QApplication.UnicodeUTF8))
        self.cbDrawFlightTrack.setText(QtGui.QApplication.translate("SideViewOptionsDialog", "draw flight track", None,
                                                                    QtGui.QApplication.UnicodeUTF8))
        self.btWaypointsColour.setText(
            QtGui.QApplication.translate("SideViewOptionsDialog", "colour of waypoints", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.btVerticesColour.setText(QtGui.QApplication.translate("SideViewOptionsDialog", "colour of vertices", None,
                                                                   QtGui.QApplication.UnicodeUTF8))
        self.cbFillFlightTrack.setText(QtGui.QApplication.translate("SideViewOptionsDialog", "fill flight track", None,
                                                                    QtGui.QApplication.UnicodeUTF8))
        self.btFillColour.setText(
            QtGui.QApplication.translate("SideViewOptionsDialog", "colour", None, QtGui.QApplication.UnicodeUTF8))
        self.cbLabelFlightTrack.setText(
            QtGui.QApplication.translate("SideViewOptionsDialog", "label flight track", None,
                                         QtGui.QApplication.UnicodeUTF8))