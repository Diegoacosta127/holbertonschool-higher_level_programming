# 0x0D. SQL - Introduction

## Install MySQL 8.0 on Ubuntu 20.04 LTS
~~~~
root@ubuntu:/# sudo apt update
root@ubuntu:/# sudo apt install mysql-server
...
root@ubuntu:/# mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
root@ubuntu:/# 
~~~~
Connect to your MySQL server:
~~~~
root@ubuntu:/# sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
root@ubuntu:/#
~~~~

## Use "container-on-demand" to run MySQL
**In the container, credentials are `root/root`**
* Ask for container `Ubuntu 20.04`
* Connect via SSH
* OR connect via the Web terminal
* In the container, you should start MySQL before playing with it:
~~~~
root@ubuntu:/# service mysql start
 * Starting MySQL database server mysqld
root@ubuntu:/# 
root@ubuntu:/# cat 0-list_databases.sql | mysql -uroot -p
Database
information_schema
mysql
performance_schema
sys
root@ubuntu:/# 
~~~~
