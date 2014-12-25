drop table if exists entries;
create table entry (
  id integer primary key autoincrement,
  latitud integer not null,
  longitud integer not null,
  description text not null,
  user text not null
);
insert into entry (latitud,longitud,description,user) values ('-39.80682059999999', '-73.25894360000001','11111','sean');
insert into entry (latitud,longitud,description,user) values ('-39.8338098', '-73.25165549999997','11111','sean');
insert into entry (latitud,longitud,description,user) values ('-39.8347538', '-73.2327482','11111','sean');
