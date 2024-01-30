import os
from tqdm import tqdm
from time import sleep  # For demonstration purposes only

def get_user_input(prompt, default=""):
    user_input = input(prompt).strip()
    return user_input if user_input else default

def main():
    try:
        # Prompt for username
        username = get_user_input("Enter username (press Enter for anonymous): ", default="anonymous")
        
        # Prompt for password if username is not anonymous
        password = ""
        if username.lower() != "anonymous":
            password = get_user_input("Enter password: ")

        # Prompt for target IP, using $IP environment variable if skipped
        target_ip = os.getenv("IP") or get_user_input("Enter target IP: ")

        # Prompt for target port
        target_port = get_user_input("Enter target port: ")

        # Inform the user that files are being retrieved
        print("Downloading files from FTP server. Please wait.")
        
        # Construct and run the wget command
        wget_command = f"wget -m -q --user={username} --password={password} ftp://{target_ip}:{target_port}"
        

        
        # Use tqdm to create a progress bar
        for _ in tqdm(range(10), desc="Downloading", unit="files"):

            os.system(wget_command)

        # Run grep command with subprocess
        search_list = ["user", "login", "pass", "cred"]
        for term in search_list:
            grep_command = f"grep --color=always -r -i {term} ."
            try:
                # Use subprocess to capture and display the output
                os.system(grep_command)
                break  # Exit the loop if grep command succeeds
            except Exception as e:
                print(f"Error executing command: {e}")

        # Prompt the user if they want to search for additional terms
        additional_search = get_user_input("Do you want to search for additional terms? (Y/N): ")
        
        while additional_search.lower() == "y":
            search_terms = get_user_input("Enter additional search terms (comma separated): ").split(',')
            for term in search_terms:
                grep_command = f"grep -r -i {term.strip()} ."
                os.system(grep_command)

            additional_search = get_user_input("Do you want to search for additional terms? (Y/N): ")

        print("Program ended.")

if __name__ == "__main__":
    main()
