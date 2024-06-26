#PIN CONNECTIONS
#LED - 23 - GND
#PIR - 3.3V
#PIR - 18
#PIR - GND

from machine import Pin
from time import sleep

motion = False

def handle_interrupt(pin):
  global motion
  motion = True
  global interrupt_pin
  interrupt_pin = pin 

led = Pin(23, Pin.OUT)
pir = Pin(18, Pin.IN)

pir.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

while True:
  if motion:
    print('Motion detected! Interrupt caused by:', interrupt_pin)
    led.value(1)
    sleep(10)
    led.value(0)
    print('Motion stopped!')
    motion = False

