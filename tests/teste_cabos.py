import time

import numpy
from dotenv import dotenv_values

import rotinas
from src.classes.FSH4 import FSH4
from src.classes.SMB100A import SMB100A

config = dotenv_values('../.env')

# Instrumentos

ip_fsh = config.get('IP_FSH') or 'Erro'
ip_smb = config.get('IP_SMB') or 'Erro'

options_fsh = 'StbInErrorCheck = False, SkipStatusSystemSettings = True, SkipClearStatus = True'

fsh = FSH4(ip_fsh, options_fsh)
rotinas.config_fsh(fsh)
fsh.clear_status()

smb = SMB100A(ip_smb)

# Variáveis

level = 0
freq_min = 100e3
freq_max = 1000e3 # 3.6e9
span = 1e6
sleep = 3

num_freq = 10
freqs = numpy.linspace(freq_min, freq_max, num_freq)

# Código principal

smb.set_level(level)

for f in freqs:
    smb.set_freq(f)
    fsh.set_freq_center(f)
    fsh.set_freq_span(span)

    fsh.cont_sweep_off()
    fsh.query_opc()

    smb.output_on()
    smb.query_opc()

    fsh.sweep()
    fsh.query_opc()

    smb.output_off()
    smb.query_opc()

    fsh.set_to_peak()
    x, y = fsh.get_marker_x(), fsh.get_marker_y()
    print(f'{f:.3e} Hz: {x:.3e} Hz, {y} dBm')

    time.sleep(sleep)

fsh.close()
smb.close()
