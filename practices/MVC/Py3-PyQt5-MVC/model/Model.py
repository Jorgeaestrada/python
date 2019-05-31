##################
# model\Model.py #
##################
from PyQt5 import QtGui

class Model(object):

    #### properties for value of Qt model contents ####
    @property
    def my_combo_box_items(self):
        return self.my_combo_box_model.stringList()
    @my_combo_box_items.setter
    def my_combo_box_items(self, value):
        self.my_combo_box_model.setStringList(value)

    def __init__(self):
        self._update_funcs = []
        self.config_section = 'settings'
        self.config_options = (
            ('my_combo_box', 'getint'),
        )

        #### create Qt models for compatible widget types ####
        self.my_combo_box_model = Qt.QStringListModel()

        #### model variables ####
        self.my_combo_box = None

    def subscribe_update_func(self, func):
        if func not in self._update_funcs:
            self._update_funcs.append(func)

    def unsubscribe_update_func(self, func):
        if func in self._update_funcs:
            self._update_funcs.remove(func)

    def announce_update(self):
        for func in self._update_funcs:
            func()


