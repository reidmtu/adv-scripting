import psutil
import PySimpleGUI as GUI
#testing commit
#testing
# Outside the while loop to use print statements
#cpu_usage = psutil.cpu_percent()  # cpu usage as a percentage
# print(cpu_usage)
#total_cpu = psutil.cpu_count()  # cpu core of cores including logical cores
# print(total_cpu)
#cpu_cores = psutil.cpu_count(logical=False)  # cpu cores only
# print(cpu_cores)
#cpu_freq = psutil.cpu_freq()
#print(cpu_freq)
#ram_info = psutil.virtual_memory()  # the amount of memory in the system
#print(ram_info)
#ram_usage = psutil.virtual_memory().percent  # ram usage as a percentage
# print(ram_usage)
#partition_info = psutil.disk_partitions()
#print(partition_info)
#disk_usage = psutil.disk_usage('/' or "C:") # "C:" for Windows, '/' for Linux
#print(disk_usage)
#disk_io_counters = psutil.disk_io_counters()
#print(disk_io_counters)
#network = psutil.net_if_addrs()
# print(network)
# tcp_networks = psutil.net_connections()# (kind='tcp')
#print(tcp_networks)
#user_info = psutil.users()
#print(user_info)
# network_pernic = psutil.net_io_counters(pernic=True)
#print(network_pernic)

layout = [[GUI.Text('CPU Usage:'), GUI.Text('', size=(20, 1), key='-cpu_usage-')],
          [GUI.Text('Total CPU Cores:'), GUI.Text('', size=(20, 1), key='-total_cpu-')],
          [GUI.Text('CPU Cores:'), GUI.Text('', size=(20, 1), key='-cpu_cores-')],
          [GUI.Text('RAM Info:'), GUI.Text('', size=(80, 1), key='-ram_info-')],
          [GUI.Text('RAM Usage:'), GUI.Text('', size=(20, 1), key='-ram_usage-')]], \
         [GUI.Button('Exit')]

window = GUI.Window('System Monitor', layout,size=(725, 200)) #size=(725, 200) makes the window big to allow the 'ram_info'

while True:
    event, values = window.read(timeout=250)

    if event == GUI.WINDOW_CLOSED or event == 'Exit':
        break
    # device information that changes
    cpu_usage = psutil.cpu_percent()  # cpu usage as a percentage
    ram_usage = psutil.virtual_memory().percent  # ram usage as a percentage
    # device information that does not change
    total_cpu = psutil.cpu_count()  # cpu core of cores including logical cores
    cpu_cores = psutil.cpu_count(logical=False)  # cpu cores only
    ram_info = psutil.virtual_memory()  # the amount of memory in the system

    # information is updated and sent to the GUI window
    window['-cpu_usage-'].update(f'{cpu_usage}%')
    window['-total_cpu-'].update(f'{total_cpu}')
    window['-cpu_cores-'].update(f'{cpu_cores}')
    window['-ram_usage-'].update(f'{ram_usage}%')
    window['-ram_info-'].update(f'{ram_info}')

window.close()
