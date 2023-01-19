import sqlite3
con=sqlite3.Connection('bus_database_new')
cur=con.cursor()
##cur.execute(''' CREATE TABLE operator
##( operator_id INTEGER,
##  name VARCHAR NOT NULL,
##  address VARCHAR,
##  email varchar,
## phone integer,
##  CONSTRAINT operator_id_pk PRIMARY KEY (operator_id)
##); ''')
##data1= """INSERT INTO operator
##                 (operator_id, name,address, email, phone) 
##                           VALUES 
##                      (1,'ram_travel','51b complex guna','ram_travel@gmail.com',1234567890)"""

##cur.execute(''' CREATE TABLE bus
##( bus_id INTEGER,
##  bus_type VARCHAR,
##  capacity integer,
##  fare_amount integer,
## start text,
## end text,
## route_id varchar,
## operator_id varchar,
## 
##
##   CONSTRAINT operator_id_fk
##    FOREIGN KEY (operator_id)
##    REFERENCES operator (operator_id)
##); ''')


##cur.execute(''' CREATE TABLE runs
##( bus_id INTEGER,
##  date text,
##  seat_available integer,
##CONSTRAINT runs_pk PRIMARY KEY (bus_id,date)
## 
##
##); ''')


##cur.execute(''' CREATE TABLE route
##( route_id INTEGER,
##  station_id integer,
##  station_name text,
##CONSTRAINT route_id_pk PRIMARY KEY (route_id,station_id)
## 
##
##); ''')


con.commit()
con.close()
