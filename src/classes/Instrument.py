from RsInstrument import RsInstrument

class Instrument(RsInstrument):
    def __init__(self, ip: str, id_query: bool, reset: bool, options: str | None = None):
        resource_name = f'TCPIP::{ip}::INSTR'
        RsInstrument.__init__(self, resource_name, id_query, reset, options=options)

    def query_idn(self) -> str:
        """Realiza uma query de identificação do instrumento."""
        return self.query('*IDN?')

    def opc(self) -> None:
        """Realiza uma query OPC, o que faz com que o instrumento espere as operações serem concluídas para continuar."""
        self.query_opc()

    # Não sei se é útil
    # @staticmethod
    # def opc_mult(*instruments: RsInstrument) -> None:
    #     for instrument in instruments:
    #         instrument.query_opc()
