from dotenv import dotenv_values

from src import rotinas
from src.classes.FSH4 import FSH4
from src.classes.SMB100A import SMB100A

config = dotenv_values('.env')

# Instrumentos

ip_fsh = config.get('IP_FSH') or 'Erro'
ip_smb = config.get('IP_SMB') or 'Erro'

options_fsh = 'StbInErrorCheck = False, SkipStatusSystemSettings = True, SkipClearStatus = True'

fsh = FSH4(ip_fsh, options_fsh)
smb = SMB100A(ip_smb)

# Variáveis

freq = 1e9
span = 10e6
level = -30
span_med = 1e6

# Exemplo

# Configurar motor

rotinas.varredura_simples(fsh, smb, freq, span, level, span_med)

# Mexer no motor

# Fazer outra varredura

# Fechando conexões

fsh.close()
smb.close()
