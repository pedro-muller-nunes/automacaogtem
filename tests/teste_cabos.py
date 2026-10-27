import time

import csv
import numpy as np
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
freq_max = 3.6e9
span = 1e6
sleep = 1

csv_path = '../data/sweep_cabo4_2.csv'

f_kilos = np.arange(100e3, 900e3+100e3, 100e3)
f_megas1 = np.arange(1e6, 9e6+1e6, 1e6)
f_megas2 = np.arange(10e6, 90e6+10e6, 10e6)
f_megas3 = np.arange(100e6, 900e6+100e6, 100e6)
f_gigas = np.arange(1e9, 3.6e9, 0.1e9)

f_megas = np.append(np.append(f_megas1, f_megas2), f_megas3)
freqs = np.append(np.append(f_kilos, f_megas), f_gigas)
freqs = np.append(freqs, 3.59e9)

# for f in freqs:
#     print(f'{f:.5e}')
# print(len(freqs))

# Código principal

rows = []

with open(csv_path, 'x', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['f', 'f_max', 'level_max'])

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
        print(f'{f:.3e}, {x:.3e}, {y}') # Só para ir vendo

        rows.append([f, x, y])

        time.sleep(sleep)

    csv_writer.writerows(rows)

fsh.close()
smb.close()
