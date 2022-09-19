import numpy as np                          # library for math operations
import time                                 # library for time access
from time import sleep
import L1_log as log2
import L1_encoder as enc
import L2_kinematics as kine
import L1_ina as ina
import L1_motor as motor


while(True):
    
    volts = ina.readVolts()
    log2.tmpFile(volts, "volt")
    
    wheel_speed = kine.getPdCurrent()
    log2.tmpFile(wheel_speed[0], "leftwheel")
    log2.tmpFile(wheel_speed[1], "rightwheel")
    print("Left Wheel (rad/s): {:.2f} \t Right Wheel (rad/s): {:.2f} \t".format(wheel_speed[0], wheel_speed[1]))

    chassis_speed = kine.getMotion()
    log2.tmpFile(chassis_speed[0], "forwardvelocity")
    log2.tmpFile(chassis_speed[1], "angularvelocity")
    print("Chassis Forward Velocity (m/s): {:.2f} \t Chassis Angular Velocity (rad/s): {:.2f} \t".format(chassis_speed[0], chassis_speed[1]))
    
    sleep(1)