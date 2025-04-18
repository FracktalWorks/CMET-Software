from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QPushButton
from pi_instruments.pi_intruments import pi_control

class PiInstrumentsControlScreen(QWidget):
    def __init__(self, parent=None):
        super(PiInstrumentsControlScreen, self).__init__(parent)
        self.load_ui()
        self.pi_control = pi_control()  # Create an instance of pi_control
        self.pi_setup_connections()

    def load_ui(self):
        try:
            uic.loadUi('src/ui/control_screen/pi_instruemnts_control_screen/pi_instruemnts_control_screen.ui', self)
            print("PiInstrumentsControlScreen UI loaded successfully")
        except Exception as e:
            print(f"Failed to load PiInstrumentsControlScreen UI: {e}")

    def pi_setup_connections(self):
        self.findChild(QPushButton, 'piPartCleaning').clicked.connect(self.pi_part_cleaning)

        self.findChild(QPushButton, 'piEnableButton').clicked.connect(self.pi_enable)

        self.findChild(QPushButton, 'piBeforeLayerStart').clicked.connect(self.pi_before_layer_start)
        self.findChild(QPushButton, 'piAfterLayerStart').clicked.connect(self.pi_after_layer_start)
        self.findChild(QPushButton, 'piBeforeVatChange').clicked.connect(self.pi_before_vat_change)
        self.findChild(QPushButton, 'piAfterVatChange').clicked.connect(self.pi_after_vat_change)
        self.findChild(QPushButton, 'Macro1Button').clicked.connect(self.macro1)
        self.findChild(QPushButton, 'Macro2Button').clicked.connect(self.macro2)

        self.findChild(QPushButton, 'piMoveZMButton').clicked.connect(self.pi_ZM)
        self.findChild(QPushButton, 'piHomeZButton').clicked.connect(self.pi_Zhome)
        self.findChild(QPushButton, 'piMoveZPButton').clicked.connect(self.pi_ZP)

        self.findChild(QPushButton, 'piMoveXMButton').clicked.connect(self.pi_XM)
        self.findChild(QPushButton, 'piMoveXPButton').clicked.connect(self.pi_XP)
        self.findChild(QPushButton, 'piHomeXYButton').clicked.connect(self.pi_XYhome)
        self.findChild(QPushButton, 'piMoveYMButton').clicked.connect(self.pi_YM)
        self.findChild(QPushButton, 'piMoveYPButton').clicked.connect(self.pi_YP)
    
    def pi_enable(self):
        self.pi_control.pi_enable()

    def pi_ZM(self):
        self.pi_control.pi_ZM()

    def pi_Zhome(self):
        self.pi_control.pi_Zhome()

    def pi_ZP(self):
        self.pi_control.pi_ZP()

    def pi_XYhome(self):
        self.pi_control.pi_XYhome()

    def pi_XM(self):
        self.pi_control.pi_XM()

    def pi_XP(self):
        self.pi_control.pi_XP()

    def pi_YM(self):
        self.pi_control.pi_YM()

    def pi_YP(self):
        self.pi_control.pi_YP()

    # Add placeholder methods for other buttons
    def pi_part_cleaning(self):
        pass

    def pi_before_layer_start(self):
        pass

    def pi_after_layer_start(self):
        pass

    def pi_before_vat_change(self):
        pass

    def pi_after_vat_change(self):
        pass

    def macro1(self):
        pass

    def macro2(self):
        pass



