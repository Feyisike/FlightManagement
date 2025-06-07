-- This SQL script creates a view named FlightView that retrieves flight information
-- including flight ID, flight number, departure and destination airport names, departure and arrival times, airline name, and flight status.
-- The view filters the flights to include only those with statuses of 'Scheduled', 'Delayed', or 'Cancelled'.
-- This script assumes that the necessary tables (Flight, Airline, Airport) already exist in the database.
-- database: FlightDatabase.db
CREATE VIEW FlightView AS
SELECT
    Flight.FlightID,
    Flight.FlightNumber,
    a1.AirportName AS DepartureAirport,
    a2.AirportName AS DestinationAirport,
    Flight.DepartureDateTime,
    Flight.ArrivalDateTime,
    Airline.AirlineName,
    Flight.FlightStatus
FROM Flight
JOIN "Airport" a1 ON Flight.DepartureAirportID = a1.AirportID
JOIN "Airport" a2 ON Flight.DestinationAirportID = a2.AirportID
JOIN Airline ON Flight.AirlineID = Airline.AirlineID
WHERE
    Flight.FlightStatus = 'Scheduled' OR
    Flight.FlightStatus = 'Delayed' OR
    Flight.FlightStatus = 'Cancelled';

    SELECT * FROM FlightView;