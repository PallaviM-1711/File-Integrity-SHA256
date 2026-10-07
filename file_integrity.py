import hashlib
import json
import os


# ============================================================
# CONFIGURATION
# ============================================================

REFERENCE_FILE = "reference_hash.json"
CHUNK_SIZE = 4096


# ============================================================
# FUNCTION 1: CALCULATE SHA-256 HASH
# ============================================================

def calculate_sha256(file_path):
    """
    Calculates the SHA-256 hash of a file.
    """

    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:

            while True:
                data = file.read(CHUNK_SIZE)

                if not data:
                    break

                sha256.update(data)

        return sha256.hexdigest()

    except FileNotFoundError:
        print("\n[ERROR] File not found.")
        return None

    except PermissionError:
        print("\n[ERROR] Permission denied.")
        return None

    except Exception as error:
        print(f"\n[ERROR] {error}")
        return None


# ============================================================
# FUNCTION 2: CREATE REFERENCE HASH
# ============================================================

def create_reference(file_path):

    if not os.path.isfile(file_path):
        print("\n[ERROR] The specified file does not exist.")
        return

    print("\nCalculating SHA-256 hash...")

    file_hash = calculate_sha256(file_path)

    if file_hash is None:
        return

    # Get absolute path
    absolute_path = os.path.abspath(file_path)

    # Create reference information
    reference_data = {
        "file_name": os.path.basename(file_path),
        "file_path": absolute_path,
        "sha256": file_hash
    }

    # Save reference information
    try:
        with open(REFERENCE_FILE, "w", encoding="utf-8") as file:
            json.dump(reference_data, file, indent=4)

    except Exception as error:
        print(f"\n[ERROR] Could not save reference hash: {error}")
        return

    print("\n==============================================")
    print("          REFERENCE HASH CREATED")
    print("==============================================")

    print(f"File Name : {os.path.basename(file_path)}")
    print(f"File Path : {absolute_path}")
    print(f"SHA-256   : {file_hash}")

    print("==============================================")
    print("Reference information saved successfully.")
    print("")


# ============================================================
# FUNCTION 3: VERIFY FILE INTEGRITY
# ============================================================

def verify_file(file_path):

    # Check whether reference file exists
    if not os.path.exists(REFERENCE_FILE):

        print("\n[ERROR] Reference hash does not exist.")

        print("\nPlease create a reference hash first")
        print("using Option 1.")

        return

    # Check whether selected file exists
    if not os.path.isfile(file_path):

        print("\n[ERROR] The specified file does not exist.")
        return

    # Read reference information
    try:

        with open(REFERENCE_FILE, "r", encoding="utf-8") as file:
            reference_data = json.load(file)

    except json.JSONDecodeError:

        print("\n[ERROR] Reference file is corrupted.")
        return

    except Exception as error:

        print(f"\n[ERROR] Could not read reference file: {error}")
        return

    # Extract stored information
    original_hash = reference_data.get("sha256")
    original_file_path = reference_data.get("file_path")

    if not original_hash or not original_file_path:

        print("\n[ERROR] Invalid reference information.")
        return

    # Get absolute path of selected file
    current_file_path = os.path.abspath(file_path)

    # Make sure we are checking the same file
    if current_file_path != original_file_path:

        print("\n==============================================")
        print("              FILE MISMATCH")
        print("==============================================")

        print("Reference File:")
        print(original_file_path)

        print("\nSelected File:")
        print(current_file_path)

        print("\n[WARNING] This is not the file used to")
        print("create the original reference hash.")

        print("==============================================")
        return

    # Calculate current hash
    print("\nCalculating current SHA-256 hash...")

    current_hash = calculate_sha256(file_path)

    if current_hash is None:
        return

    # Display results
    print("\n==============================================")
    print("           FILE INTEGRITY CHECK")
    print("==============================================")

    print(f"File Name:\n{os.path.basename(file_path)}")

    print("\nOriginal SHA-256:")
    print(original_hash)

    print("\nCurrent SHA-256:")
    print(current_hash)

    print("\n----------------------------------------------")

    # Compare hashes
    if original_hash == current_hash:

        print("✓ RESULT: FILE INTEGRITY VERIFIED")
        print("✓ The file has NOT been modified.")
        print("✓ Hash values match.")

    else:

        print("⚠ RESULT: FILE HAS BEEN MODIFIED!")
        print("⚠ The SHA-256 hashes do NOT match.")
        print("⚠ File integrity has been compromised.")

    print("==============================================")
    print("")


# ============================================================
# FUNCTION 4: DISPLAY MENU
# ============================================================

def display_menu():

    print("\n")
    print("==============================================")
    print("     FILE INTEGRITY VERIFICATION SYSTEM")
    print("                  USING SHA-256")
    print("==============================================")

    print("1. Create Reference Hash")
    print("2. Verify File Integrity")
    print("3. Exit")

    print("==============================================")


# ============================================================
# FUNCTION 5: MAIN PROGRAM
# ============================================================

def main():

    while True:

        display_menu()

        choice = input("Enter your choice (1-3): ").strip()

        # ----------------------------------------------------
        # OPTION 1: CREATE REFERENCE
        # ----------------------------------------------------

        if choice == "1":

            file_path = input(
                "\nEnter the file path: "
            ).strip()

            if not file_path:

                print("\n[ERROR] File path cannot be empty.")
                continue

            create_reference(file_path)

        # ----------------------------------------------------
        # OPTION 2: VERIFY FILE
        # ----------------------------------------------------

        elif choice == "2":

            file_path = input(
                "\nEnter the file path: "
            ).strip()

            if not file_path:

                print("\n[ERROR] File path cannot be empty.")
                continue

            verify_file(file_path)

        # ----------------------------------------------------
        # OPTION 3: EXIT
        # ----------------------------------------------------

        elif choice == "3":

            print("\n==============================================")
            print("Thank you for using the")
            print("File Integrity Verification System.")
            print("==============================================")
            print("Exiting...")

            break

        # ----------------------------------------------------
        # INVALID OPTION
        # ----------------------------------------------------

        else:

            print("\n[ERROR] Invalid choice.")
            print("Please enter 1, 2, or 3.")


# ============================================================
# PROGRAM START
# ============================================================

if __name__ == "__main__":
    main()