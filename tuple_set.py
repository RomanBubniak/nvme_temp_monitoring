import os
import psutil
import time
from time import sleep
curtemp = None
temp_status = None
def temp_check(some_variable, critical_limit, high_limit):
    if some_variable > critical_limit:
        temp_status = "the temperature is extremely dangerous, please take a break imediatly"
    elif some_variable > high_limit:
        temp_status = "the temperature have gotten dangerous, please take a break"
    else:
        temp_status = "the temp is okay"
    return temp_status
while True:
    temps = psutil.sensors_temperatures()
    print(f"current NVME's temperature: {temps['nvme'][0].current}")
    temp_check1 = temp_check(temps['nvme'][0].current, 80, 78)
    print(temp_check1)
    
    print(f"current NVME's sensor 2 temperature{temps['nvme'][1].current}")
    temp_check2 = temp_check(temps['nvme'][1].current, 80, 78)
    print(temp_check2)

    print(f"current k10temp temperature{temps['k10temp'][0].current}")
    temp_check3 = temp_check(temps['k10temp'][0].current, 80, 78)
    print(temp_check3)

    print(f"current AMDGPU temperature{temps['amdgpu'][0].current}")
    temp_check4 = temp_check(temps['amdgpu'][0].current, 80, 78)
    print(temp_check4)
    sleep(1)
    os.system("clear")