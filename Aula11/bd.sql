create database db_atv;

use db_atv;

create table tb_leds(
	id int auto_increment primary key,
    ledCor  varchar(20),
    dataCriacao datetime default now()
);