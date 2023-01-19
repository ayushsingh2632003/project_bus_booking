import sqlite3
con=sqlite3.Connection('bus_database_new')
cur=con.cursor()
#cur.execute(''' CREATE TABLE operator
#( operator_id INTEGER,
  #name VARCHAR NOT NULL,
  #address VARCHAR,
 # email varchar,
 # phone integer,
  #CONSTRAINT operator_id_pk PRIMARY KEY (operator_id)
#); ''')
#data1= """INSERT INTO operator
  #                        (operator_id, name,address, email, phone) 
    #                       VALUES 
      #                    (1,'ram_travel','51b complex guna','ram_travel@gmail.com',1234567890)"""
#cur.execute(data1)
#data2= """INSERT INTO operator
##                          (operator_id, name,address, email, phone) 
##                           VALUES 
##                          (2,'shyam_travel','51c complex guna','shyam_travel@gmail.com',9876543210)"""

##cur.execute(data2)


##data3= """INSERT INTO operator
##                     (operator_id, name,address, email, phone) 
##                           VALUES 
##                          (3,'mohan_travel','51d complex guna','mohan_travel@gmail.com',9898989898)"""
##
##
##
##cur.execute(data3)

##data4= """INSERT INTO operator
##                     (operator_id, name,address, email, phone) 
##                           VALUES 
##                          (4,'bansi_travel','51e complex guna','bansi_travel@gmail.com',99999888888)"""
##
##
##
##cur.execute(data4)
##data5= """INSERT INTO operator
##                     (operator_id, name,address, email, phone) 
##                           VALUES 
##                          (5,'krishna_travel','51f complex guna','krishna_travel@gmail.com',8888899999)"""
##
##
##
##cur.execute(data5)


