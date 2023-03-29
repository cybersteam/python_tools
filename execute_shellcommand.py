import os
#https://stackoverflow.com/questions/38489755/python-script-to-type-something-in-terminal
os.system("gnome-terminal -e 'bash -c \"scp -r /home/ict/Documents/Code root@ivann.mobi://var/www/backups/; exec bash\"'")
