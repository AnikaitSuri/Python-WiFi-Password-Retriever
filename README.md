# Python-WiFi-Password-Retriever

WiFi Password Retriever (Windows)

This Python script retrieves a list of WiFi profiles stored on a Windows system and attempts to retrieve their passwords.

Important Note:
This script requires administrative privileges to run.
Retrieving WiFi passwords without permission is illegal. This script is intended for educational purposes only and should be used on authorized devices.

Features:
Lists all WiFi profiles on the system.
Attempts to retrieve the password for each profile.
Saves details of profiles for which passwords couldn't be retrieved for further analysis (optional).
Outputs results to the console and optionally saves them to a file.

Requirements:
Python 3
Administrative privileges on the target system

Installation:
Save the script as wifi_password_retriever.py.
Open a command prompt or terminal and navigate to the directory where you saved the script.
Run the script with python wifi_password_retriever.py.

Usage:
The script will automatically retrieve and display WiFi profiles and passwords. It will also create a file named "details.txt" to store details of profiles where passwords couldn't be retrieved.

Optional:
The script can save the results to a file named "wifi_passwords.txt". This functionality is currently commented out (# Optionally save results to a file). You can uncomment the save_results_to_file(results) line in the main function to enable it.

Disclaimer:
This script is provided for educational purposes only. The author is not responsible for any misuse of this script.
