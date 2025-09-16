import tkinter as tk

def increment(a,b):
    return a + b

def decrement(a,b):
    return a - b

def multiple(a,b):
    return a * b

def division(a,b):
    return a / b

root = tk.Tk()
root.title("Hello GUI")
root.geometry("300x200")

result_label = tk.Label(root, text="Halo, ini GUI pakai Tkinter!")
result_label.pack(pady=20) 

entry_1 = tk.Entry(root, width=30)
entry_1.pack(pady=5)

entry_2 = tk.Entry(root, width=30)
entry_2.pack(pady=5)

def calculate(opration):
    try:
        value_1 = float(entry_1.get())
        value_2 = float(entry_2.get())

        if opration == "add":
            result = increment(value_1, value_2)
        elif opration == "sub":
            result = decrement(value_1, value_2)
        elif opration == "mul":
            result = multiple(value_1, value_2)
        elif opration == "div":
            result = division(value_1, value_2)
        
        result_label.config(text=f"Hasil : {result}")

    except ValueError:
        result_label.config(text="error value")

button_increment = tk.Button(root, text="+", width=10, command=lambda: calculate("add"))
button_decrement = tk.Button(root, text="-", width=10, command=lambda: calculate("sub"))
button_multiple  = tk.Button(root, text="×", width=10, command=lambda: calculate("mul"))
button_division  = tk.Button(root, text="÷", width=10, command=lambda: calculate("div"))

button_increment.pack(pady=2)
button_decrement.pack(pady=2)
button_multiple.pack(pady=2)
button_division.pack(pady=2)

root.mainloop()
