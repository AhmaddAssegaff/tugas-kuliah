import tkinter as tk
from tkinter import ttk
from components.button import create_button

def create_raport_page(parent, width, height, on_back):
    frame = tk.Frame(parent)
    frame.place(x=0, y=0, width=width, height=height)

    selected_item_id = {"id": None}

    def reset_form():
        entry_nama.delete(0, tk.END)
        daftar_jurusan.set("")
        entry_alamat.delete(0, tk.END)
        entry_sekolah.delete(0, tk.END)
        selected_item_id["id"] = None

    def simpan_data():
        nama = entry_nama.get()
        jurusan = daftar_jurusan.get()
        alamat = entry_alamat.get()
        sekolah = entry_sekolah.get()

        if not nama or not jurusan:
            return

        if selected_item_id["id"]:
            no = tabel.item(selected_item_id["id"])["values"][0]
            tabel.item(
                selected_item_id["id"],
                values=(no, nama, jurusan, alamat, sekolah)
            )
        else:
            no = len(tabel.get_children()) + 1
            tabel.insert(
                "",
                "end",
                values=(no, nama, jurusan, alamat, sekolah)
            )

        reset_form()

    def pilih_data(event):
        selected_item_id["id"] = tabel.focus()
        if not selected_item_id["id"]:
            return

        data = tabel.item(selected_item_id["id"], "values")
        reset_form()

        entry_nama.insert(0, data[1])
        daftar_jurusan.set(data[2])
        entry_alamat.insert(0, data[3])
        entry_sekolah.insert(0, data[4])

    def hapus_data():
        if not selected_item_id["id"]:
            return

        tabel.delete(selected_item_id["id"])
        reset_form()

        for i, item in enumerate(tabel.get_children(), start=1):
            tabel.set(item, "No", i)

    frame_input = tk.LabelFrame(
        frame,
        text="Data Diri Calon Mahasiswa (Jalur Rapor)",
        padx=15,
        pady=15
    )
    frame_input.pack(fill="x", padx=20, pady=15)

    tk.Label(frame_input, text="Nama Lengkap").grid(row=0, column=0, sticky="w")
    entry_nama = tk.Entry(frame_input, width=40)
    entry_nama.grid(row=0, column=1, padx=8, pady=4)

    tk.Label(frame_input, text="Jurusan").grid(row=1, column=0, sticky="w")
    daftar_jurusan = ttk.Combobox(frame_input, width=38, state="readonly")
    daftar_jurusan["values"] = (
        "Teknik Informatika",
        "Sistem Informasi",
        "Teknik Elektro",
        "Artificial Intelligence",
        "Desain Grafis",
        "Aktuaria",
        "Bisnis Digital"
    )
    daftar_jurusan.grid(row=1, column=1, padx=8, pady=4)

    tk.Label(frame_input, text="Alamat").grid(row=2, column=0, sticky="w")
    entry_alamat = tk.Entry(frame_input, width=40)
    entry_alamat.grid(row=2, column=1, padx=8, pady=4)

    tk.Label(frame_input, text="Asal Sekolah").grid(row=3, column=0, sticky="w")
    entry_sekolah = tk.Entry(frame_input, width=40)
    entry_sekolah.grid(row=3, column=1, padx=8, pady=4)

    frame_action = tk.Frame(frame_input)
    frame_action.grid(row=4, column=0, columnspan=2, pady=15)

    create_button(
        frame_action,
        "Simpan",
        command=simpan_data,
        width=18
    ).pack(side="left", padx=5)

    create_button(
        frame_action,
        "Hapus",
        command=hapus_data,
        width=18,
        bg="#EF4444"
    ).pack(side="left", padx=5)

    create_button(
        frame_action,
        "Kembali",
        command=on_back,
        width=18,
        bg="#E5E7EB",
        fg="#111",
        active_bg="#D1D5DB"
    ).pack(side="left", padx=5)

    frame_tabel = tk.LabelFrame(frame, text="Daftar Pendaftar")
    frame_tabel.pack(fill="both", expand=True, padx=20, pady=10)

    tabel = ttk.Treeview(
        frame_tabel,
        columns=("No", "Nama", "Jurusan", "Alamat", "Asal Sekolah"),
        show="headings"
    )

    for col in ("No", "Nama", "Jurusan", "Alamat", "Asal Sekolah"):
        tabel.heading(col, text=col)
        tabel.column(col, anchor="center")

    tabel.pack(fill="both", expand=True)
    tabel.bind("<<TreeviewSelect>>", pilih_data)

    return frame
