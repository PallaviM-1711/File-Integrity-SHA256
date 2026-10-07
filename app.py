import tkinter as tk
from tkinter import filedialog, messagebox
import hashlib
import json
import os
from datetime import datetime


# ============================================================
# CONFIGURATION
# ============================================================

REFERENCE_FILE = "reference_hash.json"
CHUNK_SIZE = 4096


# ============================================================
# SHA-256 CALCULATION
# ============================================================

def calculate_sha256(file_path):

    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:

            while True:

                data = file.read(CHUNK_SIZE)

                if not data:
                    break

                sha256.update(data)

        return sha256.hexdigest()

    except Exception as error:

        messagebox.showerror(
            "Error",
            f"Unable to calculate SHA-256:\n\n{error}"
        )

        return None


# ============================================================
# BROWSE FILE
# ============================================================

def browse_file():

    file_path = filedialog.askopenfilename(
        title="Select File"
    )

    if not file_path:
        return

    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

    # File information
    file_name = os.path.basename(file_path)

    try:
        file_size = os.path.getsize(file_path)

        if file_size < 1024:
            size_text = f"{file_size} bytes"

        elif file_size < 1024 * 1024:
            size_text = f"{file_size / 1024:.2f} KB"

        else:
            size_text = f"{file_size / (1024 * 1024):.2f} MB"

    except Exception:
        size_text = "Unknown"

    file_info_label.config(
        text=f"File: {file_name}    •    Size: {size_text}"
    )

    reset_hash_display()

    status_label.config(
        text="READY FOR VERIFICATION",
        fg="#475467"
    )


# ============================================================
# CREATE REFERENCE HASH
# ============================================================

def create_reference():

    file_path = file_entry.get().strip()

    if not file_path:

        messagebox.showwarning(
            "No File Selected",
            "Please select a file first."
        )

        return

    if not os.path.isfile(file_path):

        messagebox.showerror(
            "File Not Found",
            "The selected file does not exist."
        )

        return

    file_hash = calculate_sha256(file_path)

    if file_hash is None:
        return

    absolute_path = os.path.abspath(file_path)

    reference_data = {
        "file_name": os.path.basename(file_path),
        "file_path": absolute_path,
        "sha256": file_hash,
        "created_at": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    }

    try:

        with open(
            REFERENCE_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                reference_data,
                file,
                indent=4
            )

    except Exception as error:

        messagebox.showerror(
            "Error",
            f"Unable to save reference hash:\n\n{error}"
        )

        return

    original_hash_label.config(
        text=file_hash
    )

    current_hash_label.config(
        text="Not checked yet"
    )

    status_label.config(
        text="✓ REFERENCE HASH CREATED",
        fg="#16803c"
    )

    timestamp_label.config(
        text=f"Reference created: "
             f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
    )

    messagebox.showinfo(
        "Success",
        "Reference SHA-256 hash created successfully."
    )


# ============================================================
# VERIFY FILE
# ============================================================

def verify_file():

    file_path = file_entry.get().strip()

    if not file_path:

        messagebox.showwarning(
            "No File Selected",
            "Please select a file first."
        )

        return

    if not os.path.isfile(file_path):

        messagebox.showerror(
            "File Not Found",
            "The selected file does not exist."
        )

        return

    if not os.path.exists(REFERENCE_FILE):

        messagebox.showwarning(
            "Reference Not Found",
            "Please create a reference hash first."
        )

        return

    try:

        with open(
            REFERENCE_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            reference_data = json.load(file)

    except Exception as error:

        messagebox.showerror(
            "Reference Error",
            f"Unable to read reference information:\n\n{error}"
        )

        return

    original_file_path = reference_data.get(
        "file_path"
    )

    original_hash = reference_data.get(
        "sha256"
    )

    current_file_path = os.path.abspath(
        file_path
    )

    # Check whether this is the same file
    if current_file_path != original_file_path:

        status_label.config(
            text="⚠ WRONG FILE SELECTED",
            fg="#d92d20"
        )

        messagebox.showwarning(
            "File Mismatch",
            "The selected file is different from "
            "the reference file."
        )

        return

    # Calculate current hash
    current_hash = calculate_sha256(
        file_path
    )

    if current_hash is None:
        return

    # Display hashes
    original_hash_label.config(
        text=original_hash
    )

    current_hash_label.config(
        text=current_hash
    )

    # Current verification time
    timestamp_label.config(
        text=f"Last verified: "
             f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}"
    )

    # Compare hashes
    if original_hash == current_hash:

        status_label.config(
            text="✓ FILE INTEGRITY VERIFIED",
            fg="#16803c"
        )

        result_box.config(
            bg="#ecfdf3"
        )

        result_icon.config(
            text="✓",
            fg="#16803c",
            bg="#ecfdf3"
        )

        result_text.config(
            text="FILE IS INTEGRITY SAFE",
            fg="#16803c",
            bg="#ecfdf3"
        )

        messagebox.showinfo(
            "Integrity Verified",
            "The file has NOT been modified.\n\n"
            "Original and current SHA-256 hashes match."
        )

    else:

        status_label.config(
            text="⚠ FILE HAS BEEN MODIFIED!",
            fg="#d92d20"
        )

        result_box.config(
            bg="#fef3f2"
        )

        result_icon.config(
            text="⚠",
            fg="#d92d20",
            bg="#fef3f2"
        )

        result_text.config(
            text="FILE HAS BEEN MODIFIED",
            fg="#d92d20",
            bg="#fef3f2"
        )

        messagebox.showwarning(
            "File Modified",
            "WARNING: The file has been modified!\n\n"
            "The SHA-256 hashes do not match."
        )


