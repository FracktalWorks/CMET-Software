from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

class PiInstrumentsControlScreen(QWidget):
    def __init__(self, parent=None):
        super(PiInstrumentsControlScreen, self).__init__(parent)
        self.load_ui()

    def load_ui(self):
        try:
            uic.loadUi('src/ui/control_screen/pi_instruemnts_control_screen/pi_instruemnts_control_screen.ui', self)
            print("PiInstrumentsControlScreen UI loaded successfully")
        except Exception as e:
            print(f"Failed to load PiInstrumentsControlScreen UI: {e}")