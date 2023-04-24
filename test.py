import psutil
import PySimpleGUI as GUI

# Outside the while loop to use print statements
cpu_usage = psutil.cpu_percent()  # cpu usage as a percentage
# print(cpu_usage)
total_cpu = psutil.cpu_count()  # cpu core of cores including logical cores
# print(total_cpu)
cpu_cores = psutil.cpu_count(logical=False)  # cpu cores only
# print(cpu_cores)
ram_info = psutil.virtual_memory()  # the amount of memory in the system
# print(ram_info)
ram_usage = psutil.virtual_memory().percent  # ram usage as a percentage
# print(ram_usage)

layout = [[GUI.Text('CPU Usage:'), GUI.Text('', size=(20, 1), key='-cpu_usage-')],
          [GUI.Text('Memory Usage:'), GUI.Text('', size=(20, 1), key='-ram_usage-')]],\
         [GUI.Button('Exit')]

window = GUI.Window('System Monitor', layout)

while True:
    event, values = window.read(timeout=600)

    if event == GUI.WINDOW_CLOSED or event == 'Exit':
        break
    # device information that changes
    cpu_usage = psutil.cpu_percent()  # cpu usage as a percentage
    ram_usage = psutil.virtual_memory().percent  # ram usage as a percentage
    # device information that does not change
    total_cpu = psutil.cpu_count()  # cpu core of cores including logical cores
    cpu_cores = psutil.cpu_count(logical=False)  # cpu cores only
    ram_info = psutil.virtual_memory()  # the amount of memory in the system

    # information is updated
    window['-cpu_usage-'].update(f'{cpu_usage}%')
    window['-ram_usage-'].update(f'{ram_usage}%')

window.close()
