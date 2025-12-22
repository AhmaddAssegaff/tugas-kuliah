import tkinter as tk
from page_raport import create_raport_page as raport_page
from page_cbt import create_cbt_page as cbt_page
from components.button import create_button

WIDTH = 1200
HEIGHT = 620

window = tk.Tk()
window.title("Aplikasi Pendaftaran PMB")
window.geometry(f"{WIDTH}x{HEIGHT}")
window.resizable(True, True)

container = tk.Frame(window)
container.place(x=0, y=0, width=WIDTH, height=HEIGHT)

def show_frame(frame):
    frame.tkraise()

def create_landing_page(parent):
    frame = tk.Frame(parent, bg="#F4F6F8")
    frame.place(x=0, y=0, width=WIDTH, height=HEIGHT)

    card = tk.Frame(frame, bg="white", padx=40, pady=40)
    card.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        card,
        text="Daftar Sebagai",
        font=("Segoe UI", 14),
        bg="white",
        fg="#555"
    ).pack()

    tk.Label(
        card,
        text="Mahasiswa Baru",
        font=("Segoe UI", 22, "bold"),
        bg="white",
        fg="#2563EB"
    ).pack(pady=20)

    create_button(
        card,
        "Daftar",
        command=lambda: show_frame(menu_page)
    ).pack(pady=10)

    create_button(
        card,
        "Keluar",
        command=window.destroy,
        bg="#E5E7EB",
        fg="#111",
        active_bg="#D1D5DB"
    ).pack()

    return frame

def create_menu_pmb_page(parent):
    frame = tk.Frame(parent, bg="#F4F6F8")
    frame.place(x=0, y=0, width=WIDTH, height=HEIGHT)

    card = tk.Frame(frame, bg="white", padx=40, pady=40)
    card.place(relx=0.5, rely=0.5, anchor="center")

    tk.Label(
        card,
        text="PENDAFTARAN MAHASISWA BARU",
        font=("Segoe UI", 18, "bold"),
        bg="white"
    ).pack()

    tk.Label(
        card,
        text="TAHUN AKADEMIK 2026/2027",
        font=("Segoe UI", 12),
        bg="white",
        fg="#666"
    ).pack(pady=10)

    create_button(
        card,
        "Jalur Tes CBT",
        width=35,
        command=lambda: show_frame(jalur_cbt)
    ).pack(pady=10)

    create_button(
        card,
        "Jalur Tes Rapor",
        width=35,
        command=lambda: show_frame(jalur_raport)
    ).pack(pady=10)

    create_button(
        card,
        "Kembali",
        width=20,
        bg="#E5E7EB",
        fg="#111",
        active_bg="#D1D5DB",
        font=("Segoe UI", 11),
        command=lambda: show_frame(login_page)
    ).pack(pady=20)

    return frame

login_page = create_landing_page(container)
menu_page = create_menu_pmb_page(container)

jalur_raport = raport_page(
    container,
    WIDTH,
    HEIGHT,
    on_back=lambda: show_frame(menu_page)
)

jalur_cbt = cbt_page(
    container,
    WIDTH,
    HEIGHT, 
    on_back=lambda: show_frame(menu_page)
)

show_frame(login_page)
window.mainloop()
