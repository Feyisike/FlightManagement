import sqlite3
# My own code which I can understand my own way
#create a database
con =sqlite3.connect("DBName.db")
mycur = con.cursor()
#mycur.execute("CREATE TABLE Airline(AirlineID, AirlineName, AirlineCode,Region Coverage)")
mycur.execute("""INSERT INTO Airline VALUES
    (1, 'Airways International', 'AI123', 'Global'),
    (2, 'Sky High Airlines', 'SHA456', 'North America'),
    (3, 'Oceanic Flights', 'OF789', 'Europe'),
    (4, 'Desert Wings', 'DW101', 'Middle East'),
    (5, 'Mountain Air', 'MA112', 'Asia'),
    (6, 'Pacific Airlines', 'PA113', 'Australia'),
    (7, 'Atlantic Airways', 'AA114', 'South America'),
    (8, 'Polar Express', 'PE115', 'Antarctica'),
    (9, 'Urban Jets', 'UJ116', 'Urban Areas'),
    (10, 'Rural Air Services', 'RAS117', 'Rural Areas'),
    (11, 'Luxury Flights', 'LF118', 'Luxury Travel'),
    (12, 'Budget Airlines', 'BA119', 'Budget Travel'),
    (13, 'Charter Air', 'CA120', 'Charter Services'),
    (14, 'Cargo Carriers', 'CC121', 'Cargo Transport'),
    (15, 'HeliServices', 'HS122', 'Helicopter Services')""")
#res =mycur.execute ("SELECT name FROM sqlite_master")
#res.fetchone()