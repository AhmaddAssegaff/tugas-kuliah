create table ulasan (
    id int auto_increment primary key,
    id_pesanan INT NOT NULL UNIQUE,
    rating INT NOT NULL,
    komentar TEXT NOT NULL,

    CONSTRAINT fk_ulasan_pesanan 
        FOREIGN  KEY (id_pesanan) REFERENCES  pesanan(id) 
        ON DELETE cascade
        ON UPDATE cascade,

    CONSTRAINT check_ulasan_rating 
            CHECK (rating >= 1 AND rating <= 5)
);
