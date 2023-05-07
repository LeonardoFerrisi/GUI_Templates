# Start up the entire application
import subprocess
import os
import time

current_path = os.path.dirname(os.path.realpath(__file__))
print(current_path)

# Start up the server

print("\nStarting up Python Backend Server\n")

server_path = os.path.join(current_path, "server_python", "server.py")

venv_activate = os.path.join(current_path, "server_python", ".venv", "Scripts","activate.bat")
command = f"{venv_activate} && python {server_path}"
# res = subprocess.Popen(command, shell=False, creationflags=subprocess.CREATE_NEW_CONSOLE)
fullCommand = f'start "" /B cmd /k "{command}"'
os.system(fullCommand)


#############################################
time.sleep(1)
print("\nStarting up React Frontend Server\n")


frontend_path = os.path.join(current_path, "client")
# callString_A = f"cd {frontend_path} && npm start"
# command = f'start "" /B cmd "{callString_A}"'
# os.system(command)

callString_A = f"cd {frontend_path} && npm start"
command = f'start "" /B cmd /k "{callString_A}"'   # /k keeps the window open, /B doesn't open a new window
os.system(command)



#############################################
time.sleep(1)
print("\nStarting up Python Socket Listener Sample\n")
listener_path = os.path.join(current_path, "server_python", "listener.py")
venv_activate = os.path.join(current_path, "server_python", ".venv", "Scripts","activate.bat")
command = f"{venv_activate} && python {listener_path}"
res = subprocess.run(command, shell=False, creationflags=subprocess.CREATE_NEW_CONSOLE)
print(f"Subprocess returned: {res}\n")


