import os
import subprocess
import shutil
import ctypes

def set_power_settings():
    """
    Set power settings to high performance.
    """
    try:
        subprocess.run(["powercfg", "-setactive", "SCHEME_MIN"], check=True)
        print("Set power settings to high performance.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to set power settings: {e}")

def disk_cleanup():
    """
    Run disk cleanup.
    """
    try:
        subprocess.run(["cleanmgr", "/sagerun:1"], check=True)
        print("Disk cleanup executed.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run disk cleanup: {e}")

def defragment_disk():
    """
    Run disk defragmentation.
    """
    try:
        subprocess.run(["defrag", "C:", "/O"], check=True)
        print("Disk defragmentation executed.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to run disk defragmentation: {e}")

def disable_scheduled_tasks():
    """
    Disable unnecessary scheduled tasks.
    """
    tasks_to_disable = [
        "Microsoft\\Windows\\Application Experience\\Microsoft Compatibility Appraiser",
        "Microsoft\\Windows\\Customer Experience Improvement Program\\Consolidator",
        "Microsoft\\Windows\\DiskDiagnostic\\Microsoft-Windows-DiskDiagnosticDataCollector",
        "Microsoft\\Windows\\Maintenance\\WinSAT"
    ]
    for task in tasks_to_disable:
        try:
            subprocess.run(["schtasks", "/Change", "/TN", task, "/Disable"], check=True)
            print(f"Disabled scheduled task: {task}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to disable scheduled task {task}: {e}")

def disable_visual_effects():
    """
    Disable unnecessary visual effects.
    """
    reg_commands = [
        r'reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer\VisualEffects" /v "VisualFXSetting" /t REG_DWORD /d "2" /f',
        r'reg add "HKCU\Control Panel\Desktop" /v "DragFullWindows" /t REG_SZ /d "0" /f',
        r'reg add "HKCU\Control Panel\Desktop\WindowMetrics" /v "MinAnimate" /t REG_SZ /d "0" /f',
        r'reg add "HKCU\Software\Microsoft\Windows\DWM" /v "Animations" /t REG_DWORD /d "0" /f',
        r'reg add "HKCU\Software\Microsoft\Windows\DWM" /v "EnableAeroPeek" /t REG_DWORD /d "0" /f',
        r'reg add "HKCU\Software\Microsoft\Windows\DWM" /v "EnableBlurBehind" /t REG_DWORD /d "0" /f'
    ]
    for command in reg_commands:
        try:
            subprocess.run(command, shell=True, check=True)
            print(f"Executed registry command: {command}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to execute registry command {command}: {e}")

def disable_background_services():
    """
    Disable or set to manual non-essential background services.
    """
    services_to_disable = [
        "wuauserv",  # Windows Update
        "bits",      # Background Intelligent Transfer Service (BITS)
        "wsearch",   # Windows Search (Indexing Service)
        "SysMain",   # Superfetch (SysMain)
        "Spooler"    # Print Spooler
    ]
    for service in services_to_disable:
        try:
            subprocess.run(["sc", "config", service, "start= disabled"], check=True)
            print(f"Disabled service: {service}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to disable service {service}: {e}")

def make_system_fast_and_secure():
    """
    Execute all optimization functions.
    """
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("This script must be run as administrator.")
        return

    set_power_settings()
    disk_cleanup()
    defragment_disk()
    disable_scheduled_tasks()
    disable_visual_effects()
    disable_background_services()
    print("System optimization completed.")

if __name__ == "__main__":
    make_system_fast_and_secure()
