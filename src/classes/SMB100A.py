from src.classes.Instrument import Instrument

class SMB100A(Instrument):
    def __init__(self, ip: str, options: str | None = None):
        Instrument.__init__(self, ip, True, True, options)

    def get_output_state(self) -> bool:
        """Diz o estado da saída RF do instrumento."""
        return self.query_bool('OUTP:STAT?')

    def output_on(self) -> None:
        """Liga a saída RF do instrumento."""
        self.write('OUTP:STAT ON')

    def output_off(self) -> None:
        """Desliga a saída RF do instrumento."""
        self.write('OUTP:STAT OFF')

    def get_freq(self) -> float | int:
        """Retorna a frequência que o instrumento produz na saída RF em Hz."""
        return self.query_float('SOUR:FREQ?')

    def set_freq(self, freq: float | int) -> None:
        """Define a frequência que o instrumento produz na saída RF em Hz."""
        self.write(f'SOUR:FREQ {freq}')

    def get_level(self) -> float | int:
        """Retorna o nível que o instrumento produz na saída RF em dBm."""
        return self.query_float('SOUR:POW:LEV:IMM:AMPL?')

    def set_level(self, level: float | int) -> None:
        """Define o nível que o instrumento produz na saída RF em dBm."""
        self.write(f'SOUR:POW:LEV:IMM:AMPL {level}')
