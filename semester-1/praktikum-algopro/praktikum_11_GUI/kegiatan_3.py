import tkinter as tk
from tkinter import messagebox

def calculate_persegi(a):
    return a * a

def calculate():
    try:
        value = float(entry_angka.get())
        result = calculate_persegi(value)
        label_hasil.config(text=f"Hasil persegi dari {value} = {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan angka yang valid!")

root = tk.Tk()
root.title("Kalkulator Persegi")
root.geometry("350x200")
root.resizable(False, False)

frame_input = tk.Frame(root)
frame_input.pack(pady=20)

label_instruksi = tk.Label(frame_input, text="Masukkan angka untuk menghitung persegi:")
label_instruksi.pack(pady=5)

entry_angka = tk.Entry(frame_input, width=25)
entry_angka.pack(pady=5)
entry_angka.focus()

button_hitung = tk.Button(frame_input, text="Hitung", width=15, command=calculate)
button_hitung.pack(pady=5)

label_hasil = tk.Label(root, text="", font=("Arial", 12))
label_hasil.pack(pady=10)

root.mainloop()
