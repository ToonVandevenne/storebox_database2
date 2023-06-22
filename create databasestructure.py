import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="storebox"
)

mycursor = db.cursor()

mycursor.execute("CREATE TABLE Stores "
                 "(store_id INT AUTO_INCREMENT PRIMARY KEY, "
                 "store_location ENUM('Genk', 'Maasmechelen', 'Hasselt'), "
                 "store_address VARCHAR(255) NOT NULL, "
                 "store_contact VARCHAR(255) NOT NULL)")

mycursor.execute("CREATE TABLE Box "
                 "(box_id INT AUTO_INCREMENT PRIMARY KEY, "
                 "box_size ENUM('Small', 'Medium', 'Large'), "
                 "box_price DECIMAL(10, 2), "
                 "store_id INT, "
                 "FOREIGN KEY (store_id) REFERENCES Stores(store_id))")

mycursor.execute("CREATE TABLE Clients "
                 "(client_id INT AUTO_INCREMENT PRIMARY KEY, "
                 "first_name VARCHAR(255) NOT NULL, "
                 "last_name VARCHAR(255) NOT NULL, "
                 "email VARCHAR(255) NOT NULL, "
                 "username VARCHAR(255) NOT NULL, "
                 "password VARCHAR(255) NOT NULL)")

mycursor.execute("CREATE TABLE Reservation "
                 "(reservation_id INT AUTO_INCREMENT PRIMARY KEY, "
                 "duration INT, "
                 "status ENUM('Available', 'Unavailable'), "
                 "box_id INT, "
                 "client_id INT, "
                 "FOREIGN KEY (box_id) REFERENCES Box(box_id), "
                 "FOREIGN KEY (client_id) REFERENCES Clients(client_id))")

db.commit()
