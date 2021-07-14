CREATE TABLE users (
    password_hash VARCHAR(256),
    salt VARCHAR(64),
    email VARCHAR(64),
    code VARCHAR(64),
    CONSTRAINT id_pk PRIMARY KEY (email)
);  