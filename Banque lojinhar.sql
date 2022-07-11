create database lojinha;
use lojinha;

create table Storag(
Cod int auto_increment,
FactoryCode int,
primary key (Cod, FactoryCode),
descriptionn varchar(100),
unit int,
price  float
);

create table Factory(
cod int auto_increment,
primary key (cod),
namee varchar(100),
descPro varchar(100)
);

create table Sell(
IDs int auto_increment,
CodP int,
primary key (IDs,CodP),
foreign key (CodP) references Storag(Cod)
);

create table Buy(
IDb int auto_increment,
CodP int,
primary key (IDb,CodP),
foreign key (CodP) references Storag(Cod)
);

#____________________________________________________#

create table HistoryT(
IDbb int,
IDss int,
datar datetime,
describ varchar(100),
CodP int,
primary key (IDbb,IDss,CodP),
foreign key (IDbb) references Buy(IDb),
foreign key (IDss) references Sell(IDs),
foreign key (CodP) references Storag(Cod)
);

create table HistoryB(
IDba int,
dater datetime,
describ varchar(100),
CodP int,
primary key(IDba,CodP),
foreign key (IDba) references Buy(IDb),
foreign key (CodP) references Storag(Cod)
);

create table HistoryS(
IDsa int,
daters datetime,
describr varchar(100),
CodP int,
primary key (IDsa,CodP),
foreign key (IDsa) references Sell(IDs),
foreign key (CodP) references Storag(Cod)
);

alter table Storag
add foreign key (FactoryCode) references Factory(cod);

select * from Storag;

