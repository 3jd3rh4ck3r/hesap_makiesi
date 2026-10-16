# 🧮 3jd3rh4ck3r Calculator

**A classic and scientific calculator built with Python and Tkinter.**

A simple desktop calculator with a dark interface, scientific functions, repeat-equals functionality, and support for displaying large integer results.

## ✨ Features

- **Classic Mode** — Addition, subtraction, multiplication, division, and modulo.
- **Scientific Mode** — Sine, cosine, tangent, square root, logarithms, absolute value, factorial, and exponentiation.
- **Mode Switching** — Switch between classic and scientific modes with a single button.
- **DEG/RAD Support** — Choose degrees or radians for trigonometric calculations.
- **Repeat Equals (`=`)** — Press equals repeatedly to repeat the last basic arithmetic operation.
- **Calculation History** — View previous calculations.
- **Large Integer Display** — Display large integer results using regular digits instead of scientific notation.
- **Keyboard Support** — Press `Enter` to calculate and `Esc` to clear the display.
- **Dark UI** — A dark-themed interface built with Tkinter.
- **Developer Signature** — `coded by 3jd3rh4ck3r`

## 🛠️ Built With

- Python 3
- Tkinter
- Python Standard Library (`math`, `ast`, `operator`)

## 📋 Requirements

- Python 3.9 or later recommended
- Tkinter installed and available on your system

On Debian-based Linux distributions, install Tkinter if necessary:

```bash
sudo apt update
sudo apt install python3-tk
```

## 🚀 Installation

**1. Clone the repository**

Replace `YOUR_USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR_USERNAME/3jd3rh4ck3r-calculator.git
```

**2. Enter the project directory**

```bash
cd 3jd3rh4ck3r-calculator
```

**3. Run the calculator**

```bash
python3 hesap.py
```

No additional Python packages are required when Python and Tkinter are installed.

## 🖥️ Usage

1. Launch the application.
2. Use the number and operator buttons for basic calculations.
3. Press **Scientific Mode** to access scientific functions.
4. Use **DEG/RAD** to change the angle unit.
5. Press `=` to calculate. Press it again to repeat the last supported arithmetic operation.
6. Open **History** in scientific mode to review previous calculations.

### Example: Repeat Equals

```text
5 + 3 = 8
       = 11
       = 14
```

## 📁 Project Structure

```text
3jd3rh4ck3r-calculator/
├── hesap.py
├── README.md
└── LICENSE
```

The `LICENSE` file is optional. Add one if you decide to publish the project under an open-source license.

## ⚠️ Notes and Limitations

- Very large integer results can be displayed as regular digits.
- Floating-point calculations have limited precision.
- The visible portion of a long number depends on the display width.
- Repeat-equals functionality is designed for basic binary arithmetic operations.
- Scientific functions may return an error for invalid inputs, such as the square root of a negative number in the real-number domain.

## 🔒 Security

The calculator evaluates expressions using a restricted Python AST evaluator rather than unrestricted `eval()`. This is intended to limit which expressions can be executed.

## 👨‍💻 Developer

**3jd3rh4ck3r**

Created with Python and Tkinter.

---

*If you find this project useful, consider giving the repository a ⭐ on GitHub.*
