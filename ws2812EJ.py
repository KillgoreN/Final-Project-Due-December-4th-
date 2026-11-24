from rpi5_ws2812.ws2812 import Color, WS2812SpiDriver
import time
import random

if __name__ == "__main__":

    # Initialize the WS2812 strip with 100 leds and SPI channel 0, CE0
    try:
        i = 0
        j = 0
        loop = 0
        strip = WS2812SpiDriver(spi_bus=0, spi_device=0, led_count= 27).get_strip()
        while loop < 10:
            rand_int = random.randint(0,255)
            rand_inte = random.randint(0,255)
            rand_integ = random.randint(0,255)
            for i in range(0, 27, 2):
                strip.set_pixel_color(i,Color(rand_int, rand_inte, rand_integ))
                strip.show()
                time.sleep(0.04)
                print(i)

            #reverse traversal
            for i in range(1, 26, 2):
                strip.set_pixel_color(i,Color(rand_inte, rand_integ, rand_int))
                strip.show()
                time.sleep(.04)
                
            strip.clear()
            loop += 1
            
            
            
    finally:
        strip.clear()