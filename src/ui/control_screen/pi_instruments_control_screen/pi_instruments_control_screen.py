import logging
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QPushButton
from pi_instruments.pi_intruments import pi_control

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class PiInstrumentsControlScreen(QWidget):
    def __init__(self, parent=None):
        super(PiInstrumentsControlScreen, self).__init__(parent)
        print("!!!! PiInstrumentsControlScreen initialized")
        self.load_ui()
        self.pi_control = pi_control()  # Create an instance of pi_control
        self.pi_setup_connections()
        # Initialize button states
        self.piEnableButton.setEnabled(False)  # Disabled until connected
        self.enable_movement_buttons(False)    # Disabled until enabled

    def load_ui(self):
        try:
            # Use absolute path to ensure UI file is found
            import os
            ui_file = os.path.join(os.path.dirname(__file__), 'pi_instruments_control_screen.ui')
            uic.loadUi(ui_file, self)
            print("PiInstrumentsControlScreen UI loaded successfully")
        except Exception as e:
            print(f"Failed to load PiInstrumentsControlScreen UI: {e}")
            raise  # This will help see the full error traceback

    def pi_setup_connections(self):
        # Assign each button to an object
        self.piConnectButton = self.findChild(QPushButton, 'piConnect')
        self.piEnableButton = self.findChild(QPushButton, 'piEnableButton')
        self.piBeforeLayerStartButton = self.findChild(QPushButton, 'piBeforeLayerStart')
        self.piAfterLayerStartButton = self.findChild(QPushButton, 'piAfterLayerStart')
        self.piBeforeVatChangeButton = self.findChild(QPushButton, 'piBeforeVatChange')
        self.piAfterVatChangeButton = self.findChild(QPushButton, 'piAfterVatChange')
        self.macro1Button = self.findChild(QPushButton, 'Macro1Button')
        self.macro2Button = self.findChild(QPushButton, 'Macro2Button')
        self.piMoveZMButton = self.findChild(QPushButton, 'piMoveZMButton')
        self.piHomeZButton = self.findChild(QPushButton, 'piHomeZButton')
        self.piMoveZPButton = self.findChild(QPushButton, 'piMoveZPButton')
        self.piMoveXMButton = self.findChild(QPushButton, 'piMoveXMButton')
        self.piMoveXPButton = self.findChild(QPushButton, 'piMoveXPButton')
        self.piHomeXYButton = self.findChild(QPushButton, 'piHomeXYButton')
        self.piMoveYMButton = self.findChild(QPushButton, 'piMoveYMButton')
        self.piMoveYPButton = self.findChild(QPushButton, 'piMoveYPButton')

        # Debug prints to check if buttons are found
        print(f"piConnectButton: {self.piConnectButton}")
        print(f"piEnableButton: {self.piEnableButton}")
        print(f"piBeforeLayerStartButton: {self.piBeforeLayerStartButton}")
        print(f"piAfterLayerStartButton: {self.piAfterLayerStartButton}")
        print(f"piBeforeVatChangeButton: {self.piBeforeVatChangeButton}")
        print(f"piAfterVatChangeButton: {self.piAfterVatChangeButton}")
        print(f"macro1Button: {self.macro1Button}")
        print(f"macro2Button: {self.macro2Button}")
        print(f"piMoveZMButton: {self.piMoveZMButton}")
        print(f"piHomeZButton: {self.piHomeZButton}")
        print(f"piMoveZPButton: {self.piMoveZPButton}")
        print(f"piMoveXMButton: {self.piMoveXMButton}")
        print(f"piMoveXPButton: {self.piMoveXPButton}")
        print(f"piHomeXYButton: {self.piHomeXYButton}")
        print(f"piMoveYMButton: {self.piMoveYMButton}")
        print(f"piMoveYPButton: {self.piMoveYPButton}")

        # Check if all buttons are found
        if not all([
            self.piConnectButton, self.piEnableButton, self.piBeforeLayerStartButton,
            self.piAfterLayerStartButton, self.piBeforeVatChangeButton, self.piAfterVatChangeButton,
            self.macro1Button, self.macro2Button, self.piMoveZMButton, self.piHomeZButton,
            self.piMoveZPButton, self.piMoveXMButton, self.piMoveXPButton, self.piHomeXYButton,
            self.piMoveYMButton, self.piMoveYPButton
        ]):
            raise ValueError("One or more buttons not found in the UI file")

        # Connect buttons to their respective functions
        self.piConnectButton.clicked.connect(self.pi_connect)
        self.piEnableButton.clicked.connect(self.pi_enable)
        self.piBeforeLayerStartButton.clicked.connect(self.pi_before_layer_start)
        self.piAfterLayerStartButton.clicked.connect(self.pi_after_layer_start)
        self.piBeforeVatChangeButton.clicked.connect(self.pi_before_vat_change)
        self.piAfterVatChangeButton.clicked.connect(self.pi_after_vat_change)
        self.macro1Button.clicked.connect(self.macro1)
        self.macro2Button.clicked.connect(self.macro2)
        self.piMoveZMButton.clicked.connect(self.pi_ZM)
        self.piHomeZButton.clicked.connect(self.pi_Zhome)
        self.piMoveZPButton.clicked.connect(self.pi_ZP)
        self.piMoveXMButton.clicked.connect(self.pi_XM)
        self.piMoveXPButton.clicked.connect(self.pi_XP)
        self.piHomeXYButton.clicked.connect(self.pi_XYhome)
        self.piMoveYMButton.clicked.connect(self.pi_YM)
        self.piMoveYPButton.clicked.connect(self.pi_YP)

    # Placeholder methods for button actions
    def pi_connect(self):
        logger.debug("Connecting to PI controller...")
        try:
            success = self.pi_control.connect()
            if success:
                logger.info("Successfully connected to PI controller")
                self.piConnectButton.setEnabled(False)  # Disable connect button after successful connection
                self.piEnableButton.setEnabled(True)    # Enable the enable button
            else:
                logger.error("Failed to connect to PI controller")
        except Exception as e:
            logger.error(f"Error connecting to PI controller: {e}")

    def pi_enable(self):
        try:
            success = self.pi_control.enable()
            if success:
                logger.info("PI controller enabled")
                self.enable_movement_buttons(True)  # Enable movement buttons after successful enable
            else:
                logger.error("Failed to enable PI controller")
        except Exception as e:
            logger.error(f"Error enabling PI controller: {e}")

    def pi_ZM(self):
        try:
            self.pi_control.move_z(-1)  # Adjust value as needed
            logger.info("Moving Z axis down")
        except Exception as e:
            logger.error(f"Error moving Z axis down: {e}")

    def pi_Zhome(self):
        try:
            self.pi_control.home_z()
            logger.info("Homing Z axis")
        except Exception as e:
            logger.error(f"Error homing Z axis: {e}")

    def pi_ZP(self):
        try:
            self.pi_control.move_z(1)  # Adjust value as needed
            logger.info("Moving Z axis up")
        except Exception as e:
            logger.error(f"Error moving Z axis up: {e}")

    def pi_XM(self):
        try:
            self.pi_control.move_x(-1)  # Adjust value as needed
            logger.info("Moving X axis left")
        except Exception as e:
            logger.error(f"Error moving X axis left: {e}")

    def pi_XP(self):
        try:
            self.pi_control.move_x(1)  # Adjust value as needed
            logger.info("Moving X axis right")
        except Exception as e:
            logger.error(f"Error moving X axis right: {e}")

    def pi_YM(self):
        try:
            self.pi_control.move_y(-1)  # Adjust value as needed
            logger.info("Moving Y axis down")
        except Exception as e:
            logger.error(f"Error moving Y axis down: {e}")

    def pi_YP(self):
        try:
            self.pi_control.move_y(1)  # Adjust value as needed
            logger.info("Moving Y axis up")
        except Exception as e:
            logger.error(f"Error moving Y axis up: {e}")

    def enable_movement_buttons(self, enabled=True):
        """Enable or disable movement buttons based on controller state"""
        movement_buttons = [
            self.piMoveZMButton, self.piHomeZButton, self.piMoveZPButton,
            self.piMoveXMButton, self.piMoveXPButton, self.piHomeXYButton,
            self.piMoveYMButton, self.piMoveYPButton
        ]
        for button in movement_buttons:
            button.setEnabled(enabled)

    def pi_before_layer_start(self):
        print("Before layer start...")

    def pi_after_layer_start(self):
        print("After layer start...")

    def pi_before_vat_change(self):
        print("Before vat change...")

    def pi_after_vat_change(self):
        print("After vat change...")

    def macro1(self):
        print("Executing Macro 1...")

    def macro2(self):
        print("Executing Macro 2...")



