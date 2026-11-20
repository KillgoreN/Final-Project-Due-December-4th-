import time
import RPi.GPIO as GPIO

ROW = 21
COLS = [23, 12, 16, 20]  # GPIO 26 is the additional pin
KEYS = ["3", "4", "1", "2"]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Row is driven high; column inputs detect a pressed key.
GPIO.setup(ROW, GPIO.OUT, initial=GPIO.LOW)

for pin in COLS:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("Press a keypad button. Press Ctrl+C to stop.")

try:
    while True:
        GPIO.output(ROW, GPIO.HIGH)

        for pin, key in zip(COLS, KEYS):
            if GPIO.input(pin) == GPIO.HIGH:
                print(f"Pressed: {key} (GPIO {pin})")
                time.sleep(0.25)  # debounce

        GPIO.output(ROW, GPIO.LOW)
        time.sleep(0.01)

except KeyboardInterrupt:
    print("\nStopped.")

finally:
    GPIO.cleanup()
