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
    def _init_(self):
        self.flightID = ''
        self.departureAirport = ''
        self.destinationAirport = ''
        self.departureDateTime = ''
        self.arrivalDateTime = ''
        self.flightNumber = ''
        self.airlineName = ''
        self.flightstatus = ''

    def set_flight_id(self, flightID):
        self.flightID = flightID

    def set_depature_airport(self, departureAirport):
        self.depature_airport = departureAirport

    def set_destination_airport(self, destinationAirport):
        self.destination_airport = destinationAirport

    def set_flight_status(self, flightStatus):
        self.flight_status = flightStatus

    def set_depature_datetime(self, departureDateTime):
        self.depature_datetime = departureDateTime

    def set_arrival_datetime(self, arrivalDateTime):
        self.arrival_datetime = arrivalDateTime

    def set_airline_name(self, airlineName):
        self.airline_name = airlineName

    def set_flight_number(self, flightNumber):
        self.flight_number = flightNumber

    def get_flight_id(self):
        return self.flightID
    
    def get_depature_airport(self):
        return self.departureAirport
    
    def get_destination_airport(self):
        return self.destinationAirport
    
    def get_flight_status(self):
        return self.flightStatus
    
    def get_depature_datetime(self):
        return self.departureDateTime

    def get_arrival_datetime(self):
        return self.arrivalDateTime

    def get_airline_name(self):
        return self.airlineName

    def get_flight_number(self):
        return self.flightNumber
    
    def __str__(self):
        return str(
        self.flightID
        ) + "\n" + self.flightNumber + "\n" + self.departureAirport + "\n" + self.destinationAirport + "\n" + str(
      self.flightStatus)
    
    def insert_data(self):
        try:
        #self.get_connection()
            conn2=sqlite3.connect('DBFlight.db')
            mycur3 = conn2.cursor()

            flight = AddFlightInfo()
            flight.set_flight_id(mycur3.execute("SELECT COUNT(*) FROM {Flight}"))
            flight.set_flight_number(int(input("Enter FlightNumber: ")))
            flight.set_departure_airport(int(input("Enter Departure Airport: ")))
            flight.set_destination_airport(int(input("Enter Destination Airport: ")))
            flight.set_flight_status(int(input("Enter Flight Status: ")))

            self.mycur3.execute("INSERT INTO Flight", tuple(str(flight).split("\n")))

            self.conn2.commit()
            print("Inserted data successfully")
        except Exception as e:
            print(e)
        finally:
            self.conn.close()
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
      AddFlightInfo.insert_data()
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