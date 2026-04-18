import os
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext

LARGE_FILE_SIZE = 10 * 1024 * 1024  # 10 MB


def get_category(file_name, file_path):
    if os.path.getsize(file_path) > LARGE_FILE_SIZE:
        return "LARGE_FILES"

    ext = os.path.splitext(file_name)[1].lower().replace(".", "")
    return ext.upper() if ext else "Others"


def get_unique_path(path):
    base, ext = os.path.splitext(path)
    counter = 1

    while os.path.exists(path):
        path = f"{base}({counter}){ext}"
        counter += 1

    return path


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Pro File Organizer")
        self.root.geometry("650x500")

        self.folder_path = ""
        self.last_moves = []  # for undo

        self.log_dir = os.path.join(os.getcwd(), "logs")
        os.makedirs(self.log_dir, exist_ok=True)

        self.label = tk.Label(root, text="No folder selected")
        self.label.pack(pady=10)

        tk.Button(root, text="Select Folder", command=self.select_folder).pack(pady=5)

        self.dry_run = tk.BooleanVar()
        tk.Checkbutton(root, text="Dry Run", variable=self.dry_run).pack()

        self.progress = tk.Label(root, text="Progress: 0%")
        self.progress.pack(pady=5)

        tk.Button(root, text="Start", command=self.organize).pack(pady=5)
        tk.Button(root, text="Undo Last", command=self.undo_last).pack(pady=5)

        self.output = scrolledtext.ScrolledText(root, width=75, height=18)
        self.output.pack()

    def select_folder(self):
        self.folder_path = filedialog.askdirectory()
        self.label.config(text=self.folder_path)

    def log(self, message):
        self.output.insert(tk.END, message + "\n")
        self.output.see(tk.END)

        log_file = os.path.join(self.log_dir, f"log_{datetime.now().date()}.txt")
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(message + "\n")

    def organize(self):
        if not self.folder_path:
            messagebox.showerror("Error", "Please select a folder")
            return

        self.last_moves.clear()
        dry_run = self.dry_run.get()

        self.log(f"\n--- Run at {datetime.now()} ---")
        self.log(f"Dry Run: {dry_run}")

        files = [
            f for f in os.listdir(self.folder_path)
            if os.path.isfile(os.path.join(self.folder_path, f))
            and not f.startswith(".")  # ignore hidden
        ]

        if not files:
            self.log("No files to organize")
            return

        categorized = {}
        for file in files:
            path = os.path.join(self.folder_path, file)
            category = get_category(file, path)
            categorized.setdefault(category, []).append(file)

        stats = {}
        total = len(files)
        done = 0

        for category, file_list in categorized.items():
            target_folder = os.path.join(self.folder_path, category)

            if not dry_run:
                os.makedirs(target_folder, exist_ok=True)

            for file in file_list:
                src = os.path.join(self.folder_path, file)
                dest = os.path.join(target_folder, file)

                dest = get_unique_path(dest)

                if dry_run:
                    msg = f"[DRY RUN] {file} → {category}/"
                else:
                    shutil.move(src, dest)
                    self.last_moves.append((dest, src))
                    msg = f"Moved: {file} → {category}/"

                self.log(msg)

                stats[category] = stats.get(category, 0) + 1

                done += 1
                percent = int((done / total) * 100)
                self.progress.config(text=f"Progress: {percent}%")
                self.root.update()

        self.log("\n--- Summary ---")
        for k, v in stats.items():
            self.log(f"{k}: {v}")

        if not dry_run:
            os.startfile(self.folder_path)

    def undo_last(self):
        if not self.last_moves:
            self.log("Nothing to undo")
            return

        for src, dest in self.last_moves:
            if os.path.exists(src):
                shutil.move(src, dest)

        self.log("Undo completed")
        self.last_moves.clear()


root = tk.Tk()
app = App(root)
root.mainloop()