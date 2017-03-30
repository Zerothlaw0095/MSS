# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_wms_dockwidget.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WMSDockWidget(object):
    def setupUi(self, WMSDockWidget):
        WMSDockWidget.setObjectName("WMSDockWidget")
        WMSDockWidget.resize(1001, 155)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(WMSDockWidget.sizePolicy().hasHeightForWidth())
        WMSDockWidget.setSizePolicy(sizePolicy)
        WMSDockWidget.setMinimumSize(QtCore.QSize(1001, 0))
        WMSDockWidget.setMaximumSize(QtCore.QSize(16777215, 155))
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(WMSDockWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_7 = QtWidgets.QLabel(WMSDockWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.cbWMS_URL = QtWidgets.QComboBox(WMSDockWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbWMS_URL.sizePolicy().hasHeightForWidth())
        self.cbWMS_URL.setSizePolicy(sizePolicy)
        self.cbWMS_URL.setEditable(True)
        self.cbWMS_URL.setObjectName("cbWMS_URL")
        self.cbWMS_URL.addItem("")
        self.cbWMS_URL.addItem("")
        self.horizontalLayout_9.addWidget(self.cbWMS_URL)
        self.btGetCapabilities = QtWidgets.QPushButton(WMSDockWidget)
        self.btGetCapabilities.setObjectName("btGetCapabilities")
        self.horizontalLayout_9.addWidget(self.btGetCapabilities)
        self.pbViewCapabilities = QtWidgets.QPushButton(WMSDockWidget)
        self.pbViewCapabilities.setObjectName("pbViewCapabilities")
        self.horizontalLayout_9.addWidget(self.pbViewCapabilities)
        self.line_4 = QtWidgets.QFrame(WMSDockWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.horizontalLayout_9.addWidget(self.line_4)
        self.cbAutoUpdate = QtWidgets.QCheckBox(WMSDockWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbAutoUpdate.sizePolicy().hasHeightForWidth())
        self.cbAutoUpdate.setSizePolicy(sizePolicy)
        self.cbAutoUpdate.setMaximumSize(QtCore.QSize(200, 16777215))
        self.cbAutoUpdate.setObjectName("cbAutoUpdate")
        self.horizontalLayout_9.addWidget(self.cbAutoUpdate)
        self.btGetMap = QtWidgets.QPushButton(WMSDockWidget)
        self.btGetMap.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btGetMap.setFont(font)
        self.btGetMap.setObjectName("btGetMap")
        self.horizontalLayout_9.addWidget(self.btGetMap)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(WMSDockWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(40, 0))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.cbLayer = QtWidgets.QComboBox(WMSDockWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbLayer.sizePolicy().hasHeightForWidth())
        self.cbLayer.setSizePolicy(sizePolicy)
        self.cbLayer.setMinimumSize(QtCore.QSize(200, 0))
        self.cbLayer.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cbLayer.setToolTip("")
        self.cbLayer.setStyleSheet("QComboBox QAbstractItemView { min-width: 800px; }")
        self.cbLayer.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.cbLayer.setMinimumContentsLength(0)
        self.cbLayer.setObjectName("cbLayer")
        self.cbLayer.addItem("")
        self.cbLayer.addItem("")
        self.cbLayer.addItem("")
        self.horizontalLayout.addWidget(self.cbLayer)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_11 = QtWidgets.QLabel(WMSDockWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy)
        self.label_11.setMinimumSize(QtCore.QSize(40, 0))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_2.addWidget(self.label_11)
        self.cbStyle = QtWidgets.QComboBox(WMSDockWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbStyle.sizePolicy().hasHeightForWidth())
        self.cbStyle.setSizePolicy(sizePolicy)
        self.cbStyle.setMinimumSize(QtCore.QSize(200, 0))
        self.cbStyle.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cbStyle.setStyleSheet("QComboBox QAbstractItemView { min-width: 600px; }")
        self.cbStyle.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.cbStyle.setFrame(True)
        self.cbStyle.setObjectName("cbStyle")
        self.cbStyle.addItem("")
        self.horizontalLayout_2.addWidget(self.cbStyle)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.teLayerAbstract = QtWidgets.QTextEdit(WMSDockWidget)
        self.teLayerAbstract.setMinimumSize(QtCore.QSize(242, 0))
        self.teLayerAbstract.setReadOnly(True)
        self.teLayerAbstract.setObjectName("teLayerAbstract")
        self.verticalLayout.addWidget(self.teLayerAbstract)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.line_2 = QtWidgets.QFrame(WMSDockWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_5.addWidget(self.line_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.cbInitTime = QtWidgets.QComboBox(WMSDockWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbInitTime.sizePolicy().hasHeightForWidth())
        self.cbInitTime.setSizePolicy(sizePolicy)
        self.cbInitTime.setMinimumSize(QtCore.QSize(180, 0))
        self.cbInitTime.setMaximumSize(QtCore.QSize(250, 16777215))
        self.cbInitTime.setObjectName("cbInitTime")
        self.cbInitTime.addItem("")
        self.horizontalLayout_3.addWidget(self.cbInitTime)
        self.tbInitTime_cbback = QtWidgets.QToolButton(WMSDockWidget)
        self.tbInitTime_cbback.setObjectName("tbInitTime_cbback")
        self.horizontalLayout_3.addWidget(self.tbInitTime_cbback)
        self.tbInitTime_cbfwd = QtWidgets.QToolButton(WMSDockWidget)
        self.tbInitTime_cbfwd.setObjectName("tbInitTime_cbfwd")
        self.horizontalLayout_3.addWidget(self.tbInitTime_cbfwd)
        self.dteInitTime = QtWidgets.QDateTimeEdit(WMSDockWidget)
        self.dteInitTime.setMinimumSize(QtCore.QSize(160, 0))
        self.dteInitTime.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.dteInitTime.setFont(font)
        self.dteInitTime.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToPreviousValue)
        self.dteInitTime.setCalendarPopup(False)
        self.dteInitTime.setTimeSpec(QtCore.Qt.UTC)
        self.dteInitTime.setObjectName("dteInitTime")
        self.horizontalLayout_3.addWidget(self.dteInitTime)
        self.tbInitTime_back = QtWidgets.QToolButton(WMSDockWidget)
        self.tbInitTime_back.setObjectName("tbInitTime_back")
        self.horizontalLayout_3.addWidget(self.tbInitTime_back)
        self.cbInitTime_step = QtWidgets.QComboBox(WMSDockWidget)
        self.cbInitTime_step.setObjectName("cbInitTime_step")
        self.horizontalLayout_3.addWidget(self.cbInitTime_step)
        self.tbInitTime_fwd = QtWidgets.QToolButton(WMSDockWidget)
        self.tbInitTime_fwd.setObjectName("tbInitTime_fwd")
        self.horizontalLayout_3.addWidget(self.tbInitTime_fwd)
        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 2, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.cbValidTime = QtWidgets.QComboBox(WMSDockWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbValidTime.sizePolicy().hasHeightForWidth())
        self.cbValidTime.setSizePolicy(sizePolicy)
        self.cbValidTime.setMinimumSize(QtCore.QSize(180, 0))
        self.cbValidTime.setMaximumSize(QtCore.QSize(250, 16777215))
        self.cbValidTime.setObjectName("cbValidTime")
        self.horizontalLayout_8.addWidget(self.cbValidTime)
        self.tbValidTime_cbback = QtWidgets.QToolButton(WMSDockWidget)
        self.tbValidTime_cbback.setArrowType(QtCore.Qt.NoArrow)
        self.tbValidTime_cbback.setObjectName("tbValidTime_cbback")
        self.horizontalLayout_8.addWidget(self.tbValidTime_cbback)
        self.tbValidTime_cbfwd = QtWidgets.QToolButton(WMSDockWidget)
        self.tbValidTime_cbfwd.setObjectName("tbValidTime_cbfwd")
        self.horizontalLayout_8.addWidget(self.tbValidTime_cbfwd)
        self.dteValidTime = QtWidgets.QDateTimeEdit(WMSDockWidget)
        self.dteValidTime.setMinimumSize(QtCore.QSize(160, 0))
        self.dteValidTime.setMaximumSize(QtCore.QSize(160, 16777215))
        self.dteValidTime.setDate(QtCore.QDate(2010, 1, 17))
        self.dteValidTime.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(7, 0, 0)))
        self.dteValidTime.setMinimumDate(QtCore.QDate(2000, 1, 1))
        self.dteValidTime.setMinimumTime(QtCore.QTime(7, 0, 0))
        self.dteValidTime.setCalendarPopup(False)
        self.dteValidTime.setTimeSpec(QtCore.Qt.UTC)
        self.dteValidTime.setObjectName("dteValidTime")
        self.horizontalLayout_8.addWidget(self.dteValidTime)
        self.tbValidTime_back = QtWidgets.QToolButton(WMSDockWidget)
        self.tbValidTime_back.setObjectName("tbValidTime_back")
        self.horizontalLayout_8.addWidget(self.tbValidTime_back)
        self.cbValidTime_step = QtWidgets.QComboBox(WMSDockWidget)
        self.cbValidTime_step.setObjectName("cbValidTime_step")
        self.horizontalLayout_8.addWidget(self.cbValidTime_step)
        self.tbValidTime_fwd = QtWidgets.QToolButton(WMSDockWidget)
        self.tbValidTime_fwd.setObjectName("tbValidTime_fwd")
        self.horizontalLayout_8.addWidget(self.tbValidTime_fwd)
        spacerItem1 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_8, 2, 2, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.cbLevel = QtWidgets.QComboBox(WMSDockWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cbLevel.sizePolicy().hasHeightForWidth())
        self.cbLevel.setSizePolicy(sizePolicy)
        self.cbLevel.setMinimumSize(QtCore.QSize(180, 0))
        self.cbLevel.setMaximumSize(QtCore.QSize(250, 16777215))
        self.cbLevel.setObjectName("cbLevel")
        self.horizontalLayout_4.addWidget(self.cbLevel)
        self.tbLevel_back = QtWidgets.QToolButton(WMSDockWidget)
        self.tbLevel_back.setObjectName("tbLevel_back")
        self.horizontalLayout_4.addWidget(self.tbLevel_back)
        self.tbLevel_fwd = QtWidgets.QToolButton(WMSDockWidget)
        self.tbLevel_fwd.setObjectName("tbLevel_fwd")
        self.horizontalLayout_4.addWidget(self.tbLevel_fwd)
        spacerItem2 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.line_5 = QtWidgets.QFrame(WMSDockWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.horizontalLayout_4.addWidget(self.line_5)
        self.cbTransparent = QtWidgets.QCheckBox(WMSDockWidget)
        self.cbTransparent.setChecked(True)
        self.cbTransparent.setObjectName("cbTransparent")
        self.horizontalLayout_4.addWidget(self.cbTransparent)
        self.line_3 = QtWidgets.QFrame(WMSDockWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout_4.addWidget(self.line_3)
        self.label = QtWidgets.QLabel(WMSDockWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.cbCacheEnabled = QtWidgets.QCheckBox(WMSDockWidget)
        self.cbCacheEnabled.setChecked(True)
        self.cbCacheEnabled.setTristate(False)
        self.cbCacheEnabled.setObjectName("cbCacheEnabled")
        self.horizontalLayout_4.addWidget(self.cbCacheEnabled)
        self.btClearCache = QtWidgets.QPushButton(WMSDockWidget)
        self.btClearCache.setObjectName("btClearCache")
        self.horizontalLayout_4.addWidget(self.btClearCache)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 2, 1, 1)
        self.cbValidOn = QtWidgets.QCheckBox(WMSDockWidget)
        self.cbValidOn.setEnabled(False)
        self.cbValidOn.setMinimumSize(QtCore.QSize(0, 0))
        self.cbValidOn.setMaximumSize(QtCore.QSize(120, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.cbValidOn.setPalette(palette)
        self.cbValidOn.setObjectName("cbValidOn")
        self.gridLayout.addWidget(self.cbValidOn, 2, 0, 1, 1)
        self.cbLevelOn = QtWidgets.QCheckBox(WMSDockWidget)
        self.cbLevelOn.setEnabled(False)
        self.cbLevelOn.setMinimumSize(QtCore.QSize(0, 0))
        self.cbLevelOn.setMaximumSize(QtCore.QSize(120, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.cbLevelOn.setPalette(palette)
        self.cbLevelOn.setCheckable(True)
        self.cbLevelOn.setObjectName("cbLevelOn")
        self.gridLayout.addWidget(self.cbLevelOn, 0, 0, 1, 1)
        self.cbInitialisationOn = QtWidgets.QCheckBox(WMSDockWidget)
        self.cbInitialisationOn.setEnabled(False)
        self.cbInitialisationOn.setMinimumSize(QtCore.QSize(0, 0))
        self.cbInitialisationOn.setMaximumSize(QtCore.QSize(120, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(20, 19, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.cbInitialisationOn.setPalette(palette)
        self.cbInitialisationOn.setObjectName("cbInitialisationOn")
        self.gridLayout.addWidget(self.cbInitialisationOn, 1, 0, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.line = QtWidgets.QFrame(WMSDockWidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_4.addWidget(self.line)

        self.retranslateUi(WMSDockWidget)
        QtCore.QMetaObject.connectSlotsByName(WMSDockWidget)

    def retranslateUi(self, WMSDockWidget):
        _translate = QtCore.QCoreApplication.translate
        WMSDockWidget.setWindowTitle(_translate("WMSDockWidget", "WMS Dock Widget"))
        self.label_7.setText(_translate("WMSDockWidget", "WMS URL:"))
        self.cbWMS_URL.setToolTip(_translate("WMSDockWidget", "Enter a valid WMS URL here."))
        self.cbWMS_URL.setItemText(0, _translate("WMSDockWidget", "http://localhost:8002/fc_wms"))
        self.cbWMS_URL.setItemText(1, _translate("WMSDockWidget", "http://osm.omniscale.net/proxy/service"))
        self.btGetCapabilities.setToolTip(_translate("WMSDockWidget", "Request the capabilities from the WMS server."))
        self.btGetCapabilities.setText(_translate("WMSDockWidget", "get capabilities"))
        self.pbViewCapabilities.setToolTip(_translate("WMSDockWidget", "Show information on the selected WMS server."))
        self.pbViewCapabilities.setText(_translate("WMSDockWidget", "view"))
        self.cbAutoUpdate.setToolTip(_translate("WMSDockWidget", "Automatically request an updated map when the layer parameters have changed."))
        self.cbAutoUpdate.setText(_translate("WMSDockWidget", "update on changes"))
        self.btGetMap.setToolTip(_translate("WMSDockWidget", "Request a map with the specifed parameters."))
        self.btGetMap.setText(_translate("WMSDockWidget", "get map"))
        self.label_8.setText(_translate("WMSDockWidget", "Layer:"))
        self.cbLayer.setItemText(0, _translate("WMSDockWidget", "BASEMAP"))
        self.cbLayer.setItemText(1, _translate("WMSDockWidget", "MSLP"))
        self.cbLayer.setItemText(2, _translate("WMSDockWidget", "TCC"))
        self.label_11.setText(_translate("WMSDockWidget", "Style:"))
        self.cbStyle.setItemText(0, _translate("WMSDockWidget", "..."))
        self.teLayerAbstract.setHtml(_translate("WMSDockWidget", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:10pt;\"><br /></p></body></html>"))
        self.cbInitTime.setToolTip(_translate("WMSDockWidget", "Forecast initialisation time (base time) values provided by the WMS server."))
        self.cbInitTime.setItemText(0, _translate("WMSDockWidget", "2010-12-12T00:00:00Z"))
        self.tbInitTime_cbback.setToolTip(_translate("WMSDockWidget", "Keyboard shortcut: alt-left"))
        self.tbInitTime_cbback.setText(_translate("WMSDockWidget", "<"))
        self.tbInitTime_cbback.setShortcut(_translate("WMSDockWidget", "Alt+Left"))
        self.tbInitTime_cbfwd.setToolTip(_translate("WMSDockWidget", "Keyboard shortcut: alt-right"))
        self.tbInitTime_cbfwd.setText(_translate("WMSDockWidget", ">"))
        self.tbInitTime_cbfwd.setShortcut(_translate("WMSDockWidget", "Alt+Right"))
        self.dteInitTime.setToolTip(_translate("WMSDockWidget", "You can also specify an initialisation date here."))
        self.dteInitTime.setDisplayFormat(_translate("WMSDockWidget", "yyyy/MM/dd hh:mm UTC"))
        self.tbInitTime_back.setText(_translate("WMSDockWidget", "<"))
        self.tbInitTime_fwd.setText(_translate("WMSDockWidget", ">"))
        self.cbValidTime.setToolTip(_translate("WMSDockWidget", "Valid time values provided by the WMS server."))
        self.tbValidTime_cbback.setToolTip(_translate("WMSDockWidget", "Keyboard shortcut: left"))
        self.tbValidTime_cbback.setText(_translate("WMSDockWidget", "<"))
        self.tbValidTime_cbback.setShortcut(_translate("WMSDockWidget", "Left"))
        self.tbValidTime_cbfwd.setToolTip(_translate("WMSDockWidget", "Keyboard shortcut: right"))
        self.tbValidTime_cbfwd.setText(_translate("WMSDockWidget", ">"))
        self.tbValidTime_cbfwd.setShortcut(_translate("WMSDockWidget", "Right"))
        self.dteValidTime.setToolTip(_translate("WMSDockWidget", "Specify the time value here, especially if the server does not provide predefined values. Keep in mind that the specified value may not be available from the server, though."))
        self.dteValidTime.setDisplayFormat(_translate("WMSDockWidget", "yyyy/MM/dd hh:mm UTC"))
        self.tbValidTime_back.setText(_translate("WMSDockWidget", "<"))
        self.tbValidTime_fwd.setText(_translate("WMSDockWidget", ">"))
        self.cbLevel.setToolTip(_translate("WMSDockWidget", "Elevation values provided by the WMS server."))
        self.tbLevel_back.setToolTip(_translate("WMSDockWidget", "Keyboard shortcut: down"))
        self.tbLevel_back.setText(_translate("WMSDockWidget", "<"))
        self.tbLevel_back.setShortcut(_translate("WMSDockWidget", "Down"))
        self.tbLevel_fwd.setToolTip(_translate("WMSDockWidget", "Keyboard shortcut: up"))
        self.tbLevel_fwd.setText(_translate("WMSDockWidget", ">"))
        self.tbLevel_fwd.setShortcut(_translate("WMSDockWidget", "Up"))
        self.cbTransparent.setText(_translate("WMSDockWidget", "transparent"))
        self.label.setText(_translate("WMSDockWidget", "Cache:"))
        self.cbCacheEnabled.setToolTip(_translate("WMSDockWidget", "Enable the image cache (retrieved images will be stored locally to speed up repeated retrievals)."))
        self.cbCacheEnabled.setText(_translate("WMSDockWidget", "on"))
        self.btClearCache.setToolTip(_translate("WMSDockWidget", "Clear all cache contents."))
        self.btClearCache.setText(_translate("WMSDockWidget", "clear"))
        self.cbValidOn.setText(_translate("WMSDockWidget", "Valid:"))
        self.cbLevelOn.setText(_translate("WMSDockWidget", "Level:"))
        self.cbInitialisationOn.setText(_translate("WMSDockWidget", "Initialisation:"))

