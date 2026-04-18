# 📂 Dynamic File Organizer

### 🚀 Python Desktop Automation Tool

A production-style desktop application built with Python and Tkinter that intelligently organizes files in any directory based on their **file type and size**, with a strong focus on safety, usability, and automation.

---

## ✨ Overview

Managing messy folders manually is inefficient and error-prone.

This tool automates file organization by:
- Analyzing files dynamically
- Grouping them intelligently
- Ensuring safe operations with undo support and logging

It is designed as a **real-world desktop utility**, not just a script.

---

## 🔥 Key Features

### 📁 Smart File Organization
- Automatically organizes files based on **file extensions**
- Fully **dynamic system** (no hardcoded mappings required)
- Creates folders only when needed (no empty folders)

---

### 🧠 Intelligent Processing
- Detects **large files** and separates them into a dedicated folder
- Prevents **data loss** by avoiding overwrites (auto-renaming duplicates)
- Skips hidden/system files for clean processing

---

### 🛡️ Safety & Control
- 🧪 **Dry Run Mode** → Preview all actions before execution
- 🔁 **Undo Feature** → Revert the last operation safely
- 🧾 **Logging System** → Tracks all operations with timestamps (daily logs)

---

### ⚡ User Experience
- 🖥️ Simple and clean **Tkinter GUI**
- 📊 Real-time progress tracking
- 📂 Auto-opens folder after execution (Windows)

---

## 🏗️ Architecture

The project follows a clean modular structure:

- **File Detection Layer** → Classifies files by type & size  
- **Processing Engine** → Handles safe file movement & grouping  
- **UI Layer (Tkinter)** → User interaction & control  
- **Logging System** → Full traceability of actions  

---

## 🛠️ Tech Stack

- Python 3
- Tkinter (GUI)
- OS Module (File system operations)
- Shutil (File handling)
- Datetime (Logging system)

---

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/dynamic-file-organizer.git
cd dynamic-file-organizer

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/emanemad-dev/file-organizer-automation.git
cd file-organizer-automation
```

### 2. Run the application

```bash
python file_organizer.py
```

---

## 💡 Use Cases

* Organizing messy **Downloads** folders
* Cleaning up large directories
* Preparing structured files for backups
* Improving daily file management workflow

---

## ⚠️ Notes

* No files are deleted — only moved safely
* All operations can be reversed using **Undo**
* Designed with a **safe-first approach**

---

## 📈 Future Improvements

* Preview table before execution
* Scheduled automatic execution (Task Scheduler integration)
* Custom file size filters via GUI
* Multi-directory processing
* Export logs to CSV
* Configurable rules via settings file

---

## 👩‍💻 Author

Built as a hands-on project to explore **Python Automation & Desktop Applications**.

---

## ⭐ Support

If you found this project useful, consider giving it a star ⭐
