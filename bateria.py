import psutil

battery = psutil.sensors_battery()

percent = str(battery.percent)

display(f'No momento você tem {percent}% de bateria!')