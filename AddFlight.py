import sqlite3
# connect to database created by flight.py
conn=sqlite3.connect('DBFlight.db')
mycur2 = conn.cursor()
# test to check that database connects and the data can be visible
for row in mycur2.execute("SELECT * FROM Flight"):
    print(row)
mycur2.close()

#create a class to handle the addition of flight info
class AddFlightInfo:
    def __init__(self):
        self.flightID = 0
        self.departureAirportID = 0
        self.destinationAirportID = 0
        self.departureDateTime = ''
        self.arrivalDateTime = ''
        self.flightNumber = ''
        self.airlineID = 0
        self.flightStatus = ''
        self.pilotID = 0

    def set_flight_id(self, flightID):
        self.flightID = flightID

    def set_departure_airport_id(self, departureAirportID):
        self.departure_airport_id = departureAirportID

    def set_destination_airport_id(self, destinationAirportID):
        self.destination_airport_id = destinationAirportID

    def set_flight_status(self, flightStatus):
        self.flight_status = flightStatus

    def set_departure_datetime(self, departureDateTime):
        self.departure_datetime = departureDateTime

    def set_arrival_datetime(self, arrivalDateTime):
        self.arrival_datetime = arrivalDateTime

    def set_airline_id(self, airlineID):
        self.airline_id = airlineID

    def set_flight_number(self, flightNumber):
        self.flight_number = flightNumber

    def set_pilot_id(self, pilotID):
        self.pilot_id = pilotID

    def get_flight_id(self):
        return self.flightID
    
    def get_departure_airport_id(self):
        return self.departureAirportID
    
    def get_destination_airport_id(self):
        return self.destinationAirportID
    
    def get_flight_status(self):
        return self.flightStatus
    
    def get_departure_datetime(self):
        return self.departureDateTime

    def get_arrival_datetime(self):
        return self.arrivalDateTime

    def get_airline_id(self):
        return self.airlineID

    def get_flight_number(self):
        return self.flightNumber
    
    def get_pilot_id(self):
        return self.pilotID

    def __str__(self):
        return str(self.flightID) + "," + self.flightNumber + ","+ str(self.departureAirportID)+","+ str(self.destinationAirportID)+ "," + self.departureDateTime + "," + self.arrivalDateTime + "," +str(self.airlineID) + "," + self.flightStatus + ","+str(self.pilotID)
        #return str(
        #self.flightID
        #) + "\n" + self.flightNumber + "\n" + self.departureAirport + "\n" + self.destinationAirport + "\n" + self.flightStatus
    
class DBoperations:
    def __init__(self):
        try:
            self.connq = sqlite3.connect("DBFlight.db")
            self.curq = self.connq.cursor()
            #self.cur.execute(self.sql_create_table_firsttime_Airline)
            #self.conn.commit()
        except Exception as e:
            print(e)
        finally:
            self.connq.close()

    def insert_data(self):
        try:
            #self.get_connection()
            conn2=sqlite3.connect('DBFlight.db')
            mycur3 = conn2.cursor()

            flight = AddFlightInfo()
            #flight.set_flight_id(mycur3.execute("SELECT COUNT(*) FROM {Flight}"))
            flight.set_flight_id(int(input("Enter FlightID: ")))
            flight.set_flight_number(input("Enter FlightNumber: "))
            for row in mycur3.execute("SELECT AirportID, AirportName FROM Airport ORDER BY AirportID"):
                print (row)
            print("Please select different Airport IDs for Departure and Destination Airports")
            flight.set_departure_airport_id(int(input("Enter Departure Airport ID: ")))
            flight.set_destination_airport_id(int(input("Enter Destination Airport ID: ")))
            flight.set_departure_datetime(input("Enter Departure Date and Time YYYY-MM-DD HH:MM:SS: "))
            flight.set_arrival_datetime(input("Enter Arrival Date and Time YYYY-MM-DD HH:MM:SS: "))
            for row in mycur3.execute("SELECT AirlineID, AirlineName FROM Airline ORDER BY AirlineID"):
                print (row)
            flight.set_airline_id(int(input("Enter AirlineID: ")))
            flight.set_flight_status(input("Enter Flight Status: "))
            print("Pilot IDs: 1 - John, 5 - Sarah, 9 - Linda, 13 - Elizabeth")
            flight.set_pilot_id(int(input("Enter PilotID: ")))
            #data = str(flight.flightID) + "," + flight.flight_number + ","+ str(flight.departureAirportID)+","+ str(flight.destinationAirportID)+ "," + flight.departureDateTime +","+ flight.arrivalDateTime + "," +str(flight.airlineID) + "," + flight.flight_status + ","+str(flight.pilotID)
            mycur3.executemany("INSERT INTO Flight VALUES(?,?,?,?,?,?,?,?,?)", tuple(str(flight).split(",")))
            #mycur3.executemany("INSERT INTO Flight VALUES(?,?,?,?,?,?,?,?,?)", data)
            mycur3.commit()
            print("Inserted data successfully")
        except Exception as e:
            print(e)
        finally:
            mycur3.close()
while True:
  print("\n Menu:")
  print("**********")
  print(" 1. Add a New Flight")
  #print(" 2. Insert data into FlightInfo")
  #print(" 3. Select all data from FlightInfo")
  #print(" 4. Search a flight")
  #print(" 5. Update data some records")
  #print(" 6. Delete data some records")
  print(" 7. Exit\n")

  __choose_menu = int(input("Enter your choice: "))
  #db_ops = DBOperations()
  if __choose_menu == 1:
    DBoperations().insert_data()
    #db_ops.create_table()
  #elif __choose_menu == 2:
   # db_ops.insert_data()
  #elif __choose_menu == 3:
    #db_ops.select_all()
  #elif __choose_menu == 4:
    #db_ops.search_data()
  #elif __choose_menu == 5:
    #db_ops.update_data()
  #elif __choose_menu == 6:
    #db_ops.delete_data()
  elif __choose_menu == 7:
    exit(0)
  else:
    print("Invalid Choice")