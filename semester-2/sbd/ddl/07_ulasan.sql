create table ulasan (
    id int auto_increment primary key,
    id_pesanan int not null,
    rating int not null,
    komentar text,

    constraint fk_ulasan_pesanan 
        foreign key (id_pesanan) references pesanan(id) 
        on delete cascade on update cascade

    CONSTRAINT check_ulasan_rating 
            CHECK (rating >= 1 AND rating <= 5)
);
