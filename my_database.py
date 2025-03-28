import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)


mycursor = mydb.cursor()
# általunk létrehozott adatbázis
DATABASE = "mydatabases"


# táblázatok létrehozása
mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")

# adatbázisok mutatása
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)

# adatbázis használata
mycursor.execute(f"USE {DATABASE}")

# táblázat létrehozása
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# adatok beszúrása (INSERT)
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

#Select
mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
  
#Where
sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)