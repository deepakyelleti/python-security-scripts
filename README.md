# python-security-scripts
Python automation scripts for IT administration and cybersecurity tasks.

## Scripts
- Password Policy Audit Script
    Built a Python-based audit tool that evaluates password strength and returns a list of policy violations. I also used "getpass" which ensures that the password isn't visible on screen when a user types it in, preventing shoulder surfing.
    The script will check for:
     1. Length.
     2. Uppercase.
     3. Lowercase.
     4. Numerical Digit.
     5. Special Character.

- Log Analyzer
    Built a Python-based log analysis tool to identify failed authentication attempts and detect suspicious login behavior through log parsing and incident reporting. Please use a "sample_auth.log" file to verify.
    The script will:
     1. Read a Log File.
     2. Detect Failed Login Attempts.
     3. Extract: Timestamp, IP Address, Username (if available).
     4. Count Repeated Failed Logins.
     5. Flag Suspicious Activity (Multiple failures from same IP).

- Port Scanner
- Password Generator
- File Integrity Checker
