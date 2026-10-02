import time

from src.classes.Arduino import Arduino

arduino = Arduino(4, baudrate=9600, timeout=1)
# arduino.dtr = True # Ver o que faz e se precisa
# arduino.rts = True
time.sleep(2)

arduino.reset_input_buffer()
arduino.reset_output_buffer()
time.sleep(2)

comando = "R"
arduino.send_command(comando)
time.sleep(0.01)
print(arduino.read_ascii())
time.sleep(0.01)

# tempo = 3
#
# for i in range(20):
#     arduino.send_command("R")
#     time.sleep(0.01)
#     arduino.read_ascii()
#     time.sleep(tempo)
#     arduino.send_command("R")
#     time.sleep(0.01)
#     arduino.read_ascii()
#     time.sleep(tempo)
#     arduino.send_command("POS_B")
#     time.sleep(0.01)
#     arduino.read_ascii()
#     time.sleep(tempo)


# for i in range(10):
#     arduino.send_command(comando)
#     time.sleep(0.01) # Essencial o tempo entre enviar o comando e ler a resposta
#     arduino.read_ascii()
#     time.sleep(0.01)

# print(f'Comando: \"{comando}\"')
# print(f'Resposta: \"{res}\"')
