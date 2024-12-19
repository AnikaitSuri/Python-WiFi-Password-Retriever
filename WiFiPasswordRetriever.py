import subprocess

def get_wifi_profiles():
    """Retrieve a list of WiFi profiles stored on the system."""
    try:
        data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
        profiles = [line.split(":")[1][1:-1] for line in data if "All User Profile" in line]
        return profiles
    except subprocess.CalledProcessError:
        print("Failed to retrieve WiFi profiles. Make sure you have administrative privileges.")
        return []

def get_wifi_password(profile, details_file):
    """Retrieve the password for a given WiFi profile."""
    try:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
        password = [line.split(":")[1][1:-1] for line in results if "Key Content" in line]
        if not password:
            with open(details_file, "a") as file:
                file.write(f"\nDetails for profile: {profile}\n")
                file.write("\n".join(results))
                file.write("\n" + "-" * 50 + "\n")
            print(f"No password found for profile: {profile}. Details appended to {details_file}")
        return password[0] if password else None
    except subprocess.CalledProcessError:
        print(f"Failed to retrieve details for profile: {profile}")
        return None

def save_results_to_file(results, filename="wifi_passwords.txt"):
    """Save the WiFi profiles and passwords to a file."""
    try:
        with open(filename, "w") as file:
            file.write("{:<30}|  {:<}\n".format("WiFi Network", "Password"))
            file.write("-" * 50 + "\n")
            for profile, password in results:
                file.write("{:<30}|  {:<}\n".format(profile, password if password else ""))
        print(f"Results saved to {filename}")
    except IOError as e:
        print(f"Failed to save results to file: {e}")

def main():
    print("{:<30}|  {:<}".format("WiFi Network", "Password"))
    print("-" * 50)
    profiles = get_wifi_profiles()
    results = []
    details_file = "wifi_details.txt"

    with open(details_file, "w") as file:
        file.write("WiFi Profile Details\n")
        file.write("=" * 50 + "\n")

    for profile in profiles:
        password = get_wifi_password(profile, details_file)
        results.append((profile, password))
        print("{:<30}|  {:<}".format(profile, password if password else ""))

    # Optionally save results to a file
    save_results_to_file(results)

if __name__ == "__main__":
    main()
