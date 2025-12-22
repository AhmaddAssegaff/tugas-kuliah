import tkinter as tk

def create_button(
    parent,
    text,
    command,
    width=18,
    bg="#2563EB",
    fg="white",
    active_bg="#1E40AF",
    font=("Segoe UI", 11, "bold"),
    pady=8
):
    return tk.Button(
        parent,
        text=text,
        command=command,
        font=font,
        bg=bg,
        fg=fg,
        activebackground=active_bg,
        activeforeground=fg,
        width=width,
        bd=0,
        padx=10,
        pady=pady
    )
