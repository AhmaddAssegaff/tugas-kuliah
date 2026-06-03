create table ulasan (
    id int auto_increment primary key,
    id_pesanan INT NOT NULL,
    rating INT NOT NULL,
    komentar TEXT NOT NULL,

    constraint fk_ulasan_pesanan 
        foreign key (id_pesanan) references pesanan(id) 
        on delete cascade on update cascade

    CONSTRAINT check_ulasan_rating 
            CHECK (rating >= 1 AND rating <= 5)
);
