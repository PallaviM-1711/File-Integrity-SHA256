# File Integrity Verification System Using SHA-256

A Python-based cybersecurity application that verifies the integrity of files using the SHA-256 cryptographic hash algorithm.

## Features

- Generate SHA-256 hash of a file
- Store a reference hash
- Verify file integrity
- Detect file modifications
- Compare original and current hashes
- Graphical User Interface using Tkinter
- Browse and select files
- Display verification status

## Technologies Used

- Python
- Tkinter
- hashlib
- JSON
- SHA-256

## How It Works

1. Select a file using the Browse button.
2. Generate its SHA-256 hash.
3. Store the hash as a reference value.
4. Verify the file later.
5. Calculate the current SHA-256 hash.
6. Compare the current hash with the reference hash.
7. If both hashes match, the file has not been modified.
8. If the hashes differ, the application reports that the file has been modified.

## Applications

- Digital forensics
- Security monitoring
- File integrity checking
- Malware detection
- Data verification

## How to Run

Run the graphical application using:

```bash
python app.py