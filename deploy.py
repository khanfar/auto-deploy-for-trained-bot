import subprocess
import time
import pyautogui
import os

# Define the commands and delays
commands = [
    "huggingface-cli login",
    "gradio deploy"
]

# Delay times in seconds
delays = [5, 5]

# Read the deployment directory from the text file
with open("deploy_directory.txt", "r") as file:
    deploy_directory = file.read().strip()

# Function to run the commands in the terminal and handle input prompts
def run_commands_with_input(commands, delays):
    for command, delay in zip(commands, delays):
        if command.startswith("echo "):
            subprocess.run(command, shell=True, text=True)
        else:
            subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            if "Token:" in command:
                print("Please enter the token manually when prompted.")
                input("Press Enter to continue after providing the token...")
            else:
                print(f"Executing command: {command}")
            time.sleep(delay)  # Pause for the specified delay

# Function to check if the deployment folder exists
def check_deploy_folder(directory):
    if not os.path.exists(directory):
        print(f"Error: The deployment folder '{directory}' does not exist.")
        return False
    print(f"Deployment folder location is correct: '{directory}'")
    return True

# Change the current working directory to the deployment folder
if check_deploy_folder(deploy_directory):
    os.chdir(deploy_directory)
    # Run the commands with input handling and logging
    run_commands_with_input(commands, delays)
