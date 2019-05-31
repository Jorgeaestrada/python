#####################
# views\MainView.py #
#####################
from PyQt5 import QtWidgets
from gen.ui_MainView import Ui_MainView

class MainView(QtWidgets.QMainWindow):

    #### properties for widget value ####
    @property
    def my_combo_box(self):
        return self.ui.comboBox_my_combo_box.currentIndex()
    @my_combo_box.setter
    def my_combo_box(self, value):
        self.ui.comboBox_my_combo_box.setCurrentIndex(value)

    #### properties for widget enabled state ####
    @property
    def my_combo_box_enabled(self):
        return self.ui.comboBox_my_combo_box.isEnabled()
    @my_combo_box_enabled.setter
    def my_combo_box_enabled(self, value):
        self.ui.comboBox_my_combo_box.setEnabled(value)

    def __init__(self, model, main_ctrl):
        self.model = model
        self.main_ctrl = main_ctrl
        super(MainView, self).__init__()
        self.build_ui()
        # register func with model for model update announcements
        self.model.subscribe_update_func(self.update_ui_from_model)

    def build_ui(self):
        self.ui = Ui_MainView()
        self.ui.setupUi(self)

        #### set Qt model for compatible widget types ####
        self.ui.comboBox_my_combo_box.setModel(self.model.my_combo_box_model)

        #### connect widget signals to event functions ####
        self.ui.comboBox_my_combo_box.currentIndexChanged.connect(self.on_my_combo_box)

    def update_ui_from_model(self):
        print ('DEBUG: update_ui_from_model called')
        #### update widget values from model ####
        self.my_combo_box = self.model.my_combo_box

    #### widget signal event functions ####
    def on_my_combo_box(self, index): self.main_ctrl.change_my_combo_box(index)
