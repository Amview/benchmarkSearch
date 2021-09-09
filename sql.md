* passmark cpu多核表
```
create table passmark_manyCpu
(
    id     integer not null
        constraint passmark_manyCpu_pk
            primary key autoincrement,
    name   varchar(50) default null,
    scores varchar(20) default null
);
```
* passmark cpu单核表
```
create table passmark_singleCpu
(
    id     integer not null
        constraint passmark_manyCpu_pk
            primary key autoincrement,
    name   varchar(50) default null,
    scores varchar(20) default null
);
```
* passmark gpu表
```
create table passmarkGpu
(
    id     integer not null
        constraint passmark_manyCpu_pk
            primary key autoincrement,
    name   varchar(50) default null,
    scores varchar(20) default null
);
```
