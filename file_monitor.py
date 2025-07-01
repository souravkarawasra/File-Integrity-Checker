import os
import hashlib
import json
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

HASH_FILE = "file_hashes.json"

def calculate_hash(filepath):
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        return None

def scan_directory(directory):
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for name in files:
            filepath = os.path.join(root, name)
            file_hashes[filepath] = calculate_hash(filepath)
    return file_hashes

def load_previous_hashes():
    if os.path.exists(HASH_FILE):
        with open(HASH_FILE, "r") as f:
            return json.load(f)
    return {}

def save_hashes(hashes):
    with open(HASH_FILE, "w") as f:
        json.dump(hashes, f, indent=4)

def compare_hashes(old_hashes, new_hashes):
    modified = []
    added = []
    deleted = []

    for file, hash_val in new_hashes.items():
        if file not in old_hashes:
            added.append(file)
        elif old_hashes[file] != hash_val:
            modified.append(file)

    for file in old_hashes:
        if file not in new_hashes:
            deleted.append(file)

    return modified, added, deleted

def browse_directory():
    folder = filedialog.askdirectory()
    if folder:
        folder_path.set(folder)

def start_scan():
    directory = folder_path.get()
    if not directory or not os.path.isdir(directory):
        messagebox.showerror("Error", "Please select a valid directory.")
        return

    old_hashes = load_previous_hashes()
    new_hashes = scan_directory(directory)
    modified, added, deleted = compare_hashes(old_hashes, new_hashes)

    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, f"Scanning directory: {directory}\n\n")

    if not modified and not added and not deleted:
        output_text.insert(tk.END, "✅ No changes detected.\n")
    else:
        if modified:
            output_text.insert(tk.END, f"🔄 Modified Files:\n" + "\n".join(modified) + "\n\n")
        if added:
            output_text.insert(tk.END, f"➕ New Files:\n" + "\n".join(added) + "\n\n")
        if deleted:
            output_text.insert(tk.END, f"❌ Deleted Files:\n" + "\n".join(deleted) + "\n\n")

    save_hashes(new_hashes)

# -------- GUI Setup --------
root = tk.Tk()
root.title("File Change Monitor Tool")
root.geometry("700x500")

folder_path = tk.StringVar()

tk.Label(root, text="Select Folder to Monitor:").pack(pady=5)
tk.Entry(root, textvariable=folder_path, width=60).pack(pady=2)
tk.Button(root, text="Browse", command=browse_directory).pack(pady=2)
tk.Button(root, text="Start Scan", command=start_scan, bg="#4CAF50", fg="white").pack(pady=10)

output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
output_text.pack(padx=10, pady=10)

root.mainloop()
