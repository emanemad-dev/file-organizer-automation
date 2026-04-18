# 📂 Dynamic File Organizer

### 🚀 Python Desktop Automation Tool

A production-style desktop application built with Python and Tkinter that intelligently organizes files in any directory based on their **extensions and size**, with a focus on safety, usability, and performance.

---

## ✨ Overview

Managing messy folders can be time-consuming and error-prone.
This tool automates the process by dynamically categorizing files, handling edge cases, and providing a safe, user-friendly interface.

---

## 🔥 Key Features

### 📁 Smart File Organization

* Automatically organizes files based on their **extensions**
* Supports **all file types dynamically** (no predefined mapping)

### 🧠 Intelligent Processing

* Detects and separates **large files** into a dedicated folder
* Prevents **duplicate overwrites** with automatic renaming
* Skips **hidden/system files** for clean results
* Avoids creating empty folders

### 🛡️ Safety & Control

* 🧪 **Dry Run Mode** → Preview changes before applying
* 🔁 **Undo Feature** → Revert the last operation instantly
* 🧾 **Logging System** → Track all operations with timestamps

### ⚡ User Experience

* 📊 Real-time **progress tracking**
* 🖥️ Clean and simple **GUI (Tkinter)**
* 📂 Automatically opens folder after execution

---

## 🏗️ Architecture & Design

The application follows a clean and modular structure:

* **File Categorization Layer** → Determines file destination (extension + size)
* **Processing Engine** → Handles grouping and safe file movement
* **UI Layer (Tkinter)** → Provides user interaction and feedback
* **Logging System** → Ensures traceability and debugging

---

## 🛠️ Tech Stack

* **Python 3**
* **Tkinter** – Desktop GUI
* **os / shutil** – File system operations

---

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/file-organizer.git
cd file-organizer
```

### 2. Run the application

```bash
python file_organizer_gui.py
```

---

## 📸 Demo

> Add screenshots or a short demo video here
> (Highly recommended for better visibility)

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
* Custom file size filters via GUI
* Multi-directory processing
* Export logs to CSV

---

## 👩‍💻 Author

Built as a hands-on project to explore **Python Automation & Desktop Applications**.

---

## ⭐ Support

If you found this project useful, consider giving it a star ⭐
