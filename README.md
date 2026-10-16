# 🧮 3jd3rh4ck3r Calculator

A dark-themed scientific calculator built with Python and Tkinter. Supports basic arithmetic, scientific functions, calculation history, and standalone builds for Linux and Windows.

## 📥 Download

**[⬇️ Download HesapMakinesi for Windows](https://github.com/3jd3rh4ck3r/hesap_makiesi/raw/refs/heads/main/dist/HesapMakinesi.zip)**

1. Download the ZIP file.
2. Extract its contents.
3. Run `HesapMakinesi.exe`.

> If Windows displays a security warning, make sure you trust the source before running the application.

## ✨ Features

- Basic arithmetic: addition, subtraction, multiplication, and division
- Modulo and power operations
- Scientific functions: `sin`, `cos`, `tan`, square root, logarithms, absolute value, and factorial
- Degree (DEG) and radian (RAD) modes
- Calculation history
- Repeat the last arithmetic operation with `=`
- Dark-themed graphical interface
- Improved formatting for large integer results
- Linux executable and Windows executable build support

## 🛠️ Requirements

To run from source:

- Python 3.9 or newer recommended
- Tkinter

To build standalone applications:

- PyInstaller

## 🚀 Run from Source

Clone the repository:

```bash
git clone https://github.com/3jd3rh4ck3r/hesap_makiesi.git
cd hesap_makiesi
```

Run the calculator:

```bash
python3 hesap.py
```

## 🐧 Build for Linux

Install the required packages on Debian-based Linux distributions:

```bash
sudo apt update
sudo apt install python3-tk python3-venv
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install pyinstaller
```

Build the executable:

```bash
pyinstaller --clean --onefile --windowed --name HesapMakinesi hesap.py
```

The resulting executable will be located at:

```text
dist/HesapMakinesi
```

Run it with:

```bash
./dist/HesapMakinesi
```

## 🪟 Build for Windows

Run these commands on Windows with Python installed:

```powershell
py -m pip install pyinstaller
py -m PyInstaller --clean --onefile --windowed --name HesapMakinesi hesap.py
```

The executable will be created at:

```text
dist/HesapMakinesi.exe
```

**Note:** PyInstaller builds for the operating system on which it runs. To create a Windows `.exe` from Linux, use a Windows machine or a Windows-based GitHub Actions workflow.

## 📁 Project Structure

```text
hesap_makiesi/
├── hesap.py
├── README.md
└── dist/
    └── HesapMakinesi.zip
```

The structure above is illustrative; generated build files may differ.

## ⚠️ Notes

- Floating-point calculations have the usual Python precision limitations.
- Only download and run executable files from sources you trust.
- Test Linux and Windows builds on their respective operating systems.

## 👨‍💻 Author

**3jd3rh4ck3r**

*coded by 3jd3rh4ck3r*

## 📜 License

No license has been specified. Add a `LICENSE` file if you want to define the terms under which others may use, modify, or distribute this project.
