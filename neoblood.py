import os
import zipfile
import subprocess
import time

# Function to check Neo4j status
def is_neo4j_running():
    try:
        subprocess.run("sudo neo4j status", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except subprocess.CalledProcessError:
        return False

# Prompt for Neo4j credentials
neo4j_password = input("\nEnter your Neo4j password: ")

# Check if Neo4j is already running
if not is_neo4j_running():
    # Start Neo4j
    start_neo4j_cmd = "sudo neo4j start"
    subprocess.run(start_neo4j_cmd, shell=True, check=True)

    # Open the browser
    open_browser_cmd = "xdg-open http://localhost:7474 2>/dev/null"  # Adjust for your operating system
    subprocess.run(open_browser_cmd, shell=True, check=True)
    print("\n\nOpening browser... You may need to refresh the page.")
    time.sleep(5)
else:
    # Open the browser
    open_browser_cmd = "xdg-open http://localhost:7474 2>/dev/null"  # Adjust for your operating system
    subprocess.run(open_browser_cmd, shell=True, check=True)
    print("\n\nOpening browser... You may need to refresh the page.")
    time.sleep(5)
    
# Prompt for BloodHound credentials and target information
domain = input("\n\nEnter the domain: ")
domain_user = input("\nEnter the domain user: ")
password = input("\nEnter the password: ")
target_ip = input("\nEnter the target IP: ")

# Run BloodHound-Python Ingestor
bloodhound_cmd = f"bloodhound-python -d {domain} -u {domain_user} -p {password} -c all -ns {target_ip}"
subprocess.run(bloodhound_cmd, shell=True, check=True)

# Zip up .json files in the working directory
json_files = [f for f in os.listdir() if f.endswith(".json")]
if json_files:
    zip_name = f"{domain}bloodhound.zip"
    with zipfile.ZipFile(zip_name, 'w') as zip_file:
        for json_file in json_files:
            zip_file.write(json_file)
            os.remove(json_file)  # Remove each .json file after zipping
    print(f'\n\nSuccessfully zipped and removed {len(json_files)} .json files into {zip_name}.')
else:
    print('\n\nNo .json files found in the working directory.\n\n')
    
# Open BloodHound
subprocess.run("bloodhound", shell=True, check=True)


