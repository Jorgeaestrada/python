###########################
# ctrls\MainController.py #
###########################
from PyQt5 import QtWidgets

class MainController(object):

    def __init__(self, model):
        self.model = model

    #### widget event functions ####
    def change_my_combo_box(self, index):
        self.model.my_combo_box = index
        print ('DEBUG: change_my_combo_box called with arg value:', index)
