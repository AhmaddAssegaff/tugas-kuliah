import tkinter as tk
from tkinter import messagebox

def increment(a, b):
    return a + b

def decrement(a, b):
    return a - b

def multiple(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ZeroDivisionError
    return a / b

def calculate(operation):
    try:
        value_1 = float(entry_1.get())
        value_2 = float(entry_2.get())

        if operation == "add":
            result = increment(value_1, value_2)
        elif operation == "sub":
            result = decrement(value_1, value_2)
        elif operation == "mul":
            result = multiple(value_1, value_2)
        elif operation == "div":
            result = division(value_1, value_2)

        label_result.config(text=f"Hasil: {result}")

    except ValueError:
        messagebox.showerror("Input Error", "Masukkan angka yang valid!")
    except ZeroDivisionError:
        messagebox.showerror("Math Error", "Tidak bisa membagi dengan 0!")

root = tk.Tk()
root.title("Kalkulator Sederhana")
root.geometry("350x250")
root.resizable(False, False)

label_instruksi = tk.Label(root, text="Masukkan dua angka:", font=("Arial", 12))
label_instruksi.pack(pady=10)

entry_1 = tk.Entry(root, width=20, font=("Arial", 12))
entry_1.pack(pady=5)
entry_2 = tk.Entry(root, width=20, font=("Arial", 12))
entry_2.pack(pady=5)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

button_increment = tk.Button(frame_buttons, text="+", width=5, font=("Arial", 12), command=lambda: calculate("add"))
button_decrement = tk.Button(frame_buttons, text="-", width=5, font=("Arial", 12), command=lambda: calculate("sub"))
button_multiple  = tk.Button(frame_buttons, text="×", width=5, font=("Arial", 12), command=lambda: calculate("mul"))
button_division  = tk.Button(frame_buttons, text="÷", width=5, font=("Arial", 12), command=lambda: calculate("div"))

button_increment.grid(row=0, column=0, padx=5)
button_decrement.grid(row=0, column=1, padx=5)
button_multiple.grid(row=0, column=2, padx=5)
button_division.grid(row=0, column=3, padx=5)

label_result = tk.Label(root, text="", font=("Arial", 14), fg="blue")
label_result.pack(pady=10)

root.mainloop()
