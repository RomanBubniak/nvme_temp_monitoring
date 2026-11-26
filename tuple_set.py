import os
import psutil
import time
from time import sleep
curtemp = None
temp_status = None
def get_limit(prompt):
    while True:
        raw = input(prompt).strip().replace(",", ".")
        if raw.count(".") <= 1 and raw.replace(".", "", 1).isdigit():
            return float(raw)
        print("Enter the propriate number, example 75 or 74,5")
print("enter your high and critical temperatures")
print("NVMe SSD")
high_NVMeSSD = get_limit("high: ")
critical_NVMeSSD = get_limit("critical: ")
print("NVMe controller")
high_NVMecontroller = get_limit("high: ")
critical_NVMecontroller = get_limit("critical: ")
print("CPU")
high_CPU = get_limit("high: ")
critical_CPU =get_limit ("critical: ")
print("iGPU")
high_iGPU = get_limit("high: ")
critical_iGPU = get_limit("critical: ")

def temp_check(some_variable, critical_limit, high_limit):
    if some_variable > critical_limit:
        temp_status = "the temperature is extremely dangerous, please take a break imediatly"
    elif some_variable > high_limit:
        temp_status = "the temperature have gotten dangerous, please take a break"
    else:
        temp_status = "✅"
    return temp_status
while True:
    temps = psutil.sensors_temperatures()
    print(f"current NVMe SSD temperature: {temps['nvme'][0].current}")
    temp_check1 = temp_check(temps['nvme'][0].current, critical_NVMeSSD, high_NVMeSSD)
    
    print(f"current NVMe Controller temperature: {temps['nvme'][1].current}")
    temp_check2 = temp_check(temps['nvme'][1].current, critical_NVMecontroller, high_NVMecontroller)

    print(f"current CPU temperature: {temps['k10temp'][0].current}")
    temp_check3 = temp_check(temps['k10temp'][0].current, critical_CPU, high_CPU)

    print(f"current iGPU temperature: {temps['amdgpu'][0].current}")
    temp_check4 = temp_check(temps['amdgpu'][0].current, critical_iGPU, high_iGPU) #как поставить условие переменная равно high или critical 
    temp_check_set =  { "NVMe SSD": temp_check1,
                        "NVMe controller": temp_check2, 
                        "CPU": temp_check3,
                        "GPU": temp_check4 }
    all_ok = True
    for name, status in temp_check_set.items():
        if status != "✅":
            print(f"there's a problem in {name}, {status}")
            all_ok = False
    if all_ok:
        print("✅")
    sleep(1)
    os.system("clear")