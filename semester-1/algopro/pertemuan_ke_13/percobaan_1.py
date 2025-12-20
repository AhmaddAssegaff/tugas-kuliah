import tkinter as tk

window = tk.Tk()
window.title("apps GUI")
window.geometry("300x200")

label = tk.Label(window, text="test")
label.pack()

def TOMBOL_DI_KLIK():
   print("test") 

button = tk.Button(window, command=TOMBOL_DI_KLIK, text="tekan saya")
button.pack()

window.mainloop()
