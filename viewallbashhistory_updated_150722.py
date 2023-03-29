import os
#https://stackoverflow.com/questions/38489755/python-script-to-type-something-in-terminal
os.system("gnome-terminal -- bash -c \"cat ~/.bash_history; exec bash\"")
