# Rotinas, ensaios específicos... a fazer
import time

from src.classes.MicroSerial import MicroSerial
from src.classes.FSH4 import FSH4
from src.classes.SMB100A import SMB100A


def config_rs(fsh: FSH4, smb: SMB100A):
    fsh.auto_attenuation_on()
    fsh.set_attenuation_mode('LNO') # Ver qual é mais adequado...
    fsh.set_ref_level(0)
    # fsh.set_ref_offset(0)

    # ref position 8...
    # trace detector rms...

# Pode retornar algo...
def varredura_simples(fsh: FSH4, smb: SMB100A, freq : float | int, level : float | int, span : float | int, span_medicao : float | int):
    # Configurando analisador e gerador

    fsh.clear_status()
    # smb.clear_status() # Opcional?

    fsh.set_freq_center(freq)
    fsh.set_freq_span(span)
    # fsh.set_ref_level(0)
    fsh.cont_sweep_off()
    fsh.query_opc()

    smb.set_freq(freq)
    smb.set_level(level)
    smb.output_on()
    smb.query_opc()

    # Uma varredura
    fsh.sweep()
    fsh.query_opc()

    # Desligando gerador
    smb.output_off()
    smb.query_opc()

    # trace = fsh.query_bin_or_ascii_float_list('TRAC:DATA? TRACE1')
    # isso que não ta funcionando ainda

    # Medindo com o analisador

    freq_medidas = [
        freq - span / 2,
        freq - span_medicao,
        freq - span_medicao / 2,
        freq,
        freq + span_medicao / 2,
        freq + span_medicao,
        freq + span / 2
    ]

    for f in freq_medidas:
        fsh.set_marker_x(f)
        x, y = fsh.get_marker_x(), fsh.get_marker_y()
        print(f'{x:.4e} Hz {y:.2f} dBm')

    # Pegando o pico
    fsh.set_to_peak()
    x_max, y_max = fsh.get_marker_x(), fsh.get_marker_y()
    print(f'Pico: {x_max:.7e} Hz {y_max:.2f} dBm')

    # fsh.cont_sweep_on() # Opcional

def config_rotor(micro: MicroSerial):
    micro.dtr = True # Ver o que faz e se precisa
    micro.rts = True
    time.sleep(micro.timeout)

    micro.reset_input_buffer()
    micro.reset_output_buffer()
    time.sleep(micro.timeout)

def calibrar_rotor(micro: MicroSerial):
    micro.send_and_read("POS_L")
    time.sleep(60) # Tempo médio para ir de 0 a 360 (fazer mais medições)
    micro.send_and_read("INI")
    time.sleep(60)
    micro.send_and_read("POS_A")
