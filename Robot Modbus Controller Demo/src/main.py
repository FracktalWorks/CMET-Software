from PyQt5.QtWidgets import QApplication
import sys
from ui.main_window import MainWindow
from modbus.client import ModbusClient
from config.settings import MODBUS_ADDRESS, MODBUS_PORT

def main():
    app = QApplication(sys.argv)
    
    # Initialize Modbus client
    modbus_client = ModbusClient(MODBUS_ADDRESS, MODBUS_PORT)
    
    # Create the main window
    main_window = MainWindow()
    
    # Show the main window
    main_window.show()
    
    # Ensure Modbus client is closed on exit
    app.aboutToQuit.connect(modbus_client.close)
    
    # Execute the application
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()