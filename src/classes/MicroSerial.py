import time

from serial import Serial

class MicroSerial(Serial):
    def __init__(self, com_port : int, baudrate : int = 9600, timeout : float | int | None = 1, write_read_sleep_time : float = 0):
        Serial.__init__(self, port=f'COM{com_port}', baudrate=baudrate, timeout=timeout)
        self.write_read_sleep_time = write_read_sleep_time

    def send_command(self, command: str) -> None:
        """Envia um comando ao microcontrolador."""
        self.write(command.upper().encode('ascii'))

    def read_ascii(self) -> str:
        """Lê uma linha da porta serial."""
        return self.readline().decode('ascii').strip()

    def send_and_read(self, command: str, sleep_btwn_write_read: float | int | None = None) -> str:
        """
        Envia um comando ao microcontrolador e lê uma linha na porta serial.

        Parâmetros:
            command (str): Comando a ser enviado.
            sleep_btwn_write_read (float | int): Tempo esperado entre o envio e a leitura da resposta ao comando.

        Retorna:
            Resposta ao comando enviado.
        """

        if sleep_btwn_write_read is None:
            sleep_btwn_write_read = self.write_read_sleep_time
        self.send_command(command)
        time.sleep(sleep_btwn_write_read)
        return self.read_ascii()

    def send_and_read_multiple(self, command: str, repetitions : int, sleep_btwn_write_read: float | int | None = None, sleep_btwn_commands: float | int | None = None) -> list:
        """
        Envia um mesmo comando múltiplas vezes e lê as respostas na porta serial.

        Parâmetros:
            command (str): Comando a ser enviado.
            repetitions (int): Vezes que o comando é enviado.
            sleep_btwn_write_read (float | int): Tempo esperado entre o envio e a leitura da resposta ao comando.
            sleep_btwn_commands (float | int): Tempo esperado entre dois comandos.

        Retorna:
            response (list): Lista de respostas aos comandos enviados.
        """

        if sleep_btwn_write_read is None:
            sleep_btwn_write_read = self.write_read_sleep_time
        if sleep_btwn_commands is None:
            sleep_btwn_commands = self.timeout

        response = []

        for i in range(repetitions):
            response.append(self.send_and_read(command, sleep_btwn_write_read))
            time.sleep(sleep_btwn_commands)

        return response

    def send_and_read_list(self, commands: list, sleep_btwn_write_read: float | int | None = None, sleep_btwn_commands : int | float | None = None) -> list:
        """
        Envia uma lista de comandos e lê as respostas na porta serial.

        Parâmetros:
            commands (list): Lista de comandos a serem enviados.
            sleep_btwn_write_read (float | int): Tempo esperado entre o envio e a leitura da resposta ao comando.
            sleep_btwn_commands (float | int): Tempo esperado entre dois comandos.

        Retorna:
            response (list): Lista de respostas aos comandos enviados.
        """

        if sleep_btwn_write_read is None:
            sleep_btwn_write_read = self.write_read_sleep_time
        if sleep_btwn_commands is None:
            sleep_btwn_commands = self.timeout

        response = []

        for command in commands:
            response.append(self.send_and_read(command, sleep_btwn_write_read))
            time.sleep(sleep_btwn_commands)

        return response

    # def go_to_pos(self, position : str, sleep : float | int = 0) -> str:
    #     return self.send_and_read(f'POS_{position}', sleep)
