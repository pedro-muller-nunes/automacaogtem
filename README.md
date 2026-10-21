# Automação de testes em célula GTEM - LACOM, DELET, UFRGS

Este código foi desenvolvido para automatizar os testes 
realizados na [célula GTEM](https://gtemcell.com/?lang=pt)
do Laboratório de Comunicações (LACOM) do Departamento de 
Engenharia Elétrica (DELET) da Universidade Federal do 
Rio Grande do Sul (UFRGS).

A célula GTEM é um dispositivo usado 
como guia de ondas para testes de caracterização e compatibilidade 
eletromagnética. Pode ser usada para testes de captação ou absorção 
de ondas eletromagnéticas em antenas ou de emissão delas em diferentes
dispositivos eletromagnéticos, como motores, por exemplo.

A automação é feita meio do controle de três
instrumentos: analisador de espectro Rohde &
Schwarz FSH4, gerador de sinais Rohde & Schwarz
SMB100A e rotor de antena Hy-Gain AR-500.

## Instrumentos controlados

* ### [Rohde & Schwarz SMB100A](https://www.rohde-schwarz.com/webhelp/smb100a_html_usermanual_1/SMB100A_HTML_UserManual.htm)
Gerador de sinais de RF e micro-ondas, usado como entrada de ondas 
eletromagnéticas na célula GTEM. Ele é controlado por meio da biblioteca
RsInstrument, desenvolvida pela própria Rohde & Schwarz. Ela serve como 
uma interface entre o Python a linguagem padrão dos instrumentos da 
empresa, SCPI, permitindo enviar comandos e controlá-los. Neste código, 
é acessado pela classe "SMB100A", encontrada no arquivo Python homônimo.

* ### [Rohde & Schwarz FSH4](https://scdn.rohde-schwarz.com/ur/pws/dl_downloads/dl_common_library/dl_manuals/dl_user_manual/FSH_OperatingManual_en_FW3.60~1.pdf)
Analisador de espectro com diversas funcionalidades, sendo o principal 
instrumento de medida dos testes na célula GTEM. Sendo da Rohde & Schwarz,
também é controlado por meio da biblioteca RsInstrument. Neste código, é 
acessado pela classe "FSH4".

* ### [Hy-Gain AR-500](https://drive.google.com/file/d/1Ui7qFmk4wRvHYsdwUo1Ipav8X_hi6TyV/view?usp=sharing)
O rotor conectado ao AR-500 é comandado por um 
microcontrolador que envia instruções por meio de pulsos 
emitidos por um LED infravermelho, emulando o controle 
remoto do próprio dispositivo. Os códigos enviados por 
infravermelho encontram-se no arquivo ```command_codes.h```.
Pode girar para a esquerda (L) e para a direita (R), possui 12 
espaços de memória para posições angulares e a possibilidade 
de calibrar seu sistema de medição de ângulo com a tecla INITIAL.

Neste código, o microcontrolador é acessado pela classe "MicroSerial".

## Estrutura do código
```
automacaogtem/
├── .env                        # Variáveis de ambiente, neste caso são os IPs dos instrumentos R&S
├── .gitignore
├── main.py                     # Código principal
├── README.md
├── requirements.txt            # Dependências
│
├── firmware/                   # Código do microcontrolador
│   └── controle_rotor/
│       └── commmand_codes.h    # Códigos do controle remoto do AR-500
│       └── controle_rotor.ino  
│
├── src/                        # Código-fonte Python
│   ├── classes/
│   │   ├── MicroSerial.py    # Classe para comunicação com microcontrolador
│   │   ├── FSH4.py
│   │   ├── Instrument.py       # Classe que herda RsInstrument e é herdada pelos instrumentos R&S
│   │   └── SMB100A.py
│   └── rotinas.py              # Rotinas comuns de configuração, varredura, etc.
│
└── tests/
    └── ...
```

* No código-fonte Python, as classes estão documentadas com *docstrings*.
