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

## 🖥️ Application Features

### 1. File Selection

The user can select a file using the **Browse** button.

### 2. Reference Hash Creation

The application calculates the SHA-256 hash and stores it as the trusted reference value.

### 3. File Verification

The application calculates the current SHA-256 hash of the selected file.

### 4. Hash Comparison

The original hash and current hash are compared.

### 5. Modification Detection

If the hashes are different, the application reports that the file has been modified.

### 6. Graphical User Interface

The project provides a user-friendly GUI using Python Tkinter.

### 7. Hash Copying

The current SHA-256 hash can be copied to the clipboard.

---

## 🧪 Testing

The system was tested using two main scenarios.

### Test Case 1 — File Not Modified

The reference hash and current hash are identical.

```text
Original SHA-256:
91657a122eb61ef8173e5f97aa3a9f7e52d321155bf224ac40e11c007fe5e990

Current SHA-256:
91657a122eb61ef8173e5f97aa3a9f7e52d321155bf224ac40e11c007fe5e990