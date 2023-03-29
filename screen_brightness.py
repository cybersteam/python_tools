os.system("gnome-terminal -e 'bash -c \"xrandr | grep <connected> | cut -f1 -d " ""'")
time.sleep(10)

os.system("gnome-terminal -e 'bash -c \"xrandr --output LVDS-1 --brightness 1.2"'")
