import os
import psutil
import time
from time import sleep
curtemp = None
limits = (78, 80)
while True:
    temps = psutil.sensors_temperatures()
    print(f"current temperature: {temps['nvme'][0].current}º")
    high_temp = limits[0]
    critical_temp = limits[1]
    if temps['nvme'][0].current > high_temp:
        print("the temperature have gotten dangerous, please take a break")
    elif temps['nvme'][0].current > critical_temp:
        print("the temperature is extremely dangerous, please take a break imediatly")
    else:
        print("the temp is okay")
    sleep(1)
    os.system("clear")