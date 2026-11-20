import time
import board
from adafruit_ads1x15 import ADS1115, AnalogIn, ads1x15

# Start I2C and create the ADS1115 object.
i2c = board.I2C()
ads = ADS1115(i2c)

# Create an input object for each channel.
channels = [
    AnalogIn(ads, ads1x15.Pin.A0),
    AnalogIn(ads, ads1x15.Pin.A1),
    AnalogIn(ads, ads1x15.Pin.A2),
    AnalogIn(ads, ads1x15.Pin.A3),
]

print("Reading ADS1115 channels. Press Ctrl+C to stop.")

try:
    while True:
        readings = [
            f"A{i}: {channel.voltage:.3f} V (raw {channel.value})"
            for i, channel in enumerate(channels)
        ]
        print(" | ".join(readings))
        time.sleep(1)

except KeyboardInterrupt:
    print("\nStopped.")
