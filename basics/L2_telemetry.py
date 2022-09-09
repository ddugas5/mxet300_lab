import L1_ina as ina
import L1_log as log2
from time import sleep

while(True):
    volts = ina.readVolts()
    log2.tmpFile(volts, "volt")
    sleep(5)