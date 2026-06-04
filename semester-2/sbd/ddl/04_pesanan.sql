CREATE TABLE pesanan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_pelanggan INT NOT NULL,
    status_pesanan BOOLEAN NOT NULL DEFAULT FALSE,
    pesanan_dibuat DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    metode_pembayaran ENUM("CASH", "QRIS", "TRANSFER") NOT NULL,
    total_harga INT NOT NULL,

    CONSTRAINT fk_pesanan_pelanggan 
        FOREIGN KEY (id_pelanggan) REFERENCES pelanggan(id) 
        ON DELETE RESTRICT ON UPDATE CASCADE
);
