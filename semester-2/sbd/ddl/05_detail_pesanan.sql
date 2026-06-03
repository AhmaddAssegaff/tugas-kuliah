CREATE TABLE detail_pesanan (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_pesanan INT NOT NULL,
    id_menu INT NOT NULL,
    kuantitas INT NOT NULL,
    sub_total INT NOT NULL,
    harga_menu_saat_pesan INT NOT NULL,

    CONSTRAINT fk_detail_pesanan_pesanan 
        FOREIGN KEY (id_pesanan) REFERENCES pesanan(id) 
        ON DELETE CASCADE ON UPDATE CASCADE,

    CONSTRAINT fk_detail_pesanan_menu 
        FOREIGN KEY (id_menu) REFERENCES menu(id) 
        ON DELETE RESTRICT ON UPDATE CASCADE
);
