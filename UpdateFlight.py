import sqlite3
#this function is to update flight infor by presenting the flight ID
class UpdateFlight:
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
    
    def update_info(self):
        try:
            #self.get_connection()
            con_ui=sqlite3.connect('DBFlight.db')
            cur_ui = con_ui.cursor()
            self.set_flight_id(int(input("Enter Flight ID: ")))
            fid=self.get_flight_id()
            data5 =(fid,)
            print("Select an action")
            print ("1. Update Flight Number")
            print ("2. Change Destination ")
            print ("3. Assign a Pilot")
            print ("4. Update Flight Status")
            up_action =(int(input("Enter your choice: ")))
            if up_action == 1:
                self.set_flight_number(input("Enter New Flight Number: "))
                fn1=self.get_flight_number()
                data6= (fn1,)
                print("Current Flight Number ")
                cur_ui.execute("SELECT * FROM Flight WHERE FlightID=?", data5)
                result = cur_ui.fetchall()
                print(result)
                # Update statement
                cur_ui.execute("UPDATE Flight SET FlightNumber=? WHERE FlightID=?", (fn1, fid))
                con_ui.commit()
                cur_ui.execute("SELECT * FROM Flight WHERE FlightID=?", data5)
                result = cur_ui.fetchall()
                print("New Flight Number ")
                print(result)
                #if result.rowcount != 0:
                   # print(str(result.rowcount) + "Row(s) affected.")
                #else:
                    #print("Cannot find this record in the database")
        except Exception as e:
            print(e)
        finally:
            con_ui.close()