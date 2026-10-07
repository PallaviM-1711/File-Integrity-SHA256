# 🔐 File Integrity Verification System Using SHA-256

A Python-based cybersecurity application that verifies whether a file has been modified by comparing its current SHA-256 cryptographic hash with a trusted reference hash.

---

## 📌 Project Overview

File integrity is an important part of cybersecurity, digital forensics, and security monitoring.

Even a small change to a file can affect its SHA-256 hash. This project uses that property to detect unauthorized or unexpected modifications.

The application provides a graphical user interface (GUI) where users can:

- Select a file
- Generate its SHA-256 hash
- Store the hash as a trusted reference
- Verify the file at a later time
- Compare the original and current hashes
- Detect whether the file has been modified

---

## 🎯 Objectives

The main objectives of this project are:

1. Understand cryptographic hashing.
2. Implement SHA-256 using Python.
3. Generate a unique hash for a file.
4. Store a reference hash for integrity verification.
5. Detect modifications to files.
6. Understand the concept of file integrity.
7. Relate hashing to digital forensics and security monitoring.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Tkinter | Graphical User Interface |
| hashlib | SHA-256 hash generation |
| JSON | Reference hash storage |
| Git | Version control |
| GitHub | Source code hosting |

---

## 🔑 What is SHA-256?

SHA-256 is a cryptographic hash algorithm from the SHA-2 family.

It converts input data into a fixed-length **256-bit hash**, represented as a **64-character hexadecimal value**.

Example:

```text
Original File
     ↓
 SHA-256
     ↓
2630d20ee3bb5a8e7c71331ede03b37b8e124ed42c888289d0215b8b5ecc4585

---

## ⚙️ How the System Works

```text
              Select File
                  │
                  ▼
          Calculate SHA-256
                  │
                  ▼
        Create Reference Hash
                  │
                  ▼
          Store Reference
                  │
                  ▼
          Verify File Later
                  │
                  ▼
      Calculate Current Hash
                  │
                  ▼
        Compare Both Hashes
             /          \
            /            \
        MATCH          DIFFERENT
          │                │
          ▼                ▼
     ✓ VERIFIED        ⚠ MODIFIED

     ---

Basic Process
1. The user selects a file.
2. The application reads the file in binary mode.
3. SHA-256 is calculated using Python's hashlib library.
4. The generated hash is stored as a trusted reference.
5. When verification is requested, the file is hashed again.
6. The new hash is compared with the reference hash.
7. Matching hashes indicate that the file contents have not changed since the reference was created.
8. Different hashes indicate that the file contents have changed.
🖥️ Application Features
1. File Selection
The user can select a file using the Browse button.
2. Reference Hash Creation
The application calculates the SHA-256 hash and stores it as the trusted reference value.
3. File Verification
The application calculates the current SHA-256 hash of the selected file.
4. Hash Comparison
The original hash and current hash are displayed and compared.
5. Modification Detection
If the hashes are different, the application reports that the file has been modified.
6. Graphical User Interface
The project provides a user-friendly GUI developed using Python Tkinter.
7. File Information
The application displays information such as the selected file name and file size.
8. Verification Status
The application displays clear results such as:
✓ FILE INTEGRITY VERIFIED

or:
⚠ FILE HAS BEEN MODIFIED

9. Hash Copying
The current SHA-256 hash can be copied to the clipboard.
10. Reset Function
The application provides a reset option to clear the current file and verification results.
🧪 Testing
The application was tested using two main scenarios.
Test Case 1 — File Not Modified
A reference hash was generated for the original file.
The file was then verified without changing its contents.
Original SHA-256:
91657a122eb61ef8173e5f97aa3a9f7e52d321155bf224ac40e11c007fe5e990

Current SHA-256:
91657a122eb61ef8173e5f97aa3a9f7e52d321155bf224ac40e11c007fe5e990

Since both hashes are identical:
✓ FILE INTEGRITY VERIFIED

Test Case 2 — File Modified
The contents of the file were changed after creating the reference hash.
Original SHA-256:
3788ef2a11c368a4edfc2833cd9319045676040e3831746e640f0e06d566281a

Current SHA-256:
23efc6e19a684430bd343780487c45cb44f298ba98c00126d1d1bf4a804db02a

Since the hashes are different:
⚠ FILE HAS BEEN MODIFIED

This demonstrates that the system can successfully detect changes to the file.
🔒 File Integrity Concept
File integrity means ensuring that a file has not been changed, corrupted, or tampered with without authorization.
The system uses SHA-256 as a digital fingerprint of the file contents.
Same Content
     ↓
Same SHA-256 Hash
     ↓
Integrity Verified

Whereas:
Changed Content
     ↓
Different SHA-256 Hash
     ↓
Possible Modification

The system does not determine exactly what part of the file was changed. It determines whether the file's contents are different from the trusted reference version.
🕵️ Applications in Digital Forensics
Hashing is widely used in digital forensics to help verify the integrity of digital evidence.
An investigator can calculate a hash of an evidence file and preserve the hash as a reference value.
Evidence File
     ↓
SHA-256 Hash
     ↓
Reference Value
     ↓
Verify Later

If the calculated hash remains the same during later verification, the file contents are consistent with the reference version.
This can support evidence integrity verification during forensic analysis.
🛡️ Applications in Security Monitoring
File integrity verification can be useful for:
- Monitoring important system files
- Detecting unauthorized changes
- Checking configuration files
- Monitoring application files
- Detecting suspicious modifications
- Supporting malware investigations
- Security auditing
- Monitoring critical files
Organizations can periodically calculate hashes of important files and compare them with trusted reference values to identify unexpected changes.
🧩 System Modules
The application can be divided into the following modules:
Module 1 — File Selection
Allows the user to select a file through the graphical interface.
Module 2 — SHA-256 Hash Generation
Reads the selected file and calculates its SHA-256 hash.
Module 3 — Reference Hash Management
Stores the original SHA-256 hash as a trusted reference.
Module 4 — File Verification
Calculates the current hash of the selected file.
Module 5 — Hash Comparison
Compares the reference hash with the current hash.
Module 6 — Integrity Status
Displays whether the file is unchanged or modified.
📁 Project Structure
FileIntegritySHA256/
│
├── app.py
├── file_integrity.py
├── sample.txt
├── README.md
└── .gitignore

app.py
Contains the graphical user interface and file integrity verification functionality.
file_integrity.py
Contains the command-line implementation of the SHA-256 file integrity system.
sample.txt
Sample file used to demonstrate file integrity verification.
README.md
Project documentation and usage information.
.gitignore
Prevents temporary files, backup files, and locally generated reference data from being committed to the repository.