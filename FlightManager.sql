CREATE TABLE Flight(
    FlightID INT PRIMARY KEY,
    FlightNnumber VARCHAR(10) NOT NULL,
    DepartureAirportID INT NOT NULL,
    DestinationAirportID INT NOT NULL,
    DepartureDateTime DATETIME NOT NULL,
    ArrivalDateTime DATETIME NOT NULL,
    AirlineID INT NOT NULL,
    FlightStatus VARCHAR(20) NOT NULL,
    FOREIGN KEY (DepartureAirportID) REFERENCES Airport (AirportID),
    FOREIGN KEY (DestinationAirportID) REFERENCES Airport (AirportID));

CREATE TABLE Airline(
    AirlineID INT PRIMARY KEY,
    AirlineName VARCHAR(80) NOT NULL,
    AirlineCode VARCHAR(10) NOT NULL,
    RegionCoverage VARCHAR(50) NOT NULL);

CREATE TABLE Airport(
    AirportID INT PRIMARY KEY,
    AirportName VARCHAR(80) NOT NULL,
    AirportCode VARCHAR(10) NOT NULL,
    Location VARCHAR(100) NOT NULL );

CREATE TABLE CrewMember(
    CrewID INT PRIMARY KEY,
    Forename VARCHAR(50) NOT NULL,
    Surname VARCHAR(50) NOT NULL,
    Role VARCHAR(20) NOT NULL,
    AirlineID INT NOT NULL,
    FlightNumber VARCHAR(10) NOT NULL,
    FOREIGN KEY (AirlineID) REFERENCES Airline (AirlineID),
    FOREIGN KEY (FlightNUmber) REFERENCES Flight (FlightNumber));