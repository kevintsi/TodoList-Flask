FROM mariadb:10.10.1-rc-jammy

COPY ./create.sql ./docker-entrypoint-initdb.d/

ENV MARIADB_ROOT_PASSWORD=P@ssW0rd
ENV MARIADB_USER=mariadb
ENV MARIADB_PASSWORD=password


