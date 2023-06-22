import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="storebox"
)

mycursor = db.cursor()

# add dummy-variables:
mycursor.execute("INSERT INTO Stores (store_location, store_address, store_contact) VALUES (%s,%s,%s)", ('Genk','Duinenlaan 1', '089/30/30/30'))
mycursor.execute("INSERT INTO Stores (store_location, store_address, store_contact) VALUES (%s,%s,%s)", ('Maasmechelen','Vijverlaan 1', '089/50/50/50'))
mycursor.execute("INSERT INTO Stores (store_location, store_address, store_contact) VALUES (%s,%s,%s)", ('Hasselt','Standbeeldlaan 1', '089/70/70/70'))

mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Small', 50, 1))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Small', 50, 1))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Small', 50, 1))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Medium', 80, 1))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Medium', 80, 1))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Medium', 80, 1))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Large', 110, 1))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Large', 110, 1))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Large', 110, 1))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Small', 50, 2))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Small', 50, 2))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Small', 50, 2))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Medium', 80, 2))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Medium', 80, 2))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Medium', 80, 2))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Large', 110, 2))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Large', 110, 2))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Large', 110, 2))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Small', 50, 3))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Small', 50, 3))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Small', 50, 3))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Medium', 80, 3))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Medium', 80, 3))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Medium', 80, 3))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Large', 110, 3))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Large', 110, 3))
mycursor.execute("INSERT INTO Box (box_size, box_price, store_id) VALUES (%s,%s,%s)", ('Large', 110, 3))

db.commit()