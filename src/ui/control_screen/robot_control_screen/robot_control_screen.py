from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

class RobotControlScreen(QWidget):
    def __init__(self, parent=None):
        super(RobotControlScreen, self).__init__(parent)
        self.load_ui()

    def load_ui(self):
        try:
            uic.loadUi('src/ui/control_screen/robot_control_screen/robot_control_screen.ui', self)
            print("RobotControlScreen UI loaded successfully")
        except Exception as e:
            print(f"Failed to load RobotControlScreen UI: {e}")