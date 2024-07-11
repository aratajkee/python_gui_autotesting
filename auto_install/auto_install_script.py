import pyautogui
import subprocess

install_script = "install_script.sh"

try:
    subprocess.run(['gnome-terminal', '--', 'bash', '-c', install_script], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error while running the script: {e}")

# Enter login and pass


simulation_script = "simulation.sh"

try:
    subprocess.run(['gnome-terminal', '--', 'bash', '-c', simulation_script], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error while running the script: {e}")