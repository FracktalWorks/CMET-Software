# CNC Modbus Controller

This project is a CNC machine controller that communicates with a CNC machine over Modbus using a PyQt graphical user interface (GUI). The application allows users to send commands to the CNC machine and control its operations.

## Features

- Control various CNC commands through a user-friendly interface.
- Communicate with the CNC machine using Modbus TCP.
- Reset command bits after each command is sent to ensure proper operation.

## Project Structure

```
cnc-modbus-controller
├── src
│   ├── main.py                # Entry point of the application
│   ├── ui                     # Contains UI components
│   │   ├── __init__.py        # Empty initializer for the ui package
│   │   ├── main_window.py      # Main window interface
│   │   └── controls_panel.py    # Control buttons for CNC commands
│   ├── modbus                 # Contains Modbus communication components
│   │   ├── __init__.py        # Empty initializer for the modbus package
│   │   ├── client.py          # Modbus client for communication
│   │   └── commands.py        # Command definitions and mappings
│   ├── config                 # Configuration settings
│   │   ├── __init__.py        # Empty initializer for the config package
│   │   └── settings.py        # Modbus server settings
│   └── utils                  # Utility functions
│       ├── __init__.py        # Empty initializer for the utils package
│       └── logger.py          # Logging utility
├── requirements.txt           # Project dependencies
├── LICENSE                    # Licensing information
└── README.md                  # Project documentation
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd cnc-modbus-controller
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/main.py
   ```

2. Use the GUI to control the CNC machine by selecting commands and monitoring the status.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.