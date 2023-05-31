import platform
import os
import time

# Define the list of websites to block
websites_to_block = ["example.com", "facebook.com", "youtube.com"]

# Determine the location of the hosts file based on the operating system
system = platform.system()
if system == "Windows":
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
elif system == "Linux" or system == "Darwin":
    hosts_path = "/etc/hosts"
else:
    print("Unsupported operating system.")
    exit()

# Function to block websites
def block_websites():
    try:
        with open(hosts_path, "a") as hosts_file:
            for website in websites_to_block:
                entry = "127.0.0.1 " + website + "\n"
                hosts_file.write(entry)
        print("Websites blocked successfully.")
    except IOError:
        print("Unable to block websites. Please run the script as an administrator or superuser.")

# Function to unblock websites
def unblock_websites():
    try:
        with open(hosts_path, "r+") as hosts_file:
            lines = hosts_file.readlines()
            hosts_file.seek(0)
            for line in lines:
                if not any(website in line for website in websites_to_block):
                    hosts_file.write(line)
            hosts_file.truncate()
        print("Websites unblocked successfully.")
    except IOError:
        print("Unable to unblock websites. Please run the script as an administrator or superuser.")

# Function to display blocked websites
def display_blocked_websites():
    print("Blocked websites:")
    for website in websites_to_block:
        print("- " + website)

# Function to add a website to the blocked list
def add_website():
    website = input("Enter the website to block: ")
    websites_to_block.append(website)
    print(website + " added to the blocked websites list.")

# Function to remove a website from the blocked list
def remove_website():
    website = input("Enter the website to unblock: ")
    if website in websites_to_block:
        websites_to_block.remove(website)
        print(website + " removed from the blocked websites list.")
    else:
        print(website + " is not in the blocked websites list.")

# Function to save blocked websites to a file
def save_blocked_websites():
    try:
        with open(blocked_websites_file, "w") as file:
            for website in websites_to_block:
                file.write(website + "\n")
        print("Blocked websites saved to file successfully.")
    except IOError:
        print("Unable to save blocked websites to file.")

# Function to load blocked websites from a file
def load_blocked_websites():
    if os.path.exists(blocked_websites_file):
        try:
            with open(blocked_websites_file, "r") as file:
                websites = file.read().splitlines()
            print("Blocked websites loaded from file successfully.")
            return websites
        except IOError:
            print("Unable to load blocked websites from file.")
    else:
        print("Blocked websites file does not exist.")

# Function to set a time-based schedule for blocking websites
def set_schedule():
    start_time = input("Enter the start time (HH:MM): ")
    end_time = input("Enter the end time (HH:MM): ")

    try:
        start = time.strptime(start_time, "%H:%M")
        end = time.strptime(end_time, "%H:%M")
        current_time = time.localtime()

        if start <= current_time <= end:
            block_websites()
            print("Websites blocked successfully.")
        else:
            unblock_websites()
            print("Websites unblocked successfully.")
    except ValueError:
        print("Invalid time format. Please use HH:MM format.")

# Function to view the current time-based schedule
def view_schedule():
    if start_time and end_time:
        print("Current time-based schedule:")
        print("Start Time: " + start_time)
        print("End Time: " + end_time)
    else:
        print("No time-based schedule is set.")

# Function to clear the time-based schedule
def clear_schedule():
    global start_time, end_time
    start_time = ""
    end_time = ""
    print("Time-based schedule cleared.")

# Prompt the user for action
print("Website Blocker")
print("1. Block websites")
print("2. Unblock websites")
print("3. Display blocked websites")
print("4. Add website to block")
print("5. Remove website from block")
print("6. Save blocked websites to file")
print("7. Load blocked websites from file")
print("8. Set time-based schedule")
print("9. View current schedule")
print("10. Clear time-based schedule")

choice = input("Enter your choice (1-10): ")

if choice == 1:
    block_websites()
elif choice == 2:
    unblock_websites()
elif choice == 3:
    display_blocked_websites()
elif choice == 4:
    add_website()
elif choice == 5:
    remove_website()
elif choice == 6:
    save_blocked_websites()
elif choice == 7:
    websites_to_block = load_blocked_websites() or websites_to_block
elif choice == 8:
    set_schedule()
elif choice == 9:
    view_schedule()
elif choice == 10:
    clear_schedule()
else:
    print("Invalid choice. Please select a valid option.")
