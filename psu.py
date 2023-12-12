#!/usr/bin/env python3
# Script:                       Create a Python script that fetches this information using Psuti
# Author:                       Yue Moua
# Date of latest revision:      12/11/2023
# Purpose:                      Ops Challeneg: Psutil

import psutil

# 
import psutil
import time

def get_cpu_times():
    cpu_times = psutil.cpu_times(percpu=False)
    
    user_mode_time = cpu_times.user
    kernel_mode_time = cpu_times.system
    idle_time = cpu_times.idle
    priority_user_mode_time = cpu_times.nice
    io_wait_time = cpu_times.iowait
    hardware_interrupt_time = cpu_times.irq
    software_interrupt_time = cpu_times.softirq
    virtualized_time = cpu_times.steal
    guest_time = cpu_times.guest

    return {
        'User Mode Time': user_mode_time,
        'Kernel Mode Time': kernel_mode_time,
        'Idle Time': idle_time,
        'Priority User Mode Time': priority_user_mode_time,
        'IO Wait Time': io_wait_time,
        'Hardware Interrupt Time': hardware_interrupt_time,
        'Software Interrupt Time': software_interrupt_time,
        'Virtualized Time': virtualized_time,
        'Guest Time': guest_time
    }

if __name__ == "__main__":
    cpu_info = get_cpu_times()

    for key, value in cpu_info.items():
        print(f"{key}: {value} seconds")

# https://psutil.readthedocs.io/en/latest/
# https://www.geeksforgeeks.org/psutil-module-in-python/
# https://chat.openai.com/c/0fb03b60-3a4e-4efa-9403-a18f6ec29d7c