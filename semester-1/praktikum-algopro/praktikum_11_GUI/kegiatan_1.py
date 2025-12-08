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

data_diri = tk.Label(root, text="Data Diri")
data_diri.pack(pady=1)

for key, value in data.items():
    result_label = tk.Label(root, text=f"{key}: {value}")
    result_label.pack(pady=1)


frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

button_tutup = tk.Button(frame_buttons, text="Close", width=5, font=("Arial", 12), command=root.quit)
button_tutup.grid(row=0, column=0, padx=5)

root.mainloop()
