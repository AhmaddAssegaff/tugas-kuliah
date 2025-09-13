import tkinter as tk

root = tk.Tk()
root.title("Hello GUI")
root.geometry("300x200")

label = tk.Label(root, text="Halo, ini GUI pakai Tkinter!")
label.pack(pady=20)

button = tk.Button(root, text="Klik Saya", command=lambda: print("Tombol diklik"))
button.pack()

root.mainloop()