# ============================================================
# COPY CURRENT HASH
# ============================================================

def copy_hash():

    current_hash = current_hash_label.cget("text")

    if (
        not current_hash
        or current_hash == "Not checked yet"
        or current_hash == "Not available"
    ):

        messagebox.showwarning(
            "No Hash Available",
            "There is no current SHA-256 hash to copy."
        )

        return

    root.clipboard_clear()
    root.clipboard_append(current_hash)
    root.update()

    messagebox.showinfo(
        "Copied",
        "SHA-256 hash copied to clipboard."
    )


# ============================================================
# RESET APPLICATION
# ============================================================

def reset_application():

    file_entry.delete(
        0,
        tk.END
    )

    file_info_label.config(
        text="No file selected"
    )

    reset_hash_display()

    status_label.config(
        text="READY FOR VERIFICATION",
        fg="#475467"
    )

    timestamp_label.config(
        text="No verification performed"
    )


# ============================================================
# RESET HASH DISPLAY
# ============================================================

def reset_hash_display():

    original_hash_label.config(
        text="Not available"
    )

    current_hash_label.config(
        text="Not available"
    )

    result_box.config(
        bg="#f8fafc"
    )

    result_icon.config(
        text="●",
        fg="#98a2b3",
        bg="#f8fafc"
    )

    result_text.config(
        text="WAITING FOR VERIFICATION",
        fg="#667085",
        bg="#f8fafc"
    )

    timestamp_label.config(
        text="No verification performed"
    )


# ============================================================
# MAIN WINDOW
# ============================================================

root = tk.Tk()

root.title(
    "File Integrity Verification - SHA-256"
)

root.geometry(
    "1000x760"
)

root.resizable(
    False,
    False
)

root.configure(
    bg="#f5f7fa"
)


# ============================================================
# HEADER
# ============================================================

header = tk.Frame(
    root,
    bg="#16213e",
    height=110
)

header.pack(
    fill="x"
)

header.pack_propagate(False)


title_label = tk.Label(
    header,
    text="🔐  FILE INTEGRITY VERIFICATION",
    font=(
        "Segoe UI",
        25,
        "bold"
    ),
    bg="#16213e",
    fg="white"
)

title_label.pack(
    pady=(18, 2)
)


subtitle_label = tk.Label(
    header,
    text="SHA-256 Cryptographic File Integrity Monitoring",
    font=(
        "Segoe UI",
        11
    ),
    bg="#16213e",
    fg="#d0d5dd"
)

subtitle_label.pack()


# ============================================================
# MAIN CONTENT
# ============================================================

content = tk.Frame(
    root,
    bg="#f5f7fa"
)

content.pack(
    fill="both",
    expand=True,
    padx=45,
    pady=25
)


# ============================================================
# FILE SELECTION CARD
# ============================================================

file_card = tk.Frame(
    content,
    bg="white",
    bd=1,
    relief="solid"
)

file_card.pack(
    fill="x"
)


file_title = tk.Label(
    file_card,
    text="📁  SELECT FILE",
    font=(
        "Segoe UI",
        12,
        "bold"
    ),
    bg="white",
    fg="#16213e"
)

file_title.pack(
    anchor="w",
    padx=20,
    pady=(16, 8)
)


file_entry_frame = tk.Frame(
    file_card,
    bg="white"
)

file_entry_frame.pack(
    fill="x",
    padx=20
)


file_entry = tk.Entry(
    file_entry_frame,
    font=(
        "Segoe UI",
        10
    ),
    bd=1,
    relief="solid"
)

file_entry.pack(
    side="left",
    fill="x",
    expand=True,
    ipady=9
)


browse_button = tk.Button(
    file_entry_frame,
    text="Browse",
    command=browse_file,
    font=(
        "Segoe UI",
        10,
        "bold"
    ),
    bg="#16213e",
    fg="white",
    activebackground="#25365f",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=25,
    pady=9
)

browse_button.pack(
    side="right",
    padx=(10, 0)
)


file_info_label = tk.Label(
    file_card,
    text="No file selected",
    font=(
        "Segoe UI",
        9
    ),
    bg="white",
    fg="#667085"
)

file_info_label.pack(
    anchor="w",
    padx=20,
    pady=(7, 15)
)


# ============================================================
# ACTION BUTTONS
# ============================================================

action_frame = tk.Frame(
    content,
    bg="#f5f7fa"
)

action_frame.pack(
    pady=20
)


