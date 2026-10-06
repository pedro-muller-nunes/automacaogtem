import time

from serial import Serial

class ArduinoSerial(Serial):
    def __init__(self, com_port : int, baudrate : int = 9600, timeout : float | int | None = 1, write_read_sleep_time : float = 0):
        Serial.__init__(self, port=f'COM{com_port}', baudrate=baudrate, timeout=timeout)
        self.write_read_sleep_time = write_read_sleep_time

    def send_command(self, command: str) -> None:
        self.write(command.upper().encode('ascii'))

    def read_ascii(self) -> str:
        return self.readline().decode('ascii').strip()

    def send_and_read(self, command: str, sleep_time: float | int | None = None) -> str:
        if sleep_time is None:
            sleep_time = self.write_read_sleep_time
        self.send_command(command)
        time.sleep(sleep_time)
        return self.read_ascii()

    def send_and_read_multiple(self, command: str, repetitions : int, sleep_btwn_write_read: float | int | None = None, sleep_btwn_commands: float | int | None = None) -> list:
        if sleep_btwn_write_read is None:
            sleep_btwn_write_read = self.write_read_sleep_time
        if sleep_btwn_commands is None:
            sleep_btwn_commands = self.timeout

        response = []

        for i in range(repetitions):
            response.append(self.send_and_read(command, sleep_btwn_write_read))
            time.sleep(sleep_btwn_commands)

        return response

    # Enviar múltiplos com uma lista de comandos... testar
    def send_and_read_list(self, commands: list, sleep_btwn_write_read: float | int | None = None, sleep_btwn_commands : int | float | None = None) -> list:
        if sleep_btwn_write_read is None:
            sleep_btwn_write_read = self.write_read_sleep_time
        if sleep_btwn_commands is None:
            sleep_btwn_commands = self.timeout

        response = []

        for command in commands:
            response.append(self.send_and_read(command, sleep_btwn_write_read))
            time.sleep(sleep_btwn_commands)

        return response
