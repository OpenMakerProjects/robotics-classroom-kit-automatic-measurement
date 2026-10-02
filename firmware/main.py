from microbit import *

PROJECT_ID = 1462
THRESHOLD = 470
confirmations = 0

while True:
    reading = pin0.read_analog()
    active = reading >= THRESHOLD
    confirmations = min(confirmations + 1, 4) if active else 0
    output = confirmations >= 4
    pin1.write_digital(1 if output else 0)
    display.show(Image.YES if output else Image.NO)
    print((PROJECT_ID, reading, int(output)))
    sleep(500)
