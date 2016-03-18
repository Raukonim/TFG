# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 13:46:47 2016

@author: a.fajula
"""

from __future__ import division
from pylab import*

interactive(True)
close('all')

class Camera(object):
    
    def __init__(self):
        self.sensor_x = 14.8
        self.sensor_y = 22.2
        self.sensor_ratio = 3/2
    

class ElementalImage(object):
    
    def __init__(self, directory, name):
        
        self.ei_directory = directory
        self.ei_name = name
        self.ei_x = int(self.ei_name[4:6])
        self.ei_y = int(self.ei_name[7:9])
        self.ei_z = int(self.ei_name[10:12])
        
        self.image = self.load(self.ei_directory,self.ei_name)
        self.ei_pixel_x = int(shape(self.image)[0])
        self.ei_pixel_y = int(shape(self.image)[1])
    
    def load(self, path, name):
        image = double(imread(path+name))
        image /= image.max()
        
        return image

class IntegralImage(object):
    
    def __init__(self):
        something


image_directory='ei1_5x3_p4\\'
ei1='ei1_00_00_00_1.jpg'
ei2='ei1_00_00_00_2.jpg'
ei3='ei1_00_00_00_3.jpg'
#imatge1=double(imread(image_directory+ei1))/255
#imatge2=double(imread(image_directory+ei2))/255
#imatge3=double(imread(image_directory+ei3))/255
#
#mitja1=(imatge1+imatge2+imatge3)/3
#imsave(image_directory+'mitjana1',mitja1)