# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 14:25:35 2015

@author: Jason
"""

import math as m
import time

class AstroPiSim:
    def __init__(self):
        self.humidity = 50
        self.temp = 50
    
    def pixelToChar(self, pixel):
        '''
        converts a pixel tri color value to a text
        character
        '''
        if max(pixel) == 0:
            return '.'
        else:
            return'X'
    
    def get_humidity(self):
        '''
        simulate a humidity reading that
        fluxuates with time
        '''
        return int(49 * m.sin(time.time()/10) + 49)
    
    def get_temp(self):
        '''
        simulate a temperature reading that
        fluxuates with time
        '''
        return int(25 * m.sin(time.time()/10) + 25)
    
    def set_pixels(self, pixels):
        '''
        simulates setting all of the pixels on the
        AstroPi to the given color
        '''
        for c in range(8):
            for r in range(7,-1, -1):
                print self.pixelToChar(pixels[r * 8 + c]),
            print ' '
        print ' '

