from PyQt5 import uic
from PyQt5.QtWidgets import (QWidget, QPushButton, QSpinBox, QProgressBar, QSizePolicy, QVBoxLayout, QMessageBox, QLabel)
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QTimer
from PyQt5.QtGui import QImage
import numpy as np
from ui.custom_widgets import ImageWidget
from utils.helpers import run_async
import time
from processAutomationController.processAutomationController import ProcessAutomationController

class pi_control:
    @staticmethod
    def send_command(command, output_widget):
        """Send a command to the motion controller and display the response."""
        try:
            # Display the G-code being sent
            output_widget.append(f"Sending G-code: {command}")
            print(f"Sending G-code: {command}")  # Print to console for debugging

            # Simulate sending the command (replace with actual implementation)
            response = f"Simulated response for: {command}"  # Replace with actual response from hardware
            if response:
                output_widget.append(f"Command Sent: {command}")
                output_widget.append(f"Response: {response}")
                
                # Wait for the movement to complete
                time.sleep(0.5)
                
                # Send ?FPOS command to get current position
                position_response = pi_control.send_command("?FPOS")
                output_widget.append(f"Current Position: {position_response}")
        except Exception as e:
            output_widget.append(f"Error: {e}")
            print(f"Error: {e}")  # Print error to console
            log_error(e)

    def send_gcode_file(file_path, output_widget):
        """Read G-code from a file and send each line to the controller."""
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    command = line.strip()
                    if command:
                        pi_control.send_command(command, output_widget)
                        time.sleep(0.2)  # Short delay to avoid command overlap
        except FileNotFoundError:
            output_widget.append(f"Error: File {file_path} not found.")
            log_error(f"File {file_path} not found.")


    # Z movements
    def pi_home_z(self):
        pi_control.send_command("N50 G01 Z0 F500")

    def pi_z_minus(self):
        self.send_command("N60 G01 Z-10 F500")

    def move_z_plus(self):
        self.send_command("N70 G01 Z10 F500")

    # XY movements
    def home_xy(self):
        self.send_command("N70 G01 X0 Y0 F500")

    def move_x_minus(self):
        self.send_command("N20 G01 X-10 F500")

    def move_x_plus(self):
        self.send_command("N30 G01 X10 F500")

    def move_y_minus(self):
        self.send_command("N40 G01 Y-10 F500")

    def move_y_plus(self):
        self.send_command("N10 G01 Y10 F500")

    # Feed movements
    def move_feed_minus(self, step):
        self.send_gcode(f"G91\nG0 Y-{step}\nG90\nM400")

    def move_feed_plus(self, step):
        self.send_gcode(f"G91\nG0 Y{step}\nG90\nM400")


    def g_codes(self):    

        self.btn_y_plus = QPushButton("Move Y+")
        self.btn_y_plus.clicked.connect(lambda: ProcessAutomationController.send_command("N10 G01 Y10 F500", self.output_display))
        #grid.addWidget(self.btn_y_plus, 0, 1)
        
        self.btn_x_minus = QPushButton("Move X-")
        self.btn_x_minus.clicked.connect(lambda: ProcessAutomationController.send_command("N20 G01 X-10 F500", self.output_display))
        #grid.addWidget(self.btn_x_minus, 1, 0)
        
        self.btn_home = QPushButton("Home XYZ")
        self.btn_home.clicked.connect(lambda: ProcessAutomationController.send_command("N70 G01 X0 Y0 Z0 F200", self.output_display))
       # grid.addWidget(self.btn_home, 1, 1)
        
        self.btn_x_plus = QPushButton("Move X+")
        self.btn_x_plus.clicked.connect(lambda: ProcessAutomationController.send_command("N30 G01 X10 F500", self.output_display))
        #grid.addWidget(self.btn_x_plus, 1, 2)
        
        self.btn_y_minus = QPushButton("Move Y-")
        self.btn_y_minus.clicked.connect(lambda: ProcessAutomationController.send_command("N40 G01 Y-10 F500", self.output_display))
        
 
        
        # Z-Axis Buttons
        self.btn_z_up = QPushButton("piMoveZPButton")
        self.btn_z_up.clicked.connect(lambda: ProcessAutomationController.send_command("N50 G01 Z10 F500", self.output_display))
        
        self.btn_z_down = QPushButton("piMoveZMButton")
        self.btn_z_down.clicked.connect(lambda: ProcessAutomationController.send_command("N60 G01 Z-10 F500", self.output_display))
        
        
        self.btn_z_home = QPushButton("piHomeZButton")
        self.btn_z_down.clicked.connect(lambda: ProcessAutomationController.send_command("N60 G01 Z0 F500", self.output_display))

