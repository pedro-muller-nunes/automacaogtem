import time

from src.classes.ArduinoSerial import ArduinoSerial

arduino = ArduinoSerial(4, baudrate=9600, timeout=1.2, write_read_sleep_time=0.01)
arduino.dtr = True # Ver o que faz e se precisa
arduino.rts = True
time.sleep(2)

arduino.reset_input_buffer()
arduino.reset_output_buffer()
time.sleep(2)

command = "R"
times = 1

print(command)

res = arduino.send_and_read_multiple(command, times)
print(res)
print(len(res))

arduino.close()
