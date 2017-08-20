# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MSSMainWindow(object):
    def setupUi(self, MSSMainWindow):
        MSSMainWindow.setObjectName(_fromUtf8("MSSMainWindow"))
        MSSMainWindow.resize(424, 540)
        self.centralwidget = QtGui.QWidget(MSSMainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setFlat(True)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.listFlightTracks = QtGui.QListWidget(self.groupBox_3)
        self.listFlightTracks.setAlternatingRowColors(False)
        self.listFlightTracks.setTextElideMode(QtCore.Qt.ElideNone)
        self.listFlightTracks.setObjectName(_fromUtf8("listFlightTracks"))
        self.verticalLayout_6.addWidget(self.listFlightTracks)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setFlat(True)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.listViews = QtGui.QListWidget(self.groupBox)
        self.listViews.setObjectName(_fromUtf8("listViews"))
        self.verticalLayout_4.addWidget(self.listViews)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setFlat(True)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.listTools = QtGui.QListWidget(self.groupBox_2)
        self.listTools.setObjectName(_fromUtf8("listTools"))
        self.verticalLayout_5.addWidget(self.listTools)
        self.verticalLayout.addWidget(self.groupBox_2)
        MSSMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MSSMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 424, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menuImport_Flight_Track = QtGui.QMenu(self.menu_File)
        self.menuImport_Flight_Track.setObjectName(_fromUtf8("menuImport_Flight_Track"))
        self.menuExport_Active_Flight_Track = QtGui.QMenu(self.menu_File)
        self.menuExport_Active_Flight_Track.setObjectName(_fromUtf8("menuExport_Active_Flight_Track"))
        self.menu_View = QtGui.QMenu(self.menubar)
        self.menu_View.setObjectName(_fromUtf8("menu_View"))
        self.menu_Tools = QtGui.QMenu(self.menubar)
        self.menu_Tools.setObjectName(_fromUtf8("menu_Tools"))
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName(_fromUtf8("menu_Help"))
        MSSMainWindow.setMenuBar(self.menubar)
        self.action_Quit = QtGui.QAction(MSSMainWindow)
        self.action_Quit.setObjectName(_fromUtf8("action_Quit"))
        self.actionNewFlightTrack = QtGui.QAction(MSSMainWindow)
        self.actionNewFlightTrack.setObjectName(_fromUtf8("actionNewFlightTrack"))
        self.actionOpenFlightTrack = QtGui.QAction(MSSMainWindow)
        self.actionOpenFlightTrack.setObjectName(_fromUtf8("actionOpenFlightTrack"))
        self.actionSaveActiveFlightTrack = QtGui.QAction(MSSMainWindow)
        self.actionSaveActiveFlightTrack.setObjectName(_fromUtf8("actionSaveActiveFlightTrack"))
        self.actionSaveActiveFlightTrackAs = QtGui.QAction(MSSMainWindow)
        self.actionSaveActiveFlightTrackAs.setObjectName(_fromUtf8("actionSaveActiveFlightTrackAs"))
        self.actionCloseSelectedFlightTrack = QtGui.QAction(MSSMainWindow)
        self.actionCloseSelectedFlightTrack.setShortcut(_fromUtf8(""))
        self.actionCloseSelectedFlightTrack.setObjectName(_fromUtf8("actionCloseSelectedFlightTrack"))
        self.actionTopView = QtGui.QAction(MSSMainWindow)
        self.actionTopView.setObjectName(_fromUtf8("actionTopView"))
        self.actionSideView = QtGui.QAction(MSSMainWindow)
        self.actionSideView.setObjectName(_fromUtf8("actionSideView"))
        self.actionTableView = QtGui.QAction(MSSMainWindow)
        self.actionTableView.setObjectName(_fromUtf8("actionTableView"))
        self.actionLoopView = QtGui.QAction(MSSMainWindow)
        self.actionLoopView.setObjectName(_fromUtf8("actionLoopView"))
        self.actionTimeSeriesViewTrajectories = QtGui.QAction(MSSMainWindow)
        self.actionTimeSeriesViewTrajectories.setObjectName(_fromUtf8("actionTimeSeriesViewTrajectories"))
        self.actionTrajectoryToolLagranto = QtGui.QAction(MSSMainWindow)
        self.actionTrajectoryToolLagranto.setObjectName(_fromUtf8("actionTrajectoryToolLagranto"))
        self.actionAboutMSUI = QtGui.QAction(MSSMainWindow)
        self.actionAboutMSUI.setObjectName(_fromUtf8("actionAboutMSUI"))
        self.actionLoad_Configuration = QtGui.QAction(MSSMainWindow)
        self.actionLoad_Configuration.setObjectName(_fromUtf8("actionLoad_Configuration"))
        self.actionOnlineHelp = QtGui.QAction(MSSMainWindow)
        self.actionOnlineHelp.setObjectName(_fromUtf8("actionOnlineHelp"))
        self.actionActivateSelectedFlightTrack = QtGui.QAction(MSSMainWindow)
        self.actionActivateSelectedFlightTrack.setShortcut(_fromUtf8(""))
        self.actionActivateSelectedFlightTrack.setObjectName(_fromUtf8("actionActivateSelectedFlightTrack"))
        self.menu_File.addAction(self.actionNewFlightTrack)
        self.menu_File.addAction(self.actionOpenFlightTrack)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionActivateSelectedFlightTrack)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionSaveActiveFlightTrack)
        self.menu_File.addAction(self.actionSaveActiveFlightTrackAs)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionCloseSelectedFlightTrack)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.menuImport_Flight_Track.menuAction())
        self.menu_File.addAction(self.menuExport_Active_Flight_Track.menuAction())
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionLoad_Configuration)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Quit)
        self.menu_View.addAction(self.actionTopView)
        self.menu_View.addAction(self.actionSideView)
        self.menu_View.addAction(self.actionTableView)
        self.menu_Tools.addAction(self.actionTrajectoryToolLagranto)
        self.menu_Tools.addAction(self.actionTimeSeriesViewTrajectories)
        self.menu_Tools.addSeparator()
        self.menu_Tools.addAction(self.actionLoopView)
        self.menu_Help.addAction(self.actionOnlineHelp)
        self.menu_Help.addAction(self.actionAboutMSUI)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_View.menuAction())
        self.menubar.addAction(self.menu_Tools.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MSSMainWindow)
        QtCore.QObject.connect(self.action_Quit, QtCore.SIGNAL(_fromUtf8("triggered()")), MSSMainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MSSMainWindow)

    def retranslateUi(self, MSSMainWindow):
        MSSMainWindow.setWindowTitle(_translate("MSSMainWindow", "Mission Support System", None))
        self.groupBox_3.setTitle(_translate("MSSMainWindow", "Open Flight Tracks:", None))
        self.listFlightTracks.setToolTip(_translate("MSSMainWindow", "List of open flight tracks.\n"
"Double-click a flight track to activate it.\n"
"Save a flight track to name it.", None))
        self.groupBox.setTitle(_translate("MSSMainWindow", "Open Views:", None))
        self.listViews.setToolTip(_translate("MSSMainWindow", "Double-click a view to bring it to the front.", None))
        self.groupBox_2.setTitle(_translate("MSSMainWindow", "Open Tools:", None))
        self.listTools.setToolTip(_translate("MSSMainWindow", "Double-click a tool to bring it to the front.", None))
        self.menu_File.setTitle(_translate("MSSMainWindow", "&File", None))
        self.menuImport_Flight_Track.setTitle(_translate("MSSMainWindow", "Import Flight Track", None))
        self.menuExport_Active_Flight_Track.setTitle(_translate("MSSMainWindow", "Export Active Flight Track", None))
        self.menu_View.setTitle(_translate("MSSMainWindow", "&Views", None))
        self.menu_Tools.setTitle(_translate("MSSMainWindow", "&Tools", None))
        self.menu_Help.setTitle(_translate("MSSMainWindow", "&Help", None))
        self.action_Quit.setText(_translate("MSSMainWindow", "&Quit", None))
        self.action_Quit.setShortcut(_translate("MSSMainWindow", "Ctrl+Q", None))
        self.actionNewFlightTrack.setText(_translate("MSSMainWindow", "&New Flight Track", None))
        self.actionNewFlightTrack.setShortcut(_translate("MSSMainWindow", "Ctrl+N", None))
        self.actionOpenFlightTrack.setText(_translate("MSSMainWindow", "&Open Flight Track...", None))
        self.actionOpenFlightTrack.setShortcut(_translate("MSSMainWindow", "Ctrl+O", None))
        self.actionSaveActiveFlightTrack.setText(_translate("MSSMainWindow", "&Save Active Flight Track", None))
        self.actionSaveActiveFlightTrack.setShortcut(_translate("MSSMainWindow", "Ctrl+S", None))
        self.actionSaveActiveFlightTrackAs.setText(_translate("MSSMainWindow", "Save Active Flight Track &As...", None))
        self.actionCloseSelectedFlightTrack.setText(_translate("MSSMainWindow", "&Close Selected Flight Track", None))
        self.actionTopView.setText(_translate("MSSMainWindow", "&Top View (Horizontal Section)", None))
        self.actionTopView.setShortcut(_translate("MSSMainWindow", "Ctrl+H", None))
        self.actionSideView.setText(_translate("MSSMainWindow", "&Side View (Vertical Section)", None))
        self.actionSideView.setShortcut(_translate("MSSMainWindow", "Ctrl+V", None))
        self.actionTableView.setText(_translate("MSSMainWindow", "T&able View", None))
        self.actionTableView.setShortcut(_translate("MSSMainWindow", "Ctrl+T", None))
        self.actionLoopView.setText(_translate("MSSMainWindow", "&Loop View (Images)", None))
        self.actionTimeSeriesViewTrajectories.setText(_translate("MSSMainWindow", "T&ime Series View (Trajectories)", None))
        self.actionTrajectoryToolLagranto.setText(_translate("MSSMainWindow", "&Trajectory Tool (Lagranto)", None))
        self.actionAboutMSUI.setText(_translate("MSSMainWindow", "&About MSS", None))
        self.actionLoad_Configuration.setText(_translate("MSSMainWindow", "Load Configuration", None))
        self.actionOnlineHelp.setText(_translate("MSSMainWindow", "Online &Help", None))
        self.actionActivateSelectedFlightTrack.setText(_translate("MSSMainWindow", "Activate Selected Flight Track", None))

