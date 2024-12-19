WiFi Password Retriever (Windows)

This Python script retrieves a list of WiFi profiles stored on a Windows system and attempts to retrieve their passwords.


Disclaimer.

This script should only be used on devices you have proper authorization to access. Unauthorized access to Wi-Fi networks is illegal and unethical.
This script is provided for educational and legitimate administrative purposes only. The author is not responsible for any misuse of this script.


Features.

Retrieves a list of all WiFi profiles.
Attempts to extract the password for each profile.
Saves detailed information of profiles with unavailable passwords to a file for further investigation.
Displays results in a user-friendly format on the console.
Optionally saves the results to a file for record-keeping.


Requirements.

Python 3: Ensure Python 3 is installed on your system.
Administrative Privileges: This script requires elevated privileges to interact with the system's network settings.


Installation & Usage.

Save the script: Save the provided Python code as wifi_password_retriever.py.
Open a terminal: Launch a command prompt or terminal with administrator rights.
Navigate to the script's location: Use the cd command to navigate to the directory where you saved the script.
Run the script: Execute the script by typing python wifi_password_retriever.py and pressing Enter.


Output.

The script will display a table of WiFi profiles and their corresponding passwords (if found).
A file named "details.txt" will be created, containing detailed information about profiles for which passwords could not be retrieved.


Optional: Saving Results.

To save the retrieved information (profiles and passwords) to a file named "wifi_passwords.txt", uncomment the save_results_to_file(results) line within the main function of the script.


Note.

The success of password retrieval depends on the security settings of the respective WiFi networks.
This script may not be able to retrieve passwords for all profiles due to various reasons, including strong security measures or system limitations.
Contributing.

Contributions and improvements are welcome. Please feel free to fork this repository and submit pull requests.
