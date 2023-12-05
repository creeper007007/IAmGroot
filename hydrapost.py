import tkinter as tk
from tkinter import ttk
import subprocess
import threading

# GUI setup
root = tk.Tk()
root.title("Hydrate those Lips")  # Updated header
# Global variable to store the subprocess object
hydra_process = None
stop_event = threading.Event()  # Event to signal the thread to stop

def run_hydra_command():
    global hydra_process
    try:
        rhost = rhost_entry.get()
        rport = rport_entry.get() or "80"  # Default to 80 if no input is provided
        login_path = login_path_entry.get()
        username_param = username_param_entry.get()
        password_param = password_param_entry.get()
        failed_login_message = failed_login_message_entry.get()

        hydra_command = f"hydra -v -L {userlist_entry.get() or '/usr/share/wordlists/seclists/Usernames/top-usernames-shortlist.txt'} -P {passwordlist_entry.get() or '/usr/share/wordlists/seclists/Passwords/Default-Credentials/default-passwords.txt'} {rhost} -s {rport} http-post-form \"{login_path}:{username_param}=^USER^&{password_param}=^PASS^:{failed_login_message}\""

        hydra_command_text.delete(1.0, tk.END)  # Clear previous text
        hydra_command_text.insert(tk.END, hydra_command)

        # Run the Hydra command in the terminal
        hydra_process = subprocess.Popen(hydra_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)

        # Capture and print the output of the command
        while hydra_process.poll() is None and not stop_event.is_set():
            line = hydra_process.stdout.readline()
            if line:
                print(line.strip())
    finally:
        # Ensure hydra_process is set to None when the thread exits
        hydra_process = None

def hydrate_command():
    global hydra_process
    global stop_event
    stop_event.clear()  # Clear the event before starting a new thread
    threading.Thread(target=run_hydra_command).start()

def cancel_command():
    global hydra_process
    global stop_event
    if hydra_process and hydra_process.poll() is None:
        # Kill the Hydra command in the terminal
        hydra_process.terminate()
        hydra_process.wait()  # Wait for the process to complete
        print("Hydra command cancelled.")
    stop_event.set()  # Set the event to stop the thread

# Generate Button
generate_button = ttk.Button(root, text="Hydrate", command=hydrate_command)
generate_button.grid(row=9, column=0, pady=10)

# Cancel Button
cancel_button = ttk.Button(root, text="Cancel", command=cancel_command)
cancel_button.grid(row=9, column=1, pady=10)

# Result Text
hydra_command_text = tk.Text(root, height=5, width=60, wrap=tk.WORD)
hydra_command_text.grid(row=10, column=0, columnspan=2, pady=10)

# Configure style
style = ttk.Style()
# ... (style configurations remain unchanged)


# Configure style
style = ttk.Style()
style.configure("TFrame", background="#1a1a1a")  # Dark background color
style.configure("TLabel", foreground="#66ff66", background="#1a1a1a")  # Light green text color
style.configure("TEntry", fieldbackground="#333333", foreground="#66ff66", insertbackground="#66ff66")  # Dark background, light green text, and green cursor color
style.configure("TButton", foreground="#66ff66", background="#333333")  # Light green text on dark background
style.configure("TText", background="#333333", foreground="#66ff66")  # Dark background and light green text color

# Labels and Entries
tk.Label(root, text="Target Host (rhost):").grid(row=0, column=0, sticky="w")
rhost_entry = ttk.Entry(root)
rhost_entry.grid(row=0, column=1)

tk.Label(root, text="Target Port (rport):").grid(row=1, column=0, sticky="w")
rport_entry = ttk.Entry(root)
rport_entry.grid(row=1, column=1)

tk.Label(root, text="Login Path (login_path):").grid(row=2, column=0, sticky="w")
login_path_entry = ttk.Entry(root)
login_path_entry.grid(row=2, column=1)

tk.Label(root, text="Username Parameter:").grid(row=3, column=0, sticky="w")
username_param_entry = ttk.Entry(root)
username_param_entry.grid(row=3, column=1)

tk.Label(root, text="Password Parameter:").grid(row=4, column=0, sticky="w")
password_param_entry = ttk.Entry(root)
password_param_entry.grid(row=4, column=1)

tk.Label(root, text="Failed Login Message:").grid(row=5, column=0, sticky="w")
failed_login_message_entry = ttk.Entry(root)
failed_login_message_entry.grid(row=5, column=1)

tk.Label(root, text="Custom User List:").grid(row=6, column=0, sticky="w")
userlist_entry = ttk.Entry(root)
userlist_entry.grid(row=6, column=1)

tk.Label(root, text="Custom Password List:").grid(row=7, column=0, sticky="w")
passwordlist_entry = ttk.Entry(root)
passwordlist_entry.grid(row=7, column=1)

# Set default value for rport to 80
rport_entry.insert(0, "80")

# Message for leaving fields blank
message_label = tk.Label(root, text="Leave form fields blank to proceed with defaults", font=("Arial", 10, "italic"), foreground="#66ff66", background="#1a1a1a")
message_label.grid(row=8, column=0, columnspan=2, pady=5)

# Result Text
hydra_command_text = tk.Text(root, height=5, width=60, wrap=tk.WORD)
hydra_command_text.grid(row=10, column=0, columnspan=2, pady=10)

root.mainloop()
