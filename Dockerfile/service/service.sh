#!/bin/bash

# Mysql 5.7 root with password 123456
docker run --name mysql -p 3306:3306 --restart always -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci

# Mysql 5.7 root without password
docker run --name mysql -p 3306:3306 --restart always -e MYSQL_ALLOW_EMPTY_PASSWORD=yes  -d mysql:5.7 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci

# Mysql 5.7 with username libgo password 123456
docker run --name mysql -p 3306:3306 --restart always -e MYSQL_USER=libgo -e MYSQL_PASSWORD=123456 -d mysql:5.7 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci

# Tidb root with password 123456
docker run --name tidb -p 3306:4000 -p 10080:10080 --restart always -d pingcap/tidb:v3.0.1 -store tikv
mycli --port 3306 --user root
UPDATE mysql.user SET Password=PASSWORD('123456') WHERE User='root';
FLUSH PRIVILEGES;

# Redis latest
docker run --name redis -p 6379:6379  --restart always -d redis
