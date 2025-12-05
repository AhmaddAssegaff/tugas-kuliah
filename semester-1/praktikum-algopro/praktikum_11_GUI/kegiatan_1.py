import tkinter as tk

data = {
    'nama': 'Ahmad',
    'NIM': 'L200250034',
    'Buku Favorit': 'buku apalah',
    'Motto': 'motto'
}

root = tk.Tk()
root.title("Hello GUI")
root.geometry("300x200")

for key, value in data.items():
    result_label = tk.Label(root, text=f"{key}: {value}")
    result_label.pack(pady=1)

root.mainloop()
