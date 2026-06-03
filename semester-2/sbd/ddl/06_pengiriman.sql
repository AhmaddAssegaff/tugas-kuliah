CREATE TABLE pengiriman (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_pesanan INT NOT NULL,
    id_kurir INT NOT NULL,
    pengiriman_selesai DATETIME,
    status Enum("dikirim", "selesai dikirim") NOT NULL DEFAULT "dikirim",

    CONSTRAINT fk_pengiriman_pesanan 
        FOREIGN KEY (id_pesanan) REFERENCES pesanan(id) 
        ON DELETE CASCADE ON UPDATE CASCADE,

    CONSTRAINT fk_pengiriman_kurir 
        FOREIGN KEY (id_kurir) REFERENCES kurir(id) 
        ON DELETE RESTRICT ON UPDATE CASCADE
);
