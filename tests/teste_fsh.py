from dotenv import dotenv_values

from src.classes.FSH4 import FSH4

config = dotenv_values('../.env')

ip_fsh = config.get('IP_FSH') or 'Erro'

options_fsh = 'StbInErrorCheck = False, SkipStatusSystemSettings = True, SkipClearStatus = True'

fsh = FSH4(ip_fsh, options_fsh)
fsh.clear_status()

print(fsh.full_instrument_model_name)
print(fsh.query_idn())

print('\nFrequência central')
print(f'Antiga: {fsh.get_freq_center()}')
fsh.set_freq_center(0.5e9)
print(f'Nova: {fsh.get_freq_center()}')

print('\nFrequência central e span')
print(fsh.get_freq_center(), fsh.get_freq_span())
fsh.set_freqs(0.9e9, 100e6)
print(fsh.get_freq_center(), fsh.get_freq_span())

# print('\nNível de referência')
# print(fsh.get_ref_level())
# fsh.set_ref_level(-10)
# print(fsh.get_ref_level())

print('\nCursor')
print(f'x antigo: {fsh.get_marker_x()}')
fsh.set_marker_x(0.925e9)
print(f'x novo: {fsh.get_marker_x()}')
print(f'y: {fsh.get_marker_y()}')

# Voltar ao que estava
fsh.set_freq_center(2.5e9)
fsh.set_freq_span(1e9)
fsh.set_marker_x(2.5e9)
# fsh.set_ref_level(0)

fsh.close()
