import os

def sleep_system():
    # Using rundll32.exe to set the system into sleep mode
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

sleep_system()