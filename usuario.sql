CREATE USER 'urubu100'@'localhost' IDENTIFIED BY 'urubu100';
GRANT ALL PRIVILEGES ON * . * TO 'urubu100'@'localhost';
FLUSH PRIVILEGES;
create database algas;
use algas;
create table dados_aquario (sensor varchar(45),
ph decimal(3,2),
temperatura decimal(4,2),
turbidez decimal(4,2),
oxigenio decimal(3,2),
data_registro datetime);