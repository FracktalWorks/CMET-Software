from PyQt5 import uic
from PyQt5.QtWidgets import QWidget , QPushButton

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

    def robot_setup_connections(self):
        self.findChild(QPushButton, 'robotPlaceCleaningStation').clicked.connect(self.)
        self.findChild(QPushButton, 'robotRemoveCleaningStation').clicked.connect(self.)
        self.findChild(QPushButton, 'robotPlaceMaterial1').clicked.connect(self.)
        self.findChild(QPushButton, 'robotPlaceMaterial2').clicked.connect(self.)
        self.findChild(QPushButton, 'robotRemoveMaterial1').clicked.connect(self.)
        self.findChild(QPushButton, 'robotRemoveMaterial2').clicked.connect(self.)
        self.findChild(QPushButton, 'robotMixVat').clicked.connect(self.)
        self.findChild(QPushButton, 'robotHomeAxis').clicked.connect(self.)

        self.findChild(QPushButton, 'robotMoveZMButton').clicked.connect(self.)
        self.findChild(QPushButton, 'robotHomeZButton').clicked.connect(self.)
        self.findChild(QPushButton, 'robotMoveZPButton').clicked.connect(self.)

        self.findChild(QPushButton, 'robotMoveXMButton').clicked.connect(self.)
        self.findChild(QPushButton, 'robotMoveYMButton').clicked.connect(self.)
        self.findChild(QPushButton, 'robotHomeXYButton').clicked.connect(self.)
        self.findChild(QPushButton, 'robotMoveYPButton').clicked.connect(self.)
        self.findChild(QPushButton, 'robotMoveXPButton').clicked.connect(self.)