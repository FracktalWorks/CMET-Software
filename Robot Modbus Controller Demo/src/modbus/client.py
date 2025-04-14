from pymodbus.client.sync import ModbusTcpClient
from time import sleep

class ModbusClient:
    def __init__(self, ip='192.168.141.1', port=1502):
        self.client = ModbusTcpClient(ip, port)
        if not self.client.connect():
            raise ConnectionError(f"Unable to connect to Modbus server at {ip}:{port}")

    def send_command(self, address, value):
        try:
            # Write the command to the specified Modbus address
            self.client.write_coil(address, value)
            sleep(0.1)  # Wait for a short duration to ensure the command is processed
            # Reset the command bit after sending
            self.client.write_coil(address, False)
        except Exception as e:
            raise RuntimeError(f"Failed to send command to address {address}: {str(e)}")

    def close(self):
        self.client.close()