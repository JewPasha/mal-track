import psutil
import os
import re
import winreg as reg
def get_program_info(program_names):
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        try:
            if proc.info['name'].lower() in (f'{name.lower()}.exe' for name in program_names):
                return proc.info['name'], proc.info['exe']
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            print('Error reading process data')
    return None, None
def display_malware_ip(file_path):
    try:
        with open(file_path, 'r', errors='ignore') as file:
            data = file.read()
            ip_pattern = re.compile(r'\b(?:(?:[1-9][0-9]{0,2}|0)\.(?:[0-9]{1,3})\.(?:[0-9]{1,3})\.(?:[1-9][0-9]{0,2}))\b')
            ips = ip_pattern.findall(data)
            if ips:
                ip = next(iter(set(ips)))
                print(f"IP addresses associated to the malware: {ip}")
                return
            print("No IP addresses found.")
    except Exception as e:
        print(f"Error retrieving network connections: {e}")
def terminate_malware(process_name):
    try:      
        for proc in psutil.process_iter(['name', 'pid']):
            if proc.info['name'].lower() == process_name.lower():
                print(f"Terminating process {process_name} (PID: {proc.info['pid']})")
                proc.terminate()
                proc.wait()
                print(f"{process_name} terminated.")
    except:
        print(f"Error terminating {process_name}")
def remove_from_startup(key_names):
    reg_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    try:
        with reg.OpenKey(reg.HKEY_CURRENT_USER, reg_path, 0, reg.KEY_WRITE | reg.KEY_READ) as key:
            i = 0
            while True:
                try:
                    program_name, _, _ = reg.EnumValue(key, i)
                    if program_name.lower() in (name for name in key_names):
                        reg.DeleteValue(key, program_name)
                        print(f"Removed {program_name} from Windows startup.\n")
                    i += 1
                except OSError as e:
                    break
    except FileNotFoundError:
        print(f"Malware not found in Windows startup.")
    except Exception as e:
        print(f"Error removing malware from startup: {e}")
def delete_malware_file(file_path):
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Malware file {file_path} deleted.")
        else:
            print(f"Malware file {file_path} not found.")
    except Exception as e:
        print(f"Error deleting malware file: {e}")
def cleanup_malware(process_name, startup_names, file_path, process_file_path):
    display_malware_ip(file_path)
    terminate_malware(process_name)
    remove_from_startup(startup_names)
    delete_malware_file(process_file_path)
    if process_file_path != file_path:
        delete_malware_file(file_path)
file_names = ['maltrack', 'mal-track']
file_path = r'C:\Users\user\Desktop\mal-track\mal-track.exe'
process_name, process_file_path = get_program_info(file_names)
if process_file_path:
    cleanup_malware(process_name, file_names, file_path, process_file_path)
else:
    print('Malware not found')
