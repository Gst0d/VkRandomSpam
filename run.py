import time
import subprocess
print('Погнали нахуй')
while True:
    subprocess.Popen("bot.py 1", shell=True) #Открывает bot.py
    time.sleep(10) #Отсчет в секундах
