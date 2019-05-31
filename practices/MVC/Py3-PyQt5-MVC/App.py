##########
# App.py #
##########
import sys
from PyQt5 import Qt
from model.Model import Model
from ctrls.MainController import MainController
from views.MainView import MainView

class App(Qt.QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.model = Model()
        self.main_ctrl = MainController(self.model)
        self.main_view = MainView(self.model, self.main_ctrl)
        self.main_view.show()

if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec_())

