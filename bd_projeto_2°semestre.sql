create database magnasync_rm;
use magnasync_rm;

create table usuario (
id_usuario int primary key auto_increment,
nome varchar(45) not null,
nome_social varchar(45),
email varchar(45) not null,
telefone int not null,
cpf char(11) not null,
cargo varchar(45)
);

create table hospital (
id_hospital int primary key auto_increment,
id_usuario int not null,
nome varchar(100) not null,
cnpj char(14),
cep char(9),
rua varchar(45),
cidade varchar(45),
estado char(2),
telefone varchar(45),
constraint fk_usuario foreign key (id_usuario)
references usuario(id_usuario)
);

create table equipamento (
id_equipamento int primary key auto_increment,
id_hospital int not null,
modelo varchar(100) not null,
fabricante varchar(60),
numero_serie varchar(60),
sistema_operacional varchar(60),
status_atual varchar(45),
data_instalacao date,
constraint fk_hospital foreign key (id_hospital) 
references hospital(id_hospital)
);

create table registroCpu (
id_cpu int primary key auto_increment,
id_equipamento int not null,
percentual_uso decimal(5,2),
frequencia decimal(10,2),
nucleos int,
data_hora datetime not null,
constraint fk_equipamento foreign key (id_equipamento)
references equipamento(id_equipamento)
);

create table registroRam (
id_ram int primary key auto_increment,
id_equipamento int not null,
percentual_uso decimal(5,2),
memoria_total decimal(10,2),
memoria_disponivel decimal(10,2),
data_hora datetime not null,
constraint fk_equipamento2 foreign key (id_equipamento)
references equipamento(id_equipamento)
);

create table registroArmazenamento(
id_armazenamento int primary key auto_increment,
id_equipamento int not null,
percentual_uso decimal(5,2),
espaco_total decimal(10,2),
espaco_disponivel decimal(10,2),
data_hora datetime not null,
constraint fk_equipamento3 foreign key (id_equipamento)
references equipamento(id_equipamento)
);

create table alerta (
id_alerta int primary key auto_increment,
id_equipamento int not null,
tipo varchar(50) not null,
descricao varchar(255),
valor_atual decimal(10,2),
limite decimal(10,2),
data_hora datetime not null,
status_atual varchar(20),
constraint fk_equipamento4 foreign key (id_equipamento)
references equipamento(id_equipamento)
);
