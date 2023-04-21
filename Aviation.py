# Developed By: Yosra Alim
# Date: April 1st
# Description: A Python program that reads text files containing airport and flight data, then analyzes flights based on specific criteria.



import Flight
from Flight import *
from Airport import *


class Aviation:
    def __init__(self):
        self._allAirports = []
        self._allFlights = {}
        self._allCountries = {}

    # Creating getters and setters for the attributes
    def getAllAirports(self):
        return self._allAirports

    def getAllFlights(self):
        return self._allFlights

    def getAllCountries(self):
        return self._allCountries

    def setAllAirports(self, airports):
        self._allAirports = airports

    def setAllFlights(self, flights):
        self._allFlights = flights

    def setAllCountries(self, countries):
        self._allCountries = countries

    # Defining function loadData() to load data from files
    def loadData(self, airportFile, flightFile, countriesFile):
        try:
            with open(countriesFile, "r", encoding='utf8') as f:
                # Reading lines from countriesFile and extracting country name and continent
                for line in f:
                    # print(line)
                    parts = line.strip().split(',')
                    country = parts[0].strip()
                    continent = parts[1].strip()
                    # Creating dictionary with key as country name and value as continent
                    self._allCountries[country] = continent

            with open(airportFile, "r", encoding='utf8') as h:
                # Reading lines from airportFile and extracting airport code, country and city
                for line in h:
                    # print(line)
                    parts = line.strip().split(',')
                    code = parts[0].strip()
                    country = parts[1].strip()
                    city = parts[2].strip()
                    # Creating Airport object and appending it to _allAirports list
                    airport = Airport(code, city, country, self._allCountries[country])
                    if airport not in self._allAirports:
                        self._allAirports.append(airport)

            with open(flightFile, "r", encoding='utf8') as g:
                # Reading lines from flightFile and extracting flight number, origin and destination airports
                for line in g:
                    # print(line)
                    parts = line.strip().split(',')
                    flightNo = parts[0].strip()
                    origin = self.getAirportByCode(parts[1].strip())
                    destination = self.getAirportByCode(parts[2].strip())
                    # Creating Flight object and appending it to _allFlights dictionary
                    flight = Flight(flightNo, origin, destination)
                    if origin not in self._allFlights:
                        self._allFlights.setdefault(origin.getCode(), []).append(flight)
                    elif flight not in self._allFlights[origin]:
                        self._allFlights.setdefault(origin.getCode(), []).append(flight)

            return True

        except Exception as e:
            print(e)
            return False

    # Defining function getAirportByCode() to return airport object from _allAirports list by airport code
    def getAirportByCode(self, code):
        for airport in self._allAirports:
            if airport.getCode() == code:
                return airport
        return -1

    # Defining function findAllCityFlights() to find all flights to/from a city
    def findAllCityFlights(self, city):
        result = []
        flight_nos = set()
        for flightList in self._allFlights.values():
            for flight in flightList:
                if flight.getFlightNumber() not in flight_nos and (flight.getOrigin().getCity() == city or flight.getDestination().getCity() == city):
                    result.append(flight)
                    flight_nos.add(flight.getFlightNumber().strip())
        return result

    def findFlightByNo(self, flightNo):
        for flightList in self._allFlights.values():
            for flight in flightList:
                if flight.getFlightNumber() == flightNo:
                    return flight
        return -1

    def findAllCountryFlights(self, country):
        result = []
        flight_nos = set()
        for flightList in self._allFlights.values():
            for flight in flightList:
                if flight.getFlightNumber() not in flight_nos and (flight.getOrigin().getCountry() == country \
                        or flight.getDestination().getCountry() == country):
                    result.append(flight)
                    flight_nos.add(flight.getFlightNumber().strip())
        return result

    def findFlightBetween(self, origAirport, destAirport):
        # check for direct flight
        for flight in self._allFlights.get(origAirport.getCode(), []):
            if flight.getDestination().getCode() == destAirport.getCode():
                return f"Direct Flight({flight.getFlightNumber()}): {origAirport.getCode()} to {destAirport.getCode()}"
        # check for single-hop connecting flight
        possibleConnectingAirports = set()
        for flight in self._allFlights.get(origAirport.getCode(), []):
            connectingAirportCode = flight.getDestination().getCode()
            for secondFlight in self._allFlights.get(connectingAirportCode, []):
                if secondFlight.getDestination().getCode() == destAirport.getCode():
                    possibleConnectingAirports.add(connectingAirportCode)
        if len(possibleConnectingAirports) > 0:
            return possibleConnectingAirports
        else:
            return -1

    def findReturnFlight(self, firstFlight):
        for flight in self._allFlights.get(firstFlight.getDestination().getCode(), []):
            if flight.getDestination().getCode() == firstFlight.getOrigin().getCode():
                return flight
        return -1

    def findFlightsAcross(self, ocean):
        greenZone = ["North America", "South America"]
        blueZone = ["Europe", "Africa"]
        redZone = ["Asia", "Australia"]
        flights = set()
        if ocean == "Atlantic":
            for airport in self._allAirports:
                if airport.getContinent() in greenZone:
                    for flight in self._allFlights.get(airport.getCode(), []):
                        if flight.getDestination().getContinent() in blueZone:
                            flights.add(flight.getFlightNumber())
                elif airport.getContinent() in blueZone:
                    for flight in self._allFlights.get(airport.getCode(), []):
                        if flight.getDestination().getContinent() in greenZone:
                            flights.add(flight.getFlightNumber())
        elif ocean == "Pacific":
            for airport in self._allAirports:
                if airport.getContinent() in redZone:
                    for flight in self._allFlights.get(airport.getCode(), []):
                        if flight.getDestination().getContinent() in greenZone:
                            flights.add(flight.getFlightNumber())
                elif airport.getContinent() in greenZone:
                    for flight in self._allFlights.get(airport.getCode(), []):
                        if flight.getDestination().getContinent() in redZone:
                            flights.add(flight.getFlightNumber())
        if len(flights) > 0:
            return flights
        else:
            return -1
