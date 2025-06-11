import sqlite3
from ViewFlight import *
from UpdateFlight import *

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
        self.flightNumber = 'TEST123'
        self.departureAirportID = 15
        self.destinationAirportID = 14
        self.departureDateTime = '2024-10-10 00:00:00'
        self.arrivalDateTime = '2024-10-10 08:00:00'
        self.airlineID = 5
        self.flightStatus = 'Landed'
        self.pilotID = 1

    def set_flight_id(self, flightID):
        self.flightID = flightID

    def set_flight_number(self, flightNumber):
        self.flightNumber = flightNumber

    def set_departure_airport_id(self, departureAirportID):
        self.departureAirportID = departureAirportID

    def set_destination_airport_id(self, destinationAirportID):
        self.destinationAirportID = destinationAirportID

    def set_flight_status(self, flightStatus):
        self.flightStatus = flightStatus

    def set_departure_datetime(self, departureDateTime):
        self.departureDateTime = departureDateTime

    def set_arrival_datetime(self, arrivalDateTime):
        self.arrivalDateTime = arrivalDateTime

    def set_airline_id(self, airlineID):
        self.airlineID = airlineID

    def set_pilot_id(self, pilotID):
        self.pilotID = pilotID

    def get_flight_id(self):
        return self.flightID
    
    def get_flight_number(self):
        return self.flightNumber
    
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
    
    def get_pilot_id(self):
        return self.pilotID

    def __str__(self):
        return str(self.flightID) + "," + self.flightNumber + ","+ str(self.departureAirportID)+","+ str(self.destinationAirportID)+ "," + self.departureDateTime + "," + self.arrivalDateTime + "," +str(self.airlineID) + "," + self.flightStatus + ","+str(self.pilotID)
        #return str(
        #self.flightID
        #) + "\n" + self.flightNumber + "\n" + self.departureAirport + "\n" + self.destinationAirport + "\n" + self.flightStatus

 # class to deal with the database operation for adding flight info   
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
            #fid = mycur3.execute("SELECT COUNT(DISTINCT FlightID) FROM Flight")
            #print(fid)
            f=0
            for row in mycur3.execute("SELECT FlightID, FlightNumber FROM Flight ORDER by FlightID"):
                f=f+1
            #print (f)
            #flight.set_flight_id(int(mycur3.execute("SELECT COUNT(DISTINCT FlightID) FROM Flight")))
            #flight.set_flight_id(int(input("Enter FlightID: ")))
            #f1 = flight.get_flight_id()
            f1=f+1
            flight.set_flight_number(input("Enter FlightNumber: "))
            f2 = flight.get_flight_number()

            for row in mycur3.execute("SELECT AirportID, AirportName FROM Airport ORDER BY AirportID"):
                print (row)
            print("Please select different Airport IDs for Departure and Destination Airports")
            flight.set_departure_airport_id(int(input("Enter Departure Airport ID: ")))
            f3 = flight.get_departure_airport_id()
            flight.set_destination_airport_id(int(input("Enter Destination Airport ID: ")))
            f4 = flight.get_destination_airport_id()

            flight.set_departure_datetime(input("Enter Departure Date and Time YYYY-MM-DD HH:MM:SS: "))
            f5 = flight.get_departure_datetime()

            flight.set_arrival_datetime(input("Enter Arrival Date and Time YYYY-MM-DD HH:MM:SS: "))
            f6 = flight.get_arrival_datetime()

            for row in mycur3.execute("SELECT AirlineID, AirlineName FROM Airline ORDER BY AirlineID"):
                print (row)
            flight.set_airline_id(int(input("Enter AirlineID: ")))
            f7 = flight.get_airline_id()

            flight.set_flight_status(input("Enter Flight Status: "))
            f8 = flight.get_flight_status()
            #f8 =flight.flightStatus

            print("Pilot IDs: 1 - John, 5 - Sarah, 9 - Linda, 13 - Elizabeth")
            flight.set_pilot_id(int(input("Enter PilotID: ")))
            f9 = flight.get_pilot_id()
            #data = str(f1) + "," + f2 + "," + str(f3)+ "," + str(f4)+ "," + f5 + "," + f6 + "," + str(f7) + "," + f8 + "," + str(f9)
            data = [str(f1), f2, str(f3),str(f4), f5 , f6 , str(f7), f8, str(f9)]
            #data = str(flight.flightID) + "," + flight.flightNumber + ","+ str(flight.departureAirportID)+","+ str(flight.destinationAirportID)+ "," + flight.departureDateTime +","+ flight.arrivalDateTime + "," +str(flight.airlineID) + "," + flight.flightStatus + ","+str(flight.pilotID)
            #mycur3.executemany("INSERT INTO Flight VALUES(?,?,?,?,?,?,?,?,?)", tuple(str(flight).split(",")))
            #mycur3.executemany("INSERT INTO Flight VALUES(?,?,?,?,?,?,?,?,?)", data)
            mycur3.execute("INSERT INTO Flight VALUES (?,?,?,?,?,?,?,?,?)", data)
            print (data)
            conn2.commit()
            print("Inserted data successfully")
        except Exception as e:
            print(e)
        finally:
            mycur3.close()
while True:
  print("\n Menu:")
  print("**********")
  print(" 1. Add a New Flight")
  print(" 2. View FlightInfo")
  print(" 3. Update FlightInfo")
  #print(" 4. Search a flight")
  #print(" 5. Update data some records")
  #print(" 6. Delete data some records")
  print(" 7. Exit\n")

  __choose_menu = int(input("Enter your choice: "))
  #db_ops = DBOperations()
  if __choose_menu == 1:
    DBoperations().insert_data()
    #db_ops.create_table()
  elif __choose_menu == 2:
      ViewFlight().searchFlight()
   # db_ops.insert_data()
  elif __choose_menu == 3:
      UpdateFlight().update_info()
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