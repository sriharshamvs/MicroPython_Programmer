import machine
import time
pin = machine.Pin(2, machine.Pin.OUT)
for i in range(5):
    pin.value(1)
    time.sleep(0.5)
    pin.value(0)
    time.sleep(0.5)
pin.on()  # Turns off the LED

print('Hello world! I can count to 10:')
for i in range(1, 11):
    print(i)
