CREATE DATABASE todo_list;

USE todo_list;

CREATE TABLE task (
    id SERIAL,
    name VARCHAR(255),
    PRIMARY KEY(id)
);

GRANT ALL PRIVILEGES ON todo_list.* TO 'mariadb';