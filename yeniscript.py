import tkinter as tk
import math
import ast
import operator

# ---------------- AYARLAR ----------------

DEG_MODE = True
SCIENTIFIC_MODE = False
history = []

repeat_operator = None
repeat_operand = None
just_calculated = False

OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


# ---------------- SAYI BİÇİMLENDİRME ----------------

def format_result(value):
    if isinstance(value, int):
        return str(value)

    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError("Sonuç geçersiz")

        if value.is_integer():
            return str(int(value))

        return format(value, ".15f").rstrip("0").rstrip(".")

    return str(value)


# ---------------- BİLİMSEL FONKSİYONLAR ----------------

def sin_func(x):
    return math.sin(math.radians(x) if DEG_MODE else x)


def cos_func(x):
    return math.cos(math.radians(x) if DEG_MODE else x)


def tan_func(x):
    return math.tan(math.radians(x) if DEG_MODE else x)


def factorial_func(x):
    if x < 0 or not float(x).is_integer():
        raise ValueError("Faktöriyel tam sayı ister")
    if x > 170:
        raise ValueError("Sayı çok büyük")
    return math.factorial(int(x))


def safe_eval(expression):
    functions = {
        "sin": sin_func,
        "cos": cos_func,
        "tan": tan_func,
        "sqrt": math.sqrt,
        "log": math.log10,
        "ln": math.log,
        "abs": abs,
        "factorial": factorial_func,
    }

    constants = {
        "pi": math.pi,
        "e": math.e,
    }

    def evaluate(node):
        if isinstance(node, ast.Expression):
            return evaluate(node.body)

        if isinstance(node, ast.Constant):
            if isinstance(node.value, (int, float)):
                return node.value
            raise ValueError("Geçersiz değer")

        if isinstance(node, ast.Name):
            if node.id in constants:
                return constants[node.id]
            raise ValueError("Bilinmeyen sabit")

        if isinstance(node, ast.BinOp):
            op_type = type(node.op)

            if op_type not in OPERATORS:
                raise ValueError("Desteklenmeyen işlem")

            left = evaluate(node.left)
            right = evaluate(node.right)

            if op_type is ast.Pow and abs(right) > 10000:
                raise ValueError("Üs çok büyük")

            return OPERATORS[op_type](left, right)

        if isinstance(node, ast.UnaryOp):
            op_type = type(node.op)

            if op_type not in OPERATORS:
                raise ValueError("Geçersiz işlem")

            return OPERATORS[op_type](evaluate(node.operand))

        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name):
                raise ValueError("Geçersiz fonksiyon")

            name = node.func.id

            if name not in functions:
                raise ValueError("Bilinmeyen fonksiyon")

            if len(node.args) != 1 or node.keywords:
                raise ValueError("Fonksiyon tek sayı ister")

            return functions[name](evaluate(node.args[0]))

        raise ValueError("Geçersiz ifade")

    return evaluate(ast.parse(expression, mode="eval"))


# ---------------- PENCERE ----------------

root = tk.Tk()
root.title("3jd3rh4ck3r | Hesap Makinesi")
root.geometry("440x740")
root.minsize(350, 580)
root.configure(bg="#20242b")

# Uzun sayılar için yatay kaydırılabilir ekran
display_frame = tk.Frame(root, bg="#303640")
display_frame.pack(fill="x", padx=12, pady=12)

display = tk.Entry(
    display_frame,
    font=("Arial", 16),
    justify="right",
    bg="#303640",
    fg="white",
    insertbackground="white",
    relief="flat",
    bd=10
)
display.pack(fill="x", ipady=10)

mode_label = tk.Label(
    root,
    text="KLASİK MOD",
    font=("Arial", 12, "bold"),
    bg="#20242b",
    fg="#63c7ff"
)
mode_label.pack(pady=3)

angle_label = tk.Label(
    root,
    text="Açı: Derece",
    bg="#20242b",
    fg="#b8c4d1"
)
angle_label.pack()


# ---------------- GİRİŞ İŞLEMLERİ ----------------

def insert_text(value):
    global just_calculated, repeat_operator, repeat_operand

    if just_calculated:
        if value in ("+", "-", "*", "/", "%", "**"):
            repeat_operator = None
            repeat_operand = None
        else:
            display.delete(0, tk.END)
            repeat_operator = None
            repeat_operand = None

        just_calculated = False

    display.insert(tk.INSERT, value)
    display.focus_set()


def clear_display():
    global just_calculated, repeat_operator, repeat_operand

    display.delete(0, tk.END)
    just_calculated = False
    repeat_operator = None
    repeat_operand = None


def backspace():
    global just_calculated, repeat_operator, repeat_operand

    pos = display.index(tk.INSERT)

    if pos > 0:
        display.delete(pos - 1, pos)

    just_calculated = False
    repeat_operator = None
    repeat_operand = None


# ---------------- MOD GEÇİŞİ ----------------

def toggle_mode():
    global SCIENTIFIC_MODE

    SCIENTIFIC_MODE = not SCIENTIFIC_MODE

    if SCIENTIFIC_MODE:
        mode_label.config(text="BİLİMSEL MOD")
        mode_button.config(text="Klasik Moda Geç")
        scientific_frame.pack(
            fill="x",
            padx=10,
            pady=4,
            before=bottom_frame
        )
    else:
        mode_label.config(text="KLASİK MOD")
        mode_button.config(text="Bilimsel Moda Geç")
        scientific_frame.pack_forget()


def toggle_angle():
    global DEG_MODE

    DEG_MODE = not DEG_MODE
    angle_label.config(
        text="Açı: " + ("Derece" if DEG_MODE else "Radyan")
    )


# ---------------- HESAPLAMA VE TEKRAR ----------------

def calculate():
    global repeat_operator, repeat_operand, just_calculated

    expression = display.get().strip()

    if not expression:
        return

    try:
        if (
            just_calculated
            and repeat_operator is not None
            and repeat_operand is not None
        ):
            current = safe_eval(expression)

            if repeat_operator == "+":
                result = current + repeat_operand
            elif repeat_operator == "-":
                result = current - repeat_operand
            elif repeat_operator == "*":
                result = current * repeat_operand
            elif repeat_operator == "/":
                result = current / repeat_operand
            elif repeat_operator == "%":
                result = current % repeat_operand
            elif repeat_operator == "**":
                result = current ** repeat_operand
            else:
                result = current

        else:
            tree = ast.parse(expression, mode="eval")
            result = safe_eval(expression)

            repeat_operator = None
            repeat_operand = None
            body = tree.body

            if isinstance(body, ast.BinOp):
                op_map = {
                    ast.Add: "+",
                    ast.Sub: "-",
                    ast.Mult: "*",
                    ast.Div: "/",
                    ast.Mod: "%",
                    ast.Pow: "**",
                }

                repeat_operator = op_map.get(type(body.op))

                if repeat_operator is not None:
                    repeat_operand = safe_eval(
                        ast.unparse(body.right)
                    )

        formatted = format_result(result)

        history.append(f"{expression} = {formatted}")

        display.delete(0, tk.END)
        display.insert(0, formatted)
        display.icursor(tk.END)

        just_calculated = True

    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Hata")

        just_calculated = False
        repeat_operator = None
        repeat_operand = None


# ---------------- İŞLEM GEÇMİŞİ ----------------

def clear_history(box):
    history.clear()
    box.delete(0, tk.END)
    box.insert(tk.END, "Henüz işlem yapılmadı.")


def show_history():
    window = tk.Toplevel(root)
    window.title("İşlem Geçmişi")
    window.geometry("380x360")
    window.configure(bg="#20242b")

    box = tk.Listbox(
        window,
        font=("Arial", 11),
        bg="#303640",
        fg="white"
    )
    box.pack(fill="both", expand=True, padx=8, pady=8)

    if history:
        for item in history:
            box.insert(tk.END, item)
    else:
        box.insert(tk.END, "Henüz işlem yapılmadı.")

    button_frame = tk.Frame(window, bg="#20242b")
    button_frame.pack(fill="x", padx=8, pady=(0, 8))

    tk.Button(
        button_frame,
        text="Geçmişi Temizle",
        command=lambda: clear_history(box),
        bg="#b94343",
        fg="white",
        font=("Arial", 11, "bold"),
        relief="flat"
    ).pack(side="left", fill="x", expand=True, padx=3, ipady=4)

    tk.Button(
        button_frame,
        text="Kapat",
        command=window.destroy,
        bg="#596779",
        fg="white",
        font=("Arial", 11, "bold"),
        relief="flat"
    ).pack(side="left", fill="x", expand=True, padx=3, ipady=4)


# ---------------- MOD TUŞU ----------------

mode_button = tk.Button(
    root,
    text="Bilimsel Moda Geç",
    command=toggle_mode,
    font=("Arial", 12, "bold"),
    bg="#2878b5",
    fg="white",
    relief="flat"
)
mode_button.pack(fill="x", padx=12, pady=6, ipady=5)


# ---------------- KLASİK TUŞLAR ----------------

classic_frame = tk.Frame(root, bg="#20242b")
classic_frame.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=5
)

classic_buttons = [
    ("7", "7"), ("8", "8"), ("9", "9"), ("÷", "/"),
    ("4", "4"), ("5", "5"), ("6", "6"), ("×", "*"),
    ("1", "1"), ("2", "2"), ("3", "3"), ("−", "-"),
    ("0", "0"), (".", "."), ("%", "%"), ("+", "+"),
    ("(", "("), (")", ")"), ("π", "pi"), ("e", "e"),
]

for i, (label, value) in enumerate(classic_buttons):
    btn = tk.Button(
        classic_frame,
        text=label,
        font=("Arial", 15, "bold"),
        bg="#3a424e",
        fg="white",
        activebackground="#596779",
        relief="flat",
        command=lambda v=value: insert_text(v)
    )

    btn.grid(
        row=i // 4,
        column=i % 4,
        sticky="nsew",
        padx=3,
        pady=3,
        ipady=7
    )

for c in range(4):
    classic_frame.grid_columnconfigure(c, weight=1)

for r in range(5):
    classic_frame.grid_rowconfigure(r, weight=1)


# ---------------- BİLİMSEL TUŞLAR ----------------

scientific_frame = tk.Frame(root, bg="#20242b")

scientific_buttons = [
    ("sin", "sin("), ("cos", "cos("), ("tan", "tan("),
    ("√", "sqrt("), ("log", "log("), ("ln", "ln("),
    ("x²", "**2"), ("xʸ", "**"), ("n!", "factorial("),
    ("abs", "abs("), ("DEG/RAD", None), ("Geçmiş", None),
    ("⌫", None), ("C", None), ("", None),
]

for i, (label, value) in enumerate(scientific_buttons):
    if label == "DEG/RAD":
        command = toggle_angle
    elif label == "Geçmiş":
        command = show_history
    elif label == "⌫":
        command = backspace
    elif label == "C":
        command = clear_display
    elif label == "":
        continue
    else:
        command = lambda v=value: insert_text(v)

    btn = tk.Button(
        scientific_frame,
        text=label,
        font=("Arial", 12, "bold"),
        bg="#48576b",
        fg="white",
        activebackground="#647c99",
        relief="flat",
        command=command
    )

    btn.grid(
        row=i // 3,
        column=i % 3,
        sticky="nsew",
        padx=3,
        pady=3,
        ipady=6
    )

for c in range(3):
    scientific_frame.grid_columnconfigure(c, weight=1)

for r in range(5):
    scientific_frame.grid_rowconfigure(r, weight=1)


# ---------------- ALT TUŞLAR ----------------

bottom_frame = tk.Frame(root, bg="#20242b")
bottom_frame.pack(fill="x", padx=10, pady=8)

tk.Button(
    bottom_frame,
    text="C",
    command=clear_display,
    bg="#b94343",
    fg="white",
    font=("Arial", 13, "bold")
).pack(side="left", fill="x", expand=True, padx=3, ipady=5)

tk.Button(
    bottom_frame,
    text="⌫",
    command=backspace,
    bg="#596779",
    fg="white",
    font=("Arial", 13, "bold")
).pack(side="left", fill="x", expand=True, padx=3, ipady=5)

tk.Button(
    bottom_frame,
    text="Hesapla =",
    command=calculate,
    bg="#27875b",
    fg="white",
    font=("Arial", 13, "bold")
).pack(side="left", fill="x", expand=True, padx=3, ipady=5)


# ---------------- İMZA ----------------

footer = tk.Label(
    root,
    text="coded by 3jd3rh4ck3r",
    font=("Arial", 10, "italic", "bold"),
    bg="#20242b",
    fg="#8b98a8"
)
footer.pack(side="bottom", pady=7)


# ---------------- KLAVYE DESTEĞİ ----------------

display.bind("<Return>", lambda event: calculate())
display.bind("<Escape>", lambda event: clear_display())

root.mainloop()
