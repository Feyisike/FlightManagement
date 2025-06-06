-- Flight Management System Database Schema
-- This script creates the necessary tables and inserts sample data for a flight management system.
CREATE TABLE Flight(
    FlightID INT PRIMARY KEY,
    FlightNumber VARCHAR(10) NOT NULL,
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
    AirlineID INT,
    FlightNumber VARCHAR(10),
    FOREIGN KEY (AirlineID) REFERENCES Airline (AirlineID),
    FOREIGN KEY (FlightNUmber) REFERENCES Flight (FlightNumber));

    INSERT INTO Airline(AirlineID, AirlineName, AirlineCode, RegionCoverage)
    VALUES
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
    (15, 'HeliServices', 'HS122', 'Helicopter Services');

INSERT INTO Airport(AirportID, AirportName, AirportCode, LOcation)
VALUES
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
(15, 'Urban Heliport', 'UH122', 'Urban Helicopter Landing');

INSERT INTO Flight(FlightID, FlightNumber, DepartureAirportID, DestinationAIrportID, DepartureDateTime, ArrivalDateTime, AirlineID, Flightstatus)
VALUES
(1, 'AI123-001', 1, 2, '2023-10-01 08:00:00', '2023-10-01 10:00:00', 1, 'Scheduled'),
(2, 'SHA456-002', 2, 3, '2023-10-01 09:30:00', '2023-10-01 11:30:00', 2, 'Delayed'),
(3, 'OF789-003', 3, 4, '2023-10-01 12:00:00', '2023-10-01 14:00:00', 3, 'Cancelled'),
(4, 'DW101-004', 4, 5, '2023-10-01 15:00:00', '2023-10-01 17:00:00', 4, 'On Time'),
(5, 'MA112-005', 5, 6, '2023-10-01 18:30:00', '2023-10-01 20:30:00', 5, 'Boarding'),
(6, 'PA113-006', 6, 7, '2023-10-01 21:00:00', '2023-10-01 23:00:00', 6, 'Landed'),
(7, 'AA114-007', 7, 8, '2023-10-02 07:15:00', '2023-10-02 09:15:00', 7, 'Diverted'),
(8, 'PE115-008', 8, 9, '2023-10-02 10:45:00', '2023-10-02 12:45:00', 8, 'Cancelled'),
(9, 'UJ116-009', 9, 10, '2023-10-02 13:30:00', '2023-10-02 15:30:00', 9, 'Scheduled'),
(10, 'RAS117-010', 10, 11, '2023-10-02 16:20:00', '2023-10-02 18:20:00', 10, 'Delayed'),
(11, 'LF118-011', 11, 12, '2023-10-02 19:00:00', '2023-10-02 21:00:00', 11, 'On Time'),
(12, 'BA119-012', 12, 13, '2023-10-02 22:30:00', '2023-10-03 00:30:00', 12, 'Boarding'),
(13, 'CA120-013', 13, 14, '2023-10-03 01:15:00', '2023-10-03 03:15:00', 13, 'Landed'),
(14, 'CC121-014', 14, 15, '2023-10-03 04:45:00', '2023-10-03 06:45:00', 14, 'Diverted'),
(15, 'HS122-015', 15, 1, '2023-10-03 07:30:00', '2023-10-03 09:30:00', 15, 'Cancelled');

INSERT INTO CrewMember(CrewID, Forename, Surname, Role)
VALUES
(1, 'John', 'Doe', 'Pilot'),
(2, 'Jane', 'Smith', 'Co-Pilot'),
(3, 'Emily', 'Johnson', 'Flight Attendant'),
(4, 'Michael', 'Brown', 'Flight Attendant'),
(5, 'Sarah', 'Davis', 'Pilot'),
(6, 'David', 'Wilson', 'Co-Pilot'),
(7, 'Laura', 'Garcia', 'Flight Attendant'),
(8, 'James', 'Martinez', 'Flight Attendant'),
(9, 'Linda', 'Rodriguez', 'Pilot'),
(10, 'Robert', 'Lopez', 'Co-Pilot'),
(11, 'Patricia', 'Hernandez', 'Flight Attendant'),
(12, 'William', 'Gonzalez', 'Flight Attendant'),
(13, 'Elizabeth', 'Perez', 'Pilot'),
(14, 'Charles', 'Sanchez', 'Co-Pilot'),
(15, 'Jessica', 'Clark', 'Flight Attendant');




