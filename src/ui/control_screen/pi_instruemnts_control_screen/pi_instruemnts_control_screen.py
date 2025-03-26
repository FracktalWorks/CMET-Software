from PyQt5 import uic
from PyQt5.QtWidgets import QWidget ,QPushButton

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

    def pi_setup_connections(self):
        self.findChild(QPushButton, 'piPartCleaning').clicked.connect(self)
        self.findChild(QPushButton, 'piHomeButton').clicked.connect(self.)
        self.findChild(QPushButton, 'piBeforeLayerStart').clicked.connect(self.)
        self.findChild(QPushButton, 'piAfterLayerStart').clicked.connect(self.)
        self.findChild(QPushButton, 'piBeforeVatChange').clicked.connect(self.)
        self.findChild(QPushButton, 'piAfterVatChange').clicked.connect(self.)
        self.findChild(QPushButton, 'Macro1Button').clicked.connect(self.)
        self.findChild(QPushButton, 'Macro2Button').clicked.connect(self.)

        self.findChild(QPushButton, 'piMoveZMButton').clicked.connect(self.)
        self.findChild(QPushButton, 'piHomeZButton').clicked.connect(self.)
        self.findChild(QPushButton, 'piMoveZPButton').clicked.connect(self.)

        self.findChild(QPushButton, 'piMoveXMButton').clicked.connect(self.)
        self.findChild(QPushButton, 'piMoveXPButton').clicked.connect(self.)
        self.findChild(QPushButton, 'piHomeXYButton').clicked.connect(self.)
        self.findChild(QPushButton, 'piMoveYMButton').clicked.connect(self.)
        self.findChild(QPushButton, 'piMoveYPButton').clicked.connect(self.)
