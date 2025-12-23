import tkinter as tk
from tkinter import ttk, messagebox
from components.button import create_button


def create_cbt_page(parent, width, height, on_back):
    frame = tk.Frame(parent)
    frame.place(x=0, y=0, width=width, height=height)

    header = tk.Label(
        frame,
        text="FORMULIR PENDAFTARAN\nKuliah Jalur Tes",
        font=("Arial", 16, "bold"),
        bg="#2563EB",
        fg="white",
        pady=15
    )
    header.pack(fill="x")

    form_frame = tk.Frame(frame, bg="#F3F4F6")
    form_frame.pack(pady=20, padx=30, fill="both", expand=True)

    def label(text, row):
        tk.Label(
            form_frame,
            text=text,
            font=("Arial", 10),
            bg="#F3F4F6",
            anchor="w"
        ).grid(row=row, column=0, sticky="w", pady=(10, 2))

    def entry(row):
        e = tk.Entry(
            form_frame,
            font=("Arial", 10),
            relief="solid",
            borderwidth=1
        )
        e.grid(row=row, column=0, sticky="ew", pady=(0, 5))
        return e

    label("Nama Lengkap", 0)
    input_nama = entry(1)

    label("NIK", 2)
    input_nik = entry(3)

    label("Asal Sekolah", 4)
    input_sekolah = entry(5)

    label("Jurusan", 6)
    daftar_jurusan = ttk.Combobox(
        form_frame,
        state="readonly",
        values=(
            "Teknik Informatika",
            "Sistem Informasi",
            "Teknik Elektro",
            "Artificial Intelligence",
            "Desain Grafis",
            "Aktuaria",
            "Bisnis Digital"
        )
    )
    daftar_jurusan.grid(row=7, column=0, sticky="ew", pady=(0, 5))

    label("Nomor WhatsApp / Email", 8)
    input_kontak = entry(9)

    form_frame.columnconfigure(0, weight=1)

    def submit_registration():
        fields = {
            "Nama Lengkap": input_nama.get().strip(),
            "NIK": input_nik.get().strip(),
            "Asal Sekolah": input_sekolah.get().strip(),
            "Jurusan": daftar_jurusan.get(),
            "Nomor WhatsApp / Email": input_kontak.get().strip()
        }

        for field, value in fields.items():
            if not value:
                messagebox.showwarning(
                    "Peringatan",
                    f"{field} tidak boleh kosong!"
                )
                return

        messagebox.showinfo(
            "Pendaftaran Berhasil",
            f"Selamat, {input_nama.get()}!\n\n"
            f"Pendaftaran Anda berhasil pada prodi {daftar_jurusan.get()}.\n\n"
            "JADWAL UJIAN:\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Tanggal : 5 Januari 2025\n"
            "Waktu   : 08.00 - 10.00 WIB\n"
            "Tempat  : Online (CBT)\n"
            "Link    : www.ujian-kampus.ac.id\n\n"
            f"Informasi akan dikirim melalui:\n{input_kontak.get()}\n\n"
            "Terima kasih!"
        )

        input_nama.delete(0, tk.END)
        input_nik.delete(0, tk.END)
        input_sekolah.delete(0, tk.END)
        daftar_jurusan.set("")
        input_kontak.delete(0, tk.END)

    button_frame = tk.Frame(frame, bg="#F3F4F6")
    button_frame.pack(fill="x", padx=30, pady=15)

    button_frame.columnconfigure(0, weight=1)
    button_frame.columnconfigure(1, weight=1)

    create_button(
        button_frame,
        "← Kembali",
        command=on_back,
        width=18,
        bg="#E5E7EB",
        fg="#111827",
        active_bg="#D1D5DB"
    ).grid(row=0, column=0, sticky="w")

    create_button(
        button_frame,
        "DAFTAR SEKARANG",
        command=submit_registration,
        width=22,
        bg="#2563EB",
        fg="white",
        active_bg="#1D4ED8"
    ).grid(row=0, column=1, sticky="e")

    tk.Label(
        frame,
        text="* Semua field wajib diisi",
        font=("Arial", 8, "italic"),
        bg="#F3F4F6"
    ).pack(pady=(0, 10))

    return frame
