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
    
    def __init__(self, directory, name, camera):
        
        self.ei_directory = directory
        self.ei_name = name
        self.ei_x = int(self.ei_name[7:9])
        self.ei_y = int(self.ei_name[10:12])
        self.ei_z = int(self.ei_name[13:15])
        
        self.image = self.load(self.ei_directory,self.ei_name)
        self.ei_pixel_x = int(shape(self.image)[0])
        self.ei_pixel_y = int(shape(self.image)[1])
        
        self.pixel_x = camera['sensor_x']/camera['x_pixels']
        self.pixel_y = camera['sensor_y']/camera['y_pixels']
        
        self.ei_size = [self.ei_pixel_x*self.pixel_x,self.ei_pixel_y*self.pixel_y]

    
    def load(self, path, name):
        image = double(imread(path+name))
        #print shape(image)
        image /= image.max()
        image = image[650:3680,650:,:]
        
        return image

class IntegralImage(object):
    
    def __init__(self, camera, ei_path):
        
        self.sensor_x = camera['sensor_x']
        self.sensor_y = camera['sensor_y']
        self.sensor_ratio = camera['sensor_ratio']
        self.sensor_array = [int(camera['sensor_array'][0]),int(camera['sensor_array'][-1])]
        self.sensor_focal = int(camera['sensor_focal'])
        
        self.ei_list = self.load_ei(ei_path)
        
        self.oxy = self.normalization_array()
        
        
    def load_ei(self, path):
        elemental_images = []
        for filename in os.listdir(path):
            #print filename
            img = ElementalImage(path,filename, camera)
            elemental_images.append(img)
        return elemental_images
    
    def normalization_array(self):
        x_length = self.ei_list[0].ei_pixel_x
#        print x_length
        y_length = self.ei_list[0].ei_pixel_y
#        print y_length
        pixel_pitch_x = 4 / self.ei_list[0].pixel_x
#        print pixel_pitch_x
        pixel_pitch_y = 4 / self.ei_list[0].pixel_y
#        print pixel_pitch_y
        
        normalization = zeros([self.ei_list[0].ei_pixel_x+(2*pixel_pitch_x)-1,
                              self.ei_list[0].ei_pixel_y+(4*pixel_pitch_y),3])
#        figure()
#        k=0
        for i in range(self.sensor_array[0]):
            for j in range(self.sensor_array[1]):
                normalization[i*pixel_pitch_x:(i*pixel_pitch_x)+x_length,
                              j*pixel_pitch_y:(j*pixel_pitch_y)+y_length,:] += 1
#                subplot(3,5,i+j+1)
#                imsave(str(k)+'.png',normalization)
#                k+=1
#                print i, j, normalization
        normalization = normalization[pixel_pitch_x:-pixel_pitch_x,2*pixel_pitch_y:-2*pixel_pitch_y]
        imsave('Oxy.png', normalization)
        return normalization
    
    def constructor(self,depth):
        
        z = depth
        Nx = self.ei_list[0].ei_pixel_x
        Ny = self.ei_list[0].ei_pixel_y
        pitch = 4 #mm
        cx = self.ei_list[0].ei_size[0] #mm
        cy = self.ei_list[0].ei_size[1] #mm
        g = self.sensor_focal
        M = z / g
        x_arg = int((Nx*pitch)/(M*cx))
        y_arg = int((Ny*pitch)/(M*cy))
        print x_arg, y_arg
#        size = [445]
#        for i in range(3):
#            size.append(array(shape(self.ei_list[0].image))[i])
#        print size
        integral = zeros(shape(self.oxy))
#        integral = zeros([Nx,Ny,3])
        ei_num = 0
        for k in range(self.sensor_array[0]) :
            for l in range(self.sensor_array[1]):
                Ekl = self.ei_list[ei_num].image
                integral += Ekl
                print k, l
                ei_num +=1
                
        return integral/self.oxy



camera = {
        'sensor_x' : 14.8,
        'sensor_y' : 22.2,
        'sensor_ratio' : 3/2,
        'x_pixels' : 2592,
        'y_pixels' : 3888,
        'sensor_array' : '3x5',
        'sensor_focal' : 18
}

image_directory='ei1_5x3_p4\\'
ei1='ei1_00_00_00_1.jpg'
ei2='ei1_00_04_00_1.jpg'
ei3='ei1_00_08_00_2.jpg'

