import L1_lidar as lidar
import L2_vector as vector
import L1_log as log2
import numpy as np                          # library for math operations
import time                                 # library for time access
from time import sleep
import L1_ina as ina
import L1_motor as motor

while (True):
    
    my_vector = vector.getNearest()
    
    coordinates = vector.polar2cart(my_vector[0], my_vector[1])
    
    log2.tmpFile(my_vector[0], "m")
    log2.tmpFile(my_vector[1], "deg")
    
    log2.tmpFile(coordinates[0], "x")
    log2.tmpFile(coordinates[1], "y")
    
    
    