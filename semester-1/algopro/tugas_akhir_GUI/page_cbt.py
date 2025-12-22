import tkinter as tk
from components.button import create_button

def create_cbt_page(parent, width, height, on_back):
    frame = tk.Frame(parent)
    frame.place(x=0, y=0, width=width, height=height)

    tk.Label(
        frame,
        text="Halaman CBT (Coming Soon)",
        font=("Segoe UI", 20)
    ).pack(expand=True)

    create_button(
        frame,
        "Kembali",
        command=on_back,
        width=18,
        bg="#E5E7EB",
        fg="#111",
        active_bg="#D1D5DB"
    ).pack(side="left", padx=5)

    return frame
