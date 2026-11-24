from rpi5_ws2812.ws2812 import Color, WS2812SpiDriver
import time

if __name__ == "__main__":

    # Initialize the WS2812 strip with 100 leds and SPI channel 0, CE0
    try:
        i = 0
        j = 0
        loop = 0
        strip = WS2812SpiDriver(spi_bus=0, spi_device=0, led_count= 27).get_strip()
        while loop < 5:
            for i in range(27):
                strip.set_pixel_color(i,Color(255, 0, 0))
                strip.show()
                time.sleep(0.1)
                print(i)
            
            
            
            #reverse traversal
            for i in range(26, -1, -1):
                strip.set_pixel_color(i,Color(0, 99, 0))
                strip.show()
                time.sleep(.1)
                
            
            loop += 1
            
            
            
    finally:
        strip.clear()