import time

import csv
from dotenv import dotenv_values

import rotinas
from classes.MicroSerial import MicroSerial
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

arduino = MicroSerial(4, baudrate=9600, timeout=1.2, write_read_sleep_time=0.01)
arduino.dtr = True
arduino.rts = True
time.sleep(2)
arduino.reset_input_buffer()
arduino.reset_output_buffer()
time.sleep(2)

# Variáveis
ANG_MIN = 3.457844184 # em graus

level = 0
freq = 915e6
pos = 105 # 105 é para ser o necessário, bom colocar umas a mais para redundância

span = 1e6
sleep = 1

csv_path = '../data/gd_horizontal_2.csv'

# Principal
with open(csv_path, 'x', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['ang_est', 'f_max', 'level_max'])

    smb.set_level(level)

    smb.set_freq(freq)
    fsh.set_freq_center(freq)
    fsh.set_freq_span(span)

    smb.output_on()
    smb.query_opc()

    print('Começou')

    for p in range(pos):
        fsh.cont_sweep_off()
        fsh.query_opc()

        fsh.sweep()
        fsh.query_opc()

        fsh.set_to_peak()
        x, y = fsh.get_marker_x(), fsh.get_marker_y()
        print(f'P{p} - {p*ANG_MIN:.3f}° - {x:.3e} - {y}')

        csv_writer.writerow([p*ANG_MIN, x, y])

        arduino.send_and_read("R")

        time.sleep(sleep)

    smb.output_off()
    smb.query_opc()

fsh.close()
smb.close()
