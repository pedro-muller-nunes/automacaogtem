from dotenv import dotenv_values

from src.classes.SMB100A import SMB100A

config = dotenv_values('../../.env')

ip_smb = config.get('IP_SMB') or 'Erro'

smb = SMB100A(ip_smb)

print(smb.query_idn())

print('\nFrequência')
print(smb.get_freq())
smb.set_freq(241e6)
print(smb.get_freq())

print('\nMagnitude')
print(smb.get_level())
smb.set_level(-11)
print(smb.get_level())

# Voltar ao que estava
smb.set_freq(800e6)
smb.set_level(-15)

smb.close()
