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
        ) + "\n" + self.departureAirport + "\n" + self.destinationAirport + "\n" + str(
      self.flightStatus)