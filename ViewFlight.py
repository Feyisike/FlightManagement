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
                data2 = (fv1,)
                #cur_vf.execute("SELECT * FROM Flight WHERE FlightID = ?",tuple(str(fv1)))
                cur_vf.execute("SELECT * FROM Flight WHERE FlightID = ?",data2)
                result =cur_vf.fetchall()
                #cur_vf.close()
                print(result)
                '''if type(result) == type(tuple()):
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
                    print("No Record")'''
                #print(result)
                #conn_vf.commit()
                print("Data displayed successfully")
            elif choice ==2:
                self.set_flight_status(input("Enter Flight Status: "))
                fs1=self.get_flight_status()
                data3 = (fs1,)
                cur_vf.execute("SELECT * FROM Flight WHERE FlightStatus = ?",data3)
                result =cur_vf.fetchall()
                #cur_vf.close()
                print(result)
            elif choice == 3:
                print("Pilot IDs: 1 - John, 5 - Sarah, 9 - Linda, 13 - Elizabeth")
                self.set_pilot_id(int(input("Enter Pilot ID: ")))
                pid=self.get_pilot_id()
                data4 =(pid,)
                cur_vf.execute("SELECT * FROM Flight WHERE PilotID = ?",data4)
                result =cur_vf.fetchall()
                #cur_vf.close()
                print(result)
            else:
                print("Not a valid choice")
        except Exception as e:
            print(e)

        finally:
           cur_vf.close()