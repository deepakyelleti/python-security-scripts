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

## Log Analyzer
- Built a Python-based log analysis tool to identify Failed Authentication Attempts and detect Suspicious Login Behavior through Log Analysis and Incident Reporting. Please use a "sample_auth.log" file to verify.
- The script will:
     1. Read a Log File.
     2. Detect Failed Login Attempts.
     3. Extract: Timestamp, IP Address, Username (if available).
     4. Count Repeated Failed Logins.
     5. Flag Suspicious Activity (Multiple failures from same IP).

## Port Scanner
-     Disclaimer: This tool is intended only for systems that you own or are authorized to test.
- Developed a Python-based TCP port scanner using Socket Programming to identify open network services and strengthen understanding of TCP/IP networking. Created for educational and home-lab use only.
- The script will:
     1. Scan Common TCP Ports.
     2. Identify Open and Closed Ports.
     3. Use Python Socket Programming.
     4. Provide a Simple Scan Summary.

## Password Generator
- 

## File Integrity Checker
- 
