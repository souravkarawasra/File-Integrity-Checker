# Project Name: FILE INTEGRITY CHECKER
COMPANY: CODETECH IT SOLUTIONS

NAME: SOURAV

INTERN ID: CT04DG3230

DOMIAN: Cyber Security & Ethical Hacking

DURATION: 4 Weeks

MENTOR: NEELA SANTOSH

# Purpose:
This tool is designed to help users track changes in files within a selected folder. It calculates and stores the hash values (digital fingerprints) of files and compares them over time to detect any of the following:

✅ Modified files

➕ Newly added files

❌ Deleted files

# How It Works (Explanation of Code):
1. Hash Calculation:
The function calculate_hash(filepath) uses SHA-256 hashing via the hashlib module.

It reads each file in binary mode and generates a unique hash string based on its content.

If a file is edited, even slightly, the hash will change.

2. Directory Scanning:
scan_directory(directory) goes through all files in the chosen folder and subfolders using os.walk().

It creates a dictionary like:
{"path/to/file.txt": "hash_value"} for each file.

3. Saving Hashes:
save_hashes(hashes) stores the hash dictionary in a local file named file_hashes.json for future reference.

4. Loading Old Hashes:
load_previous_hashes() reads the previous scan data from the same JSON file.

If the file doesn't exist (first run), it returns an empty dictionary.

5. Comparing Changes:
compare_hashes(old, new) compares old and new hash dictionaries:

If a file is in the new set but not the old → it's new.

If it’s in both but hashes differ → it's modified.

If it’s in the old but not in the new → it's deleted.

6. GUI Interface:
Built using tkinter, a standard Python GUI library.

Features:

Folder selection (Browse button).

Start Scan (Start Scan button).

Output window (ScrolledText) showing detected changes.

7. User Interaction Flow:
User selects a folder.

Clicks "Start Scan".

Tool scans, compares, and shows differences (if any).

Changes are saved for the next run.

# Use Cases:
 Security: Detect unauthorized file changes (e.g., ransomware or malware attacks).

 Backup Management: Identify newly added or changed files to back up.

 Software Projects: Monitor code changes outside version control.

 Corporate Compliance: Track document changes in sensitive directories.

# Advantages:
No need to manually check thousands of files.

Easy GUI makes it user-friendly even for non-programmers.

Lightweight and does not require internet or heavy dependencies.

# Output 
![Image](Screenshot 2025-07-06 103336)