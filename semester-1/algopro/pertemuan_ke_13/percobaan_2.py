import tkinter as tk

window = tk.Tk()
window.title("apps GUI")
window.geometry("300x200")

label = tk.Label(window, text="test")
label.pack()

button = tk.Button(window, command=window.destroy, text="exit")
button.pack()

window.mainloop()
