import sqlite3
# My own code which I can understand my own way
#create connection to a database and create tables for A-line, Airport, Flight and Crew members
con =sqlite3.connect("DBName.db")
mycur = con.cursor()
'''mycur.execute("CREATE TABLE Airline(AirlineID, AirlineName, AirlineCode,Region Coverage)")
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
con.commit()'''
mycur.execute("CREATE TABLE Airport ( AirportID, AirportName, AirportCode, Location)")
mycur.execute(""" INSERT INTO Airport VALUES
    (1, 'International Airport', 'IA123', 'City Center'),
    (2, 'Regional Airport', 'RA456', 'Suburban Area'),
    (3, 'Coastal Airport', 'CA789', 'Beachside'),
    (4, 'Mountain Airport', 'MA101', 'Highlands'),
    (5, 'Desert Airport', 'DA112', 'Desert Region'),
    (6, 'Island Airport', 'IA113', 'Island Location'),
    (7, 'Urban Airport', 'UA114', 'Downtown Area'),
    (8, 'Rural Airport', 'RA115', 'Countryside'),
    (9, 'Luxury Airport', 'LA116', 'Luxury District'),
    (10, 'Budget Airport', 'BA117', 'Budget Zone'),
    (11, 'Charter Airport', 'CA118', 'Charter Hub'),
    (12, 'Cargo Airport', 'CA119', 'Cargo Zone'),
    (13, 'Heliport', 'HP120', 'Helicopter Landing Site'),
    (14, 'Polar Airport', 'PA121', 'Polar Region'),
    (15, 'Urban Heliport', 'UH122', 'Urban Helicopter Landing')""")
con.commit()

mycur.execute("CREATE TABLE Flight ( FlightID, FlightNumber, AirportCode, Location)")

#res =mycur.execute ("SELECT name FROM sqlite_master")
#res.fetchone()