import re
from collections import defaultdict

# -----------------------------
# Configuration
# -----------------------------
LOG_FILE = "sample_auth.log"
SUSPICIOUS_THRESHOLD = 3

# Dictionary to track failed login attempts
failed_attempts = defaultdict(int)

# Regex patterns
ip_pattern = r'(\d+\.\d+\.\d+\.\d+)'
user_pattern = r'user\s+(\w+)'
time_pattern = r'^(\w+\s+\d+\s+\d+:\d+:\d+)'

print("\n========== LOG ANALYZER ==========\n")

try:
    with open(LOG_FILE, "r") as file:
        logs = file.readlines()

    print("[+] Reading log file...\n")

    for line in logs:

        # Detect failed login attempts
        if "Failed password" in line or "authentication failure" in line:

            # Extract timestamp
            timestamp_match = re.search(time_pattern, line)
            timestamp = (
                timestamp_match.group(1)
                if timestamp_match
                else "Unknown Time"
            )

            # Extract IP address
            ip_match = re.search(ip_pattern, line)
            ip_address = (
                ip_match.group(1)
                if ip_match
                else "Unknown IP"
            )

            # Extract username
            user_match = re.search(user_pattern, line)
            username = (
                user_match.group(1)
                if user_match
                else "Unknown User"
            )

            failed_attempts[ip_address] += 1

            print("FAILED LOGIN DETECTED")
            print(f"Time: {timestamp}")
            print(f"IP Address: {ip_address}")
            print(f"Username: {username}")
            print("-" * 40)

    # -----------------------------
    # Suspicious Activity Report
    # -----------------------------
    print("\n========== INCIDENT REPORT ==========\n")

    suspicious_found = False

    for ip, count in failed_attempts.items():
        if count >= SUSPICIOUS_THRESHOLD:
            suspicious_found = True

            print("⚠️ SUSPICIOUS ACTIVITY DETECTED")
            print(f"IP Address: {ip}")
            print(f"Failed Login Attempts: {count}")
            print("Possible brute-force activity")
            print("-" * 40)

    if not suspicious_found:
        print("No suspicious login activity detected.")

except FileNotFoundError:
    print(f"[ERROR] Log file '{LOG_FILE}' not found.")
except Exception as e:
    print(f"[ERROR] Something went wrong: {e}")