reference_button = tk.Button(
    action_frame,
    text="CREATE REFERENCE HASH",
    command=create_reference,
    font=(
        "Segoe UI",
        10,
        "bold"
    ),
    bg="#16213e",
    fg="white",
    activebackground="#25365f",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=28,
    pady=12
)

reference_button.pack(
    side="left",
    padx=8
)


verify_button = tk.Button(
    action_frame,
    text="VERIFY FILE INTEGRITY",
    command=verify_file,
    font=(
        "Segoe UI",
        10,
        "bold"
    ),
    bg="#16803c",
    fg="white",
    activebackground="#116b31",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=28,
    pady=12
)

verify_button.pack(
    side="left",
    padx=8
)


reset_button = tk.Button(
    action_frame,
    text="RESET",
    command=reset_application,
    font=(
        "Segoe UI",
        10,
        "bold"
    ),
    bg="#667085",
    fg="white",
    activebackground="#475467",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=28,
    pady=12
)

reset_button.pack(
    side="left",
    padx=8
)


# ============================================================
# HASH COMPARISON CARD
# ============================================================

hash_card = tk.Frame(
    content,
    bg="white",
    bd=1,
    relief="solid"
)

hash_card.pack(
    fill="x"
)


hash_title = tk.Label(
    hash_card,
    text="🔎  SHA-256 HASH COMPARISON",
    font=(
        "Segoe UI",
        12,
        "bold"
    ),
    bg="white",
    fg="#16213e"
)

hash_title.pack(
    anchor="w",
    padx=20,
    pady=(15, 12)
)


# Original hash

original_title = tk.Label(
    hash_card,
    text="Original / Reference SHA-256",
    font=(
        "Segoe UI",
        9,
        "bold"
    ),
    bg="white",
    fg="#475467"
)

original_title.pack(
    anchor="w",
    padx=20
)


original_hash_label = tk.Label(
    hash_card,
    text="Not available",
    font=(
        "Consolas",
        9
    ),
    bg="#f8fafc",
    fg="#344054",
    anchor="w",
    padx=10,
    pady=8
)

original_hash_label.pack(
    fill="x",
    padx=20,
    pady=(5, 12)
)


# Current hash

current_title = tk.Label(
    hash_card,
    text="Current SHA-256",
    font=(
        "Segoe UI",
        9,
        "bold"
    ),
    bg="white",
    fg="#475467"
)

current_title.pack(
    anchor="w",
    padx=20
)


current_hash_label = tk.Label(
    hash_card,
    text="Not available",
    font=(
        "Consolas",
        9
    ),
    bg="#f8fafc",
    fg="#344054",
    anchor="w",
    padx=10,
    pady=8
)

current_hash_label.pack(
    fill="x",
    padx=20,
    pady=(5, 15)
)


# ============================================================
# RESULT BOX
# ============================================================

result_box = tk.Frame(
    content,
    bg="#f8fafc",
    bd=1,
    relief="solid"
)

result_box.pack(
    fill="x",
    pady=20
)


result_icon = tk.Label(
    result_box,
    text="●",
    font=(
        "Segoe UI",
        18,
        "bold"
    ),
    bg="#f8fafc",
    fg="#98a2b3"
)

result_icon.pack(
    side="left",
    padx=(25, 10),
    pady=15
)


result_text = tk.Label(
    result_box,
    text="WAITING FOR VERIFICATION",
    font=(
        "Segoe UI",
        13,
        "bold"
    ),
    bg="#f8fafc",
    fg="#667085"
)

result_text.pack(
    side="left",
    pady=15
)


# ============================================================
# STATUS + TIMESTAMP
# ============================================================

status_label = tk.Label(
    content,
    text="READY FOR VERIFICATION",
    font=(
        "Segoe UI",
        11,
        "bold"
    ),
    bg="#f5f7fa",
    fg="#475467"
)

status_label.pack(
    pady=(0, 5)
)


timestamp_label = tk.Label(
    content,
    text="No verification performed",
    font=(
        "Segoe UI",
        9
    ),
    bg="#f5f7fa",
    fg="#98a2b3"
)

timestamp_label.pack()


# ============================================================
# COPY BUTTON
# ============================================================

copy_button = tk.Button(
    content,
    text="📋 Copy Current SHA-256",
    command=copy_hash,
    font=(
        "Segoe UI",
        9,
        "bold"
    ),
    bg="#ffffff",
    fg="#16213e",
    activebackground="#eaecf0",
    relief="solid",
    cursor="hand2",
    padx=15,
    pady=6
)

copy_button.pack(
    pady=10
)


# ============================================================
# FOOTER
# ============================================================

footer = tk.Label(
    root,
    text="SHA-256  •  Cryptographic Hashing  •  File Integrity  •  Cybersecurity",
    font=(
        "Segoe UI",
        8
    ),
    bg="#f5f7fa",
    fg="#98a2b3"
)

footer.pack(
    side="bottom",
    pady=8
)


# ============================================================
# START APPLICATION
# ============================================================

root.mainloop()