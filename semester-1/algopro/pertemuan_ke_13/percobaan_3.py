import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("apps GUI")
window.geometry("300x200")

Nama = tk.StringVar()
NIM = tk.StringVar()
Alamat = tk.StringVar()

tk.Label(window, text="Nama").grid(row=0, column=0, sticky="w", padx=10, pady=5)
tk.Label(window, text="NIM").grid(row=1, column=0, sticky="w", padx=10, pady=5)
tk.Label(window, text="Alamat").grid(row=2, column=0, sticky="w", padx=10, pady=5)

tk.Entry(window, textvariable=Nama).grid(row=0, column=1, padx=10)
tk.Entry(window, textvariable=NIM).grid(row=1, column=1, padx=10)
tk.Entry(window, textvariable=Alamat).grid(row=2, column=1, padx=10)

def SIMPAN_DATA():
    if Nama.get() == "" and NIM.get() == "" and Alamat.get() == "":
        messagebox.showinfo("form kosong tidak dapat di kirim")
    else:
        hasil = f"""
                Nama   : {Nama.get()}
                NIM    : {NIM.get()}
                Alamat : {Alamat.get()}
                """
        messagebox.showinfo("Data Tersimpan", hasil)

tk.Button(window, text="Simpan", command=SIMPAN_DATA).grid(row=3, column=1, pady=10)
window.mainloop()
