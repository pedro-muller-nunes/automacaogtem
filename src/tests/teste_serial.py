import time

from src.classes.ArduinoSerial import ArduinoSerial

arduino = ArduinoSerial(4, baudrate=9600, timeout=1)
# arduino.dtr = True # Ver o que faz e se precisa
# arduino.rts = True
time.sleep(2)

arduino.reset_input_buffer()
arduino.reset_output_buffer()
time.sleep(2)

arduino.send_command("POS_A")
print(arduino.read_ascii())
time.sleep(2)

arduino.send_command("R")
print(arduino.read_ascii())

# print(f'Comando: \"{comando}\"')
# print(f'Resposta: \"{res}\"')
