# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 13:46:47 2016

@author: a.fajula
"""

from __future__ import division
from pylab import*
import os

interactive(True)
close('all')


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
        image = image[650:3680,650:,:]
        
        return image

class IntegralImage(object):
    
    def __init__(self, camera, ei_path):
        
        self.sensor_x = camera['sensor_x']
        self.sensor_y = camera['sensor_y']
        self.sensor_ratio = camera['sensor_ratio']
        
        self.ei_list = self.load_ei(ei_path)
        
    def load_ei(self, path):
        elemental_images = []
        for filename in os.listdir(path):
            #print filename
            img = ElementalImage(path,filename)
            elemental_images.append(img)
        return elemental_images
    
    def constructor(self):
        
        size = [445]
        for i in range(3):
            size.append(array(shape(self.ei_list[0].image))[i])
        print size
        integral = zeros(size)
        ei_num = 0
        for ei in ei_list:
            #integral[] = 
        
        
        return integral


camera = {
        'sensor_x' : 14.8,
        'sensor_y' : 22.2,
        'sensor_ratio' : 3/2
}

image_directory='ei1_5x3_p4\\'
ei1='ei1_00_00_00_1.jpg'
ei2='ei1_00_04_00_1.jpg'
ei3='ei1_00_08_00_2.jpg'

