from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import pyqtSignal
from processAutomationController.processAutomationController import ProcessAutomationController

class ControlScreen(QWidget):
    progress_update_signal = pyqtSignal(int)

    def __init__(self, main_window):
        super(ControlScreen, self).__init__(main_window)
        self.main_window = main_window

        # Load the control screen UI
        self.load_ui()

        # Initialize ProcessAutomationController
        self.process_automation_controller = ProcessAutomationController(main_window)

        # Load and add the pi_instruments_control_screen and robot_control_screen to the tabs
        self.load_tabs()

    def load_ui(self):
        try:
            uic.loadUi('src/ui/control_screen/control_screen.ui', self)
            print("ControlScreen UI loaded successfully")
        except Exception as e:
            print(f"Failed to load ControlScreen UI: {e}")

    def load_tabs(self):
        try:
            # Load pi_instruments_control_screen
            pi_instruments_widget = uic.loadUi('src/ui/control_screen/pi_instruemnts_control_screen/pi_instruemnts_control_screen.ui')
            pi_instruments_layout = QVBoxLayout()
            pi_instruments_layout.addWidget(pi_instruments_widget)
            self.tabWidget.widget(0).setLayout(pi_instruments_layout)

            # Load robot_control_screen
            robot_control_widget = uic.loadUi('src/ui/control_screen/robot_control_screen/robot_control_screen.ui')
            robot_control_layout = QVBoxLayout()
            robot_control_layout.addWidget(robot_control_widget)
            self.tabWidget.widget(1).setLayout(robot_control_layout)

            print("Tabs loaded successfully")
        except Exception as e:
            print(f"Failed to load tabs: {e}")

