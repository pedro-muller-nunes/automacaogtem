from serial import Serial

class Arduino(Serial):
    def __init__(self, com_port : int, baudrate : int = 9600, timeout : float | int | None = 1):
        Serial.__init__(self, port=f'COM{com_port}', baudrate=baudrate, timeout=timeout)

    def send_command(self, command: str):
        self.write(command.upper().encode('ascii'))

    def read_ascii(self) -> str:
        return self.readline().decode('ascii').strip()
