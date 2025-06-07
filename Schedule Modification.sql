-- Active: 1749242512549@@127.0.0.1@3306
-- database: FlightDatabase.db

-- This SQL script modifies  the Flight Table to update the flightStatus  and change the departure time of a flight.
UPDATE Flight
SET
    FlightStatus = 'Delayed',
    DepartureDateTime = '2025-06-07 15:00:00',
    ArrivalDateTime = '2025-06-07 18:00:10'
WHERE
    FlightID = 1;