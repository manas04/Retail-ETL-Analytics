create table train(
date DAte,
store_nbr int,
family text,
sales numeric,
onpromotion int);


create table stores(
store_nbr int, 
city text,
state text,
type text,
cluster int);


create table transactions(
date date,
store_nbr int,
transactions int);




