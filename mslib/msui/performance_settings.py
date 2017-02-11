"""
AUTHORS:
========

* Joern Ungermann (ju)

"""
import logging

from mslib.msui.mss_qt import QtGui, QtCore, QtWidgets, USE_PYQT5

from mslib.mss_util import config_loader
from mslib.msui import aircrafts
from mslib.msui import constants
from mslib.msui.mss_qt import ui_performance_settings as ui_ps


DEFAULT_PERFORMANCE = {
    "aircraft": aircrafts.SimpleAircraft(aircrafts.AIRCRAFT_DUMMY),
    "visible": False,
    "takeoff_weight": 0,
    "takeoff_time": QtCore.QDateTime.currentDateTimeUtc(),
    "fuel": 0
}


class MSS_PerformanceSettingsDialog(QtWidgets.QDialog, ui_ps.Ui_PerformanceSettingsDialog):
    """Dialog to set map appearance parameters. User interface is
       defined in "ui_topview_mapappearance.py".
    """

    def __init__(self, parent=None, settings_dict=None):
        """
        Arguments:
        parent -- Qt widget that is parent to this widget.
        settings_dict -- dictionary containing topview options.
        """
        super(MSS_PerformanceSettingsDialog, self).__init__(parent)
        self.setupUi(self)

        if not settings_dict:
            settings_dict = DEFAULT_PERFORMANCE
        self.aircraft = settings_dict["aircraft"]
        self.lbAircraftName.setText(self.aircraft.name)
        self.cbShowPerformance.setChecked(settings_dict["visible"])
        self.dsbTakeoffWeight.setValue(settings_dict["takeoff_weight"])
        self.dsbFuel.setValue(settings_dict["fuel"])
        self.dteTakeoffTime.setDateTime(settings_dict["takeoff_time"])

        self.pbLoadPerformance.clicked.connect(self.load_performance)

    def get_settings(self):
        """
        Encapsulates GUI selections in a python dictionary.

        :return:
         Dictionary of all setting informations
        """
        settings_dict = {
            "aircraft": self.aircraft,
            "visible": self.cbShowPerformance.isChecked(),
            "takeoff_weight": self.dsbTakeoffWeight.value(),
            "takeoff_time": self.dteTakeoffTime.dateTime(),
            "fuel": self.dsbFuel.value()
        }
        return settings_dict

    def load_performance(self):
        """
        Gets a filename for a JSON file specifying aircraft performance and initializes an SimpleAircraft model.
        """
        filename = QtWidgets.QFileDialog.getOpenFileName(
            self, "Open Aircraft Performance JSON File", constants.MSS_CONFIG_PATH, "(*.json)")
        filename = filename[0] if USE_PYQT5 else unicode(filename)

        try:
            performance = config_loader(config_file=filename)
            self.aircraft = aircrafts.SimpleAircraft(performance)
            self.lbAircraftName.setText(self.aircraft.name)
            self.dsbTakeoffWeight.setValue(self.aircraft.takeoff_weight)
            self.dsbFuel.setValue(self.aircraft.fuel)

        except KeyError, ex:
            QtWidgets.QMessageBox.critical(self, self.tr("Performance JSON Load"),
                                           self.tr("JSON File missing '{}' entry".format(ex)),
                                           QtWidgets.QMessageBox.Ok)
        except ValueError, ex:
            QtWidgets.QMessageBox.critical(self, self.tr("Performance JSON Load"),
                                           self.tr("JSON File has Syntax Problems:\n{}".format(ex)),
                                           QtWidgets.QMessageBox.Ok)
