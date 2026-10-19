from dotenv import dotenv_values

from src.classes.FSH4 import FSH4

config = dotenv_values('../.env')

ip_fsh = config.get('IP_FSH') or 'Erro'

options_fsh = 'StbInErrorCheck = False, SkipStatusSystemSettings = True, SkipClearStatus = True'

fsh = FSH4(ip_fsh, options_fsh)
fsh.clear_status()

# fsh.write('INP:ATT:AUTO ON')
# fsh.write('INP:ATT:AUTO OFF')
# fsh.auto_attenuation_off()

# fsh.write('INP:ATT:MODE LDIS')
# fsh.write('INP:ATT:MODE LNO')
# fsh.set_attenuation_mode('LNO')

fsh.auto_attenuation_on()
fsh.auto_attenuation_off()
fsh.auto_attenuation_on()
fsh.set_attenuation_mode('LNO')
fsh.set_ref_level(0)
# fsh.set_ref_offset(0) # Esse não ta funcionando

print(fsh.get_ref_level())
# print(fsh.get_ref_offset())
print(fsh.get_attenuation())
print(fsh.get_attenuation_mode())
print(fsh.is_auto_attenuation_on())

fsh.close()
