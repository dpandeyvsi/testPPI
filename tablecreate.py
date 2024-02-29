'''
CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


insert into user(username,password) values ('Deepak','$2b$12$Q1PAge7c/46wdY33smvRwezrDOKwPyVBuunaJj6KhfR6fqeKoezqe');

'''
