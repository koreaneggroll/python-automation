from datetime import datetime
import time
import os



while True:
    time_sleep = 3600 #one hour in seconds
    now = datetime.now()

    current_time = now.strftime("%H")
    int_current_time = int(current_time)

    if int_current_time < 12:
        print("Switching to ")
        os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/arin/python-automation-wallpapers/light-theme.jpg")


    elif int_current_time > 12:
        print("Switching to dark mode")
        os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/arin/python-automation-wallpapers/dark-theme.jpg")

    time.sleep(time_sleep)