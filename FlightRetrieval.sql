-- database: FlightDatabase.db
d destination airports.
CREATe View Status AS
SELECT
    f.FlightID,
    f.FlightNumber,
    f.FlightStatus
FROM "Flight" f
WHERE
    f.FlightStatus = 'Scheduled' OR
    f.FlightStatus = 'Delayed' OR
    f.FlightStatus = 'Cancelled';


SELECT * FROM Status;

CREATE VIEW FlightDetails AS
SELECT
    f.FlightID,
    f.FlightNumber,
    a1.AirportName AS DepartureAirport,
    a2.AirportName AS DestinationAirport,
    f.DepartureDateTime,
    f.ArrivalDateTime,
    al.AirlineName,
    f.FlightStatus
FROM "Flight" f
JOIN "Airport" a1 ON f.DepartureAirportID = a1.AirportID
JOIN "Airport" a2 ON f.DestinationAirportID = a2.AirportID
JOIN "Airline" al ON f.AirlineID = al.AirlineID
WHERE
    f.FlightStatus = 'Scheduled' OR
    f.FlightStatus = 'Delayed' OR
    f.FlightStatus = 'Cancelled';

    SELECT * FROM FlightDetails;
    
-- This view combines flight details with the corresponding airline and departure and destination airports.
-- The view includes the flight ID, flight number, departure and destination airport names, departure and arrival times, airline name, and flight status.
-- The view filters flights to only include those that are scheduled, delayed, or cancelled.
