import os
import webbrowser
import psutil  # For system monitoring

# Application Control
def open_chrome():
    webbrowser.open("https://www.google.com")

def open_calculator():
    os.system("calc")

def open_notepad():
    os.system("notepad")

# System Monitoring
def get_cpu_usage():
    return f"CPU Usage: {psutil.cpu_percent()}%"

def get_ram_usage():
    return f"RAM Usage: {psutil.virtual_memory().percent}%"

# Command Execution
def run_command(cmd):
    result = os.popen(cmd).read()
    return result
