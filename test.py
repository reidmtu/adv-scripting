import psutil
import PySimpleGUI as GUI

layout = [[GUI.Text('CPU Usage:'), GUI.Text('', size=(20, 1), key='-cpu_usage-')],
          [GUI.Text('Total CPU Cores:'), GUI.Text('', size=(20, 1), key='-total_cpu-')],
          [GUI.Text('CPU Cores:'), GUI.Text('', size=(20, 1), key='-cpu_cores-')],
          [GUI.Text('Partition Info:'), GUI.Text('', size=(80, 1), key='-partition_info-')],
          [GUI.Text('Disk Usage:'), GUI.Text('', size=(80, 1), key='-disk_usage-')],
          [GUI.Text('Username:'), GUI.Text('', size=(45, 1), key='-user_info-')],
          [GUI.Text('RAM Info:'), GUI.Text('', size=(80, 1), key='-ram_info-')],
          [GUI.Text('RAM Usage:'), GUI.Text('', size=(20, 1), key='-ram_usage-')]], \
         [GUI.Button('Exit')]

window = GUI.Window('System Monitor', layout, size=(725, 250))

while True:
    event, values = window.read(timeout=200)

    if event == GUI.WINDOW_CLOSED or event == 'Exit':
        break
    cpu_usage = psutil.cpu_percent()
    ram_usage = psutil.virtual_memory().percent
    total_cpu = psutil.cpu_count()
    cpu_cores = psutil.cpu_count(logical=False)
    ram_info = psutil.virtual_memory()
    user_info = psutil.users()
    partition_info = psutil.disk_partitions()
    disk_usage = psutil.disk_usage('/' or "C:")

    window['-cpu_usage-'].update(f'{cpu_usage}%')
    window['-total_cpu-'].update(f'{total_cpu}')
    window['-cpu_cores-'].update(f'{cpu_cores}')
    window['-partition_info-'].update(f'{partition_info}')
    window['-disk_usage-'].update(f'{disk_usage}')
    window['-ram_usage-'].update(f'{ram_usage}%')
    window['-ram_info-'].update(f'{ram_info}')
    window['-user_info-'].update(f'{user_info}')

window.close()
