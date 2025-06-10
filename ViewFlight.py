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
                self.set_flight_id(int(input("Enter the FlightID: ")))
                fv1 =self.get_flight_id()
                print(fv1)

                cur_vf.execute("SELECT * FROM Flight WHERE FlightID = ?",str(fv1))
                result =cur_vf.fetchone()
                if type(result) == type(tuple()):
                    for index, detail in enumerate(result):
                        if index == 0:
                            print("Flight ID: " + str(detail))
                        elif index == 1:
                            print("Flight Number: " + detail)
                        elif index == 2:
                            print("Flight DepartureAirportID: " + detail)
                        else:
                            print("Status: " + str(detail))
                else:
                    print("No Record")
                #print(result)
                conn_vf.commit()
                print("Data displayed successfully")
        except Exception as e:
            print(e)

        finally:
           cur_vf.close()