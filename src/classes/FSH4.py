from src.classes.Instrument import Instrument

# Fazer:
# Pegar trace.
# docstrings: precisa melhorar o padrão?

class FSH4(Instrument):
    def __init__(self, ip: str, options: str | None = None):
        Instrument.__init__(self, ip, True, False, options=options)

    def cont_sweep_on(self) -> None:
        """Liga a varredura contínua."""
        self.write('INIT:CONT ON')

    def cont_sweep_off(self) -> None:
        """Desliga a varredura contínua."""
        self.write('INIT:CONT OFF')

    def sweep(self) -> None:
        """Faz uma varredura. Só funciona se a varredura contínua está desligada."""
        self.write('INIT:IMM')

    def get_freq_center(self) -> float | int:
        """Retorna a frequência central do instrumento em Hz."""
        return self.query_float('FREQ:CENT?')

    def set_freq_center(self, center: float | int) -> None:
        """Define a frequência central do instrumento em Hz."""
        self.write(f'FREQ:CENT {center}')

    # Precisa?
    # def set_freq_center_ghz(self, center: float | int) -> None:
    #     """Define a frequência central do instrumento em GHz."""
    #     self.write(f'FREQ:CENT {center}GHz')

    def get_freq_span(self) -> float | int:
        """Retorna o span de frequências do instrumento em Hz."""
        return self.query_float('FREQ:SPAN?')

    def set_freq_span(self, span: float | int) -> None:
        """Define o span de frequências do instrumento em Hz."""
        self.write(f'FREQ:SPAN {span}')

    def set_freqs(self, center: float | int, span: float | int):
        """Define a frequência central e o span de frequências do instrumento, ambos em Hz."""
        self.write(f'FREQ:CENT {center};:FREQ:SPAN {span}')

    # TRAC pode ser 1 ou 2... como marker

    def get_ref_level(self) -> float | int:
        """Retorna o nível de referência do instrumento em dBm."""
        return self.query_float('DISP:TRAC:Y:RLEV?')

    def set_ref_level(self, level: float | int) -> None:
        """Define o nível de referência do instrumento em dBm."""
        self.write(f'DISP:WIND:TRAC:Y:RLEV {level}')

    # problema...
    # def get_ref_offset(self) -> float | int:
    #     return self.query_float('DISP:TRAC:SCAL:Y:OFFS?')

    # problema...
    # def set_ref_offset(self, offset: float | int) -> None:
    #     self.write(f'DISP:WIND:TRAC:SCAL:Y:OFFS {offset}')

    # Atenuação

    def is_auto_attenuation_on(self) -> bool:
        return self.query_bool('INP:ATT:AUTO?')

    def auto_attenuation_on(self) -> None:
        self.write('INP:ATT:AUTO ON')

    def auto_attenuation_off(self) -> None:
        self.write('INP:ATT:AUTO OFF')

    def get_attenuation(self) -> float | int:
        return self.query_float('INP:ATT?')

    def set_attenuation(self, attenuation: float | int) -> None:
        self.write(f'INP:ATT {attenuation}')

    def  get_attenuation_mode(self) -> str:
        return self.query('INP:ATT:MODE?')

    # Convém trocar str por um Enum
    def set_attenuation_mode(self, mode: str) -> None:
        self.write(f'INP:ATT:MODE {mode}')

    # Cursores
    def set_marker_x(self, x: float | int, marker: int = 1) -> None:
        """
        Define a posição x de um cursor.

        Parâmetros:
            marker (int): Identificador do cursor (de 1 a 6).
        """
        self.write(f'CALC:MARK{marker}:X {x}')

    def get_marker_x(self, marker: int = 1) -> float | int:
        """
        Retorna a posição x (frequência) de um cursor.

        Parâmetros:
            marker (int): Identificador do cursor (de 1 a 6).
        """
        return self.query_float(f'CALC:MARK{marker}:X?')

    def get_marker_y(self, marker: int = 1) -> float | int:
        """
        Retorna a posição y (nível) de um cursor.

        Parâmetros:
            marker (int): Identificador do cursor (de 1 a 6).
        """
        return self.query_float(f'CALC:MARK{marker}:Y?')

    def set_to_peak(self, marker: int = 1) -> None:
        """
        Move o cursor para o pico do espectro.

        Parâmetros:
            marker (int): Identificador do cursor (de 1 a 6).
        """
        self.write(f'CALC:MARK{marker}:MAX')

    def set_to_min(self, marker: int = 1) -> None:
        """
        Move o cursor para o valor mínimo do espectro.

        Parâmetros:
            marker (int): Identificador do cursor (de 1 a 6).
        """
        self.write(f'CALC:MARK{marker}:MIN')

    # Pode fazer um que lê o pico/mínimo e volta pro lugar que tava.

    # Unidades
    # def get_unit_pow(self) -> str:
    #     return self.query(f'POW:UNIT?')

    # def auto_attenuation_on(self):
