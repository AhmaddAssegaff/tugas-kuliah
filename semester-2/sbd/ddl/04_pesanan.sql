CREATE TABLE pesanan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_pelanggan INT NOT NULL,
    status_pesanan BOOLEAN NOT NULL DEFAULT FALSE,
    pesanan_dibuat DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    metode_pembayaran VARCHAR(50) NOT NULL,
    total_harga BIGINT NOT NULL,

    CONSTRAINT fk_pesanan_pelanggan 
        FOREIGN KEY (id_pelanggan) REFERENCES pelanggan(id) 
        ON DELETE RESTRICT ON UPDATE CASCADE
);
