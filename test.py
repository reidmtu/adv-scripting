import psutil
import PySimpleGUI as GUI

# Outside the while loop to use print statement
#  disk_io_counters = psutil.disk_io_counters()
#  print(disk_io_counters)
#  network = psutil.net_if_addrs()
#  print(tcp_networks)
#  network_pernic = psutil.net_io_counters(pernic=True)
#  print(network_pernic)

layout = [[GUI.Text('CPU Usage:'), GUI.Text('', size=(20, 1), key='-cpu_usage-')],
          [GUI.Text('Total CPU Cores:'), GUI.Text('', size=(20, 1), key='-total_cpu-')],
          [GUI.Text('CPU Cores:'), GUI.Text('', size=(20, 1), key='-cpu_cores-')],
          [GUI.Text('Partition Info:'), GUI.Text('', size=(80, 1), key='-partition_info-')],
          [GUI.Text('Disk Usage:'), GUI.Text('', size=(80, 1), key='-disk_usage-')],
          [GUI.Text('Username:'), GUI.Text('', size=(45, 1), key='-user_info-')],
          [GUI.Text('RAM Info:'), GUI.Text('', size=(80, 1), key='-ram_info-')],
          [GUI.Text('RAM Usage:'), GUI.Text('', size=(20, 1), key='-ram_usage-')]], \
         [GUI.Button('Exit')]

window = GUI.Window('System Monitor', layout,size=(725, 250))  #size=(725, 200) makes the window big to allow the 'ram_info'

while True:
    event, values = window.read(timeout=200)

    if event == GUI.WINDOW_CLOSED or event == 'Exit':
        break
    # device information that changes
    cpu_usage = psutil.cpu_percent()  # cpu usage as a percentage
    ram_usage = psutil.virtual_memory().percent  # ram usage as a percentage
    # device information that does not change
    total_cpu = psutil.cpu_count()  # cpu core of cores including logical cores
    cpu_cores = psutil.cpu_count(logical=False)  # cpu cores only
    ram_info = psutil.virtual_memory()  # the amount of memory in the system
    user_info = psutil.users()
    partition_info = psutil.disk_partitions()  # gets information on the disk partitions of the system
    disk_usage = psutil.disk_usage('/' or "C:")  # "C:" for Windows, '/' for Linux

    # information is updated and sent to the GUI window
    window['-cpu_usage-'].update(f'{cpu_usage}%')
    window['-total_cpu-'].update(f'{total_cpu}')
    window['-cpu_cores-'].update(f'{cpu_cores}')
    window['-partition_info-'].update(f'{partition_info}')
    window['-disk_usage-'].update(f'{disk_usage}')
    window['-ram_usage-'].update(f'{ram_usage}%')
    window['-ram_info-'].update(f'{ram_info}')
    window['-user_info-'].update(f'{user_info}')

window.close()
