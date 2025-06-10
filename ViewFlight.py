import sqlite3
# this code allows user to view flights by different criterias

class ViewFlight:
    def __init__(self):
        self.flightID = 0
        self.flightStatus = ''
        self.pilotID = 0

    def set_flight_id(self, flightID):
        self.flightID = flightID
    
    def set_flight_status(self, flightStatus):
        self.flightStatus = flightStatus

    def set_pilot_id(self, pilotID):
        self.pilotID = pilotID

    def get_flight_id(self):
        return self.flightID

    def get_flight_status(self):
        return self.flightStatus

    def get_pilot_id(self):
        return self.pilotID
       
    def searchFlight(self):
        try:
            conn_vf= sqlite3.connect("DBFlight.db")
            cur_vf=conn_vf.cursor()
            print("Choose critera for viewing flight details: \n")
            print("1. FlightID\n")
            print("2. Flight Status\n")
            print("3. Pilot ID\n")
            choice = (int(input("Enter your choice: ")))
            if choice ==1:
                self.flightID =self.set_flight_id(int(input("Enter the FlightID: ")))
                f1 =self.get_flight_id()
                for row in cur_vf.execute("select * from Flight where FlightID = ?", f1):
                    print(row)
                conn_vf.commit()
                print("Data displayed successfully")
        except Exception as e:
            print(e)

        finally:
           conn_vf.close()