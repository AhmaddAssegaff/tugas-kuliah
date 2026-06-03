from db import get_cursor


def ambil_pelanggan():
    cursor = get_cursor()

    query = """
    SELECT
        id,
        nama,
        alamat,
        no_hp
    FROM pelanggan
    """

    cursor.execute(query)

    result = cursor.fetchall()

    cursor.close()

    return result


def ambil_pesanan_pelanggan(id_pelanggan):
    cursor = get_cursor()

    query = """
    SELECT
        p.id AS pelanggan_id,
        p.nama AS nama_pelanggan,

        pm.id AS pesanan_id,
        pm.status_pesanan,
        pm.pesanan_dibuat,
        pm.metode_pembayaran,
        pm.total_harga,

        u.rating,
        u.komentar
    FROM pelanggan p
    JOIN pemesanan pm
        ON p.id = pm.id_pelanggan
    LEFT JOIN ulasan u
        ON pm.id = u.id_pesanan
    WHERE p.id = %s
    ORDER BY pm.pesanan_dibuat DESC
    """

    cursor.execute(query, (id_pelanggan,))

    result = cursor.fetchall()

    cursor.close()

    return result


def ambil_kurir():
    cursor = get_cursor()
    q = """
    SELECT 
        id,
        nama,
        CASE
            WHEN status_ketersediaan = 1 THEN 'Tersedia'
            ELSE 'Tidak Tersedia'
        END AS status_ketersediaan,
        kendaraan
    FROM kurir;
    """

    cursor.execute(q)
    result = cursor.fetchall()
    cursor.close()

    return result
