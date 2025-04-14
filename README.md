# CMET Control Center

A collection of Python-based projects for controlling and automating DLP-based 3D printers.

## Projects

### Control Center
The main application providing a touchscreen-friendly interface for 3D printer control. Built with PyQt5 and integrates with OctoPrint.

Key features:
- Touchscreen interface for printer control
- Real-time monitoring and status updates
- Dynamic settings management
- OctoPrint integration

[Learn more](Control%20Center/README.md)

### Image Slice Converter Demo
A utility for converting and processing image slices for DLP 3D printing.

[Learn more](Image%20Slice%20Converter%20Demo/sliceConverter.py)

### Robot Modbus Controller Demo
A Modbus-based control system for robotic components.

Features:
- Modbus communication interface
- Axis control and monitoring
- SFTP file transfer capabilities

[Learn more](Robot%20Modbus%20Controller%20Demo/README.md)

## Setup

Each project has its own requirements.txt file. Navigate to the specific project directory and install dependencies:

```sh
cd <project-directory>
pip install -r requirements.txt
```

## Development

- Use Visual Studio Code for development
- Python 3.x is required
- Qt Designer for UI development
- See individual project READMEs for specific setup instructions

## Contributing

Contributions are welcome! Please read the individual project documentation before submitting pull requests.