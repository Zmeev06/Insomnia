create database if not exists chats

CREATE TABLE users(
    ID int not None,
    username varchar(100),
    user_first_name varchar(100),
    age int(100) not None,
    cash int,
    date_mes date,
    pet varchar
);
