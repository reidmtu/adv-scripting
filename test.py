import psutil
import glances
#import PySimpleGUI as GUI


cpu_times = psutil.cpu_times()
print(cpu_times)

cpu_satus = psutil.cpu_stats()
print(cpu_satus)

cpu_freq = psutil.cpu_freq()
print(cpu_freq)

total_cpu = psutil.cpu_count()
print(total_cpu)

cpu_cores = psutil.cpu_count(logical=False)
print(cpu_cores)

ram_info = psutil.virtual_memory()
print(ram_info)

disk_info = psutil.disk_io_counters()
print(disk_info)


#GUI.Window(title="Test window", layout=[[]], margins=(200, 60)).read()