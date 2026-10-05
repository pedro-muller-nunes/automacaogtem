import time

from serial import Serial

class ArduinoSerial(Serial):
    def __init__(self, com_port : int, baudrate : int = 9600, timeout : float | int | None = 1):
        Serial.__init__(self, port=f'COM{com_port}', baudrate=baudrate, timeout=timeout)

    def send_command(self, command: str) -> None:
        self.write(command.upper().encode('ascii'))

    def read_ascii(self) -> str:
        return self.readline().decode('ascii').strip()

    def send_and_read(self, command: str, sleep_time: float | int) -> str:
        self.send_command(command)
        time.sleep(sleep_time)
        return self.read_ascii()
