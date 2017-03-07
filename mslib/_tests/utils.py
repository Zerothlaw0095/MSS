# -*- coding: utf-8 -*-
"""

    mslib._tests.utils
    ~~~~~~~~~~~~~~~~~~

    This module provides common functions for MSS testing

    This file is part of mss.

    :copyright: Copyright 2017 Reimar Bauer, Joern Ungermann
    :copyright: Copyright 2017 by the mss team, see AUTHORS.
    :license: APACHE-2.0, see LICENSE for details.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import os
import tempfile
from mslib.msui.mss_qt import QtWidgets, QtTest, QtCore

try:
    import git
except ImportError:
    SHA = ""
else:
    repo = git.Repo(search_parent_directories=True)
    SHA = repo.head.object.hexsha


BASE_DIR = os.path.join(tempfile.gettempdir(), "mss{}".format(SHA))
DATA_DIR = os.path.join(BASE_DIR, 'testdata')
SERVER_CONFIG_FILE = os.path.join(BASE_DIR, "mss_wms_settings.py")
VALID_TIME_CACHE = os.path.join(BASE_DIR, 'vt_cache')


def close_modal_messagebox(window):
    """
    This function closes a non-blocking modal message box typically used to indicate an error.
    :param window: parent widget of the message box
    :return: whether a window was closed
    """
    box = [_x for _x in window.children() if isinstance(_x, QtWidgets.QMessageBox)]
    if len(box) == 1:
        QtTest.QTest.keyClick(box[0], QtCore.Qt.Key_Enter)
        QtTest.QTest.qWait(20)
        QtWidgets.QApplication.processEvents()
        return True
    return False
