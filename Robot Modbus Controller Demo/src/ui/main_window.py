from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QScrollArea, QTextEdit, QFileDialog
from PyQt5.QtCore import QTimer
from modbus.client import ModbusClient
from modbus.commands import COMMANDS
from config.settings import MODBUS_ADDRESS, MODBUS_PORT
import subprocess

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CNC Modbus Controller")
        self.setGeometry(100, 100, 400, 600)

        # Central widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Main layout
        self.layout = QVBoxLayout(self.central_widget)

        # Connection status label
        self.connection_status_label = QLabel("Connection Status: Checking...", self)
        self.layout.addWidget(self.connection_status_label)

        # Status label
        self.status_label = QLabel("Status: Ready", self)
        self.layout.addWidget(self.status_label)

        # Scroll area for buttons
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)

        # Add buttons to the scroll layout
        self.buttons = {}
        for command_name, command in COMMANDS.items():
            button = QPushButton(command_name, self)
            button.clicked.connect(lambda checked, cmd=command: self.handle_command(cmd))
            self.scroll_layout.addWidget(button)
            self.buttons[command_name] = button

        self.scroll_area.setWidget(self.scroll_content)
        self.layout.addWidget(self.scroll_area)

        # Add a text area to display CNC controller responses
        self.response_area = QTextEdit(self)
        self.response_area.setReadOnly(True)
        self.layout.addWidget(self.response_area)

        # Add a label to display axis data
        self.axis_data_label = QLabel("Axis Data: Not Available", self)
        self.layout.addWidget(self.axis_data_label)

        # Add a button to send G-code files
        self.send_gcode_button = QPushButton("Send G-code File", self)
        self.send_gcode_button.clicked.connect(self.send_gcode_file)
        self.layout.addWidget(self.send_gcode_button)

        # Initialize Modbus client
        self.modbus_client = ModbusClient(MODBUS_ADDRESS, MODBUS_PORT)

        # Start a timer to periodically check the connection status
        self.connection_timer = QTimer(self)
        self.connection_timer.timeout.connect(self.check_connection_status)
        self.connection_timer.start(5000)  # Check every 5 seconds

        # Timer for fetching axis data
        self.axis_data_timer = QTimer(self)
        self.axis_data_timer.timeout.connect(self.fetch_axis_data)
        self.axis_data_timer.start(1000)  # Fetch data every 1 second

    def check_connection_status(self):
        """Check the connection status to the CNC controller."""
        if self.modbus_client.client.connect():
            self.connection_status_label.setText("Connection Status: Connected")
            self.modbus_client.client.close()
        else:
            self.connection_status_label.setText("Connection Status: Disconnected")

    def handle_command(self, command):
        """Handle sending and reading commands."""
        if command["action"] == "read_write":
            self.read_register(command)
        self.send_command(command)

    def send_command(self, command):
        """Send a command to the CNC controller."""
        client = ModbusClient(MODBUS_ADDRESS, MODBUS_PORT)
        if client.client.connect():  # Ensure the client connects properly
            try:
                # Send the command
                client.send_command(command['address'], True)
                self.status_label.setText(f"Status: {command} command sent.")
            except Exception as e:
                self.status_label.setText(f"Error: {str(e)}")
            finally:
                client.close()
        else:
            self.status_label.setText("Error: Unable to connect to Modbus server.")

    def read_register(self, command):
        """Read the appropriate register for a command."""
        client = ModbusClient(MODBUS_ADDRESS, MODBUS_PORT)
        if client.client.connect():  # Ensure the client connects properly
            try:
                if command["type"] == "coil":
                    response = client.client.read_coils(command["address"], 1)
                elif command["type"] == "holding":
                    response = client.client.read_holding_registers(command["address"], 1)
                else:
                    self.response_area.append(f"Unsupported command type: {command['type']}")
                    return

                if response.isError():
                    self.response_area.append(f"Error reading {command['address']}")
                else:
                    value = response.bits[0] if command["type"] == "coil" else response.registers[0]
                    self.response_area.append(f"{command['address']} Value: {value}")
            except Exception as e:
                self.response_area.append(f"Error: {str(e)}")
            finally:
                client.close()
        else:
            self.response_area.append("Error: Unable to connect to Modbus server.")

    def fetch_axis_data(self):
        """Fetch and display axis data."""
        axis_data = []
        for command_name, command in COMMANDS.items():
            # Filter commands based on their action being "read"
            if command["action"] == "read":
                try:
                    # Handle Coil Status and Holding Register types
                    if command["type"] == "coil":
                        response = self.modbus_client.client.read_coils(command["address"], 1)
                        if not response.isError():
                            value = response.bits[0]
                            axis_data.append(f"{command_name}: {value}")
                        else:
                            axis_data.append(f"{command_name}: Error")
                    elif command["type"] == "holding":
                        response = self.modbus_client.client.read_holding_registers(command["address"], 1)
                        if not response.isError():
                            value = response.registers[0]
                            axis_data.append(f"{command_name}: {value}")
                        else:
                            axis_data.append(f"{command_name}: Error")
                    else:
                        axis_data.append(f"{command_name}: Unsupported type")
                except Exception as e:
                    axis_data.append(f"{command_name}: {str(e)}")

        # Update the axis data label with the fetched data
        self.axis_data_label.setText("\n".join(axis_data))

    def send_gcode_file(self):
        """Open a file dialog to select a G-code file and send it to the CNC controller."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Select G-code File", "", "G-code Files (*.ngc)")
        if file_path:
            try:
                # Execute the sftp_module.exe with the selected file
                result = subprocess.run(
                    ["src/sftp_module.exe", "-i", file_path],
                    capture_output=True,
                    text=True
                )
                if result.returncode == 0:
                    self.status_label.setText(f"Status: G-code file '{file_path}' sent successfully.")
                    self.response_area.append(result.stdout)
                else:
                    self.status_label.setText(f"Error: Failed to send G-code file '{file_path}'.")
                    self.response_area.append(result.stderr)
            except Exception as e:
                self.status_label.setText(f"Error: {str(e)}")
                self.response_area.append(f"Exception: {str(e)}")