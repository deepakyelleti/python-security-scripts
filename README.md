# python-security-scripts
Python automation scripts for IT administration and cybersecurity tasks.

## Password Policy Audit Script
- Built a Python-based audit tool that evaluates Password Strength and returns a list of policy violations.
- I also used "getpass" which ensures that the password isn't visible on screen when a user types it in, preventing Shoulder Surfing.
- The script will check for:
     1. Length.
     2. Uppercase.
     3. Lowercase.
     4. Numerical Digit.
     5. Special Character.
 - Output:
   <img width="1099" height="464" alt="image" src="https://github.com/user-attachments/assets/3bff8566-4f24-4ade-a99b-aa2f1db1308d" />

## Log Analyzer
- Built a Python-based log analysis tool to identify Failed Authentication Attempts and detect Suspicious Login Behavior through Log Analysis and Incident Reporting. Please use a "sample_auth.log" file to verify.
- The script will:
     1. Read a Log File.
     2. Detect Failed Login Attempts.
     3. Extract: Timestamp, IP Address, Username (if available).
     4. Count Repeated Failed Logins.
     5. Flag Suspicious Activity (Multiple failures from same IP).
- Output:
  <img width="1096" height="846" alt="image" src="https://github.com/user-attachments/assets/a0b3d3c9-4b4c-4682-b0fc-55892c79ac47" />

## Port Scanner
-     Disclaimer: This tool is intended only for systems that you own or are authorized to test.
- Developed a Python-based TCP port scanner using Socket Programming to identify open network services and strengthen understanding of TCP/IP networking. Created for educational and home-lab use only.
- The script will:
     1. Scan Common TCP Ports.
     2. Identify Open and Closed Ports.
     3. Use Python Socket Programming.
     4. Provide a Simple Scan Summary.
- Output:
  <img width="1098" height="713" alt="image" src="https://github.com/user-attachments/assets/b0990350-97a0-411f-b787-c81a2d34ea45" />

## Password Generator
-     Security Note: I've used Python's `secrets` module rather than the `random` module because it is designed for generating secure credentials and authentication tokens.
- Developed a Python-based secure password generator utilizing cryptographically secure randomness (secrets module) and password complexity validation to reinforce authentication security best practices.
- The script:
     1. Uses Python's "secrets" module.
     2. Enforces Strong Password Complexity.
     3. Includes Uppercase, Lowercase, Numeric, and Special Characters.
     4. Built-in Password Strength Validation.
- Output:
  <img width="1108" height="513" alt="image" src="https://github.com/user-attachments/assets/489c55f1-02db-478f-ac71-7881006ad44d" />

## File Integrity Checker
- Developed a Python-based File Integrity Monitoring (FIM) tool utilizing SHA256 cryptographic hashing to verify file integrity and detect unauthorized modifications.
- The script will:
     1. Generate SHA256 Hashes.
     2. Verify File Integrity.
     3. Detect Unauthorized File Modifications.
- How It Works:
     - Step 1: Generate a Baseline Hash.
     - Say you have a document "document.txt"
     - Run "python file-hash-checker.py" and Choose Option 1 "Generate SHA256 hash" and provide the File Path and store the Generated Hash.
     - Step 2: Verify Integrity Later.
     - Run "python file-hash-checker.py" and Choose Option 2 "Verify file integrity" and provide the File Path and previously Stored Hash from Step 1.
     - Result: If the file has not changed, it will Pass the Integrity Check else Fail and display that the file has been modified.
- Output:
  <img width="1163" height="914" alt="image" src="https://github.com/user-attachments/assets/aa3065e0-5e55-46ac-9722-2ed5fc257abf" />
