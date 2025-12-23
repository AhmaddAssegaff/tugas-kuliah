import tkinter as tk
from tkinter import ttk
from components.button import create_button
from tkinter import messagebox

def create_raport_page(parent, width, height, on_back):
    frame = tk.Frame(parent)
    frame.place(x=0, y=0, width=width, height=height)

    selected_item_id = None

    def simpan_data():
        nonlocal selected_item_id

        nama = entry_nama.get().strip()
        jurusan = daftar_jurusan.get().strip()
        alamat = entry_alamat.get().strip()
        sekolah = entry_sekolah.get().strip()
        bindo = entry_bindo.get().strip()
        bing = entry_bing.get().strip()
        mtk = entry_mtk.get().strip()

        if not nama:
            messagebox.showerror("Error", "Nama Lengkap wajib diisi!")
            return

        if not jurusan:
            messagebox.showerror("Error", "Jurusan wajib dipilih!")
            return

        if not alamat:
            messagebox.showerror("Error", "Alamat wajib diisi!")
            return

        if not sekolah:
            messagebox.showerror("Error", "Asal Sekolah wajib diisi!")
            return

        if not bindo or not bing or not mtk:
            messagebox.showerror("Error", "Semua nilai wajib diisi!")
            return

        try:
            bindo = float(bindo)
            bing = float(bing)
            mtk = float(mtk)
        except ValueError:
            messagebox.showerror("Error", "Nilai harus berupa angka!")
            return

        for nilai, nama_mapel in [
            (bindo, "Bahasa Indonesia"),
            (bing, "Bahasa Inggris"),
            (mtk, "Matematika")
        ]:
            if nilai < 0 or nilai > 100:
                messagebox.showerror(
                    "Error",
                    f"Nilai {nama_mapel} harus antara 0 - 100!"
                )
                return

        if selected_item_id:
            no = tabel.item(selected_item_id)["values"][0]
            tabel.item(
                selected_item_id,
                values=(no, nama, jurusan, alamat, sekolah, bindo, bing, mtk)
            )
        else:
            no = len(tabel.get_children()) + 1
            tabel.insert(
                "",
                "end",
                values=(no, nama, jurusan, alamat, sekolah, bindo, bing, mtk)
            )

        messagebox.showinfo("Sukses", "Data berhasil disimpan!")
        reset_form()


    def hapus_data():
        nonlocal selected_item_id

        if not selected_item_id:
            messagebox.showwarning("Peringatan", "Pilih data yang ingin dihapus!")
            return

        if not messagebox.askyesno("Konfirmasi", "Yakin ingin menghapus data ini?"):
            return

        tabel.delete(selected_item_id)
        reset_form()

        for i, item in enumerate(tabel.get_children(), start=1):
            tabel.set(item, "No", i)

    def pilih_data(event):
        nonlocal selected_item_id

        selected = tabel.selection()
        if not selected:
            return

        selected_item_id = selected[0]
        data = tabel.item(selected_item_id, "values")

        reset_form(clear_selection=False)

        entry_nama.insert(0, data[1])
        daftar_jurusan.set(data[2])
        entry_alamat.insert(0, data[3])
        entry_sekolah.insert(0, data[4])
        entry_bindo.insert(0, data[5])
        entry_bing.insert(0, data[6])
        entry_mtk.insert(0, data[7])

    def reset_form(clear_selection=True):
        nonlocal selected_item_id

        entry_nama.delete(0, tk.END)
        daftar_jurusan.set("")
        entry_alamat.delete(0, tk.END)
        entry_sekolah.delete(0, tk.END)
        entry_bindo.delete(0, tk.END)
        entry_bing.delete(0, tk.END)
        entry_mtk.delete(0, tk.END)

        if clear_selection:
            selected_item_id = None
            tabel.selection_remove(tabel.selection())

    frame_input = tk.LabelFrame(
        frame,
        text="Data Diri Calon Mahasiswa (Jalur Rapor)",
        padx=15,
        pady=15
    )
    frame_input.pack(fill="x", padx=20, pady=15)

    def label(text, row):
        tk.Label(frame_input, text=text).grid(row=row, column=0, sticky="w")

    def entry(row):
        e = tk.Entry(frame_input, width=40)
        e.grid(row=row, column=1, padx=8, pady=4)
        return e

    label("Nama Lengkap", 0)
    entry_nama = entry(0)

    label("Jurusan", 1)
    daftar_jurusan = ttk.Combobox(
        frame_input,
        width=38,
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
    daftar_jurusan.grid(row=1, column=1, padx=8, pady=4)

    label("Alamat", 2)
    entry_alamat = entry(2)

    label("Asal Sekolah", 3)
    entry_sekolah = entry(3)

    label("Nilai Bahasa Indonesia", 4)
    entry_bindo = entry(4)

    label("Nilai Bahasa Inggris", 5)
    entry_bing = entry(5)

    label("Nilai Matematika", 6)
    entry_mtk = entry(6)

    frame_action = tk.Frame(frame_input)
    frame_action.grid(row=7, column=0, columnspan=2, pady=15)

    create_button(
        frame_action,
        "Reset",
        command=reset_form,
        width=18,
        bg="#F59E0B"
    ).pack(side="left", padx=5)

    create_button(frame_action, "Simpan", command=simpan_data, width=18).pack(side="left", padx=5)
    create_button(frame_action, "Hapus", command=hapus_data, width=18, bg="#EF4444").pack(side="left", padx=5)
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
        columns=(
            "No",
            "Nama",
            "Jurusan",
            "Alamat",
            "Asal Sekolah",
            "B. Indo",
            "B. Inggris",
            "MTK"
        ),
        show="headings"
    )

    for col in (
        "No", "Nama", "Jurusan", "Alamat",
        "Asal Sekolah", "B. Indo", "B. Inggris", "MTK"
    ):
        tabel.heading(col, text=col)
        tabel.column(col, anchor="center", width=110)

    tabel.pack(fill="both", expand=True)
    tabel.bind("<<TreeviewSelect>>", pilih_data)

    return frame
