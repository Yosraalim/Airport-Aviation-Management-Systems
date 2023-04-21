# Developed By: Yosra Alim
# Date: April 1st
# Description: A Python program that reads text files containing airport and flight data, then analyzes flights based on specific criteria.



from Airport import *


class Flight:
    def __init__(self, flightNo: str, origAirport: Airport, destAirport: Airport):
        if not isinstance(origAirport, Airport) or not isinstance(destAirport, Airport):
            raise TypeError("The origin and destination must be Airport objects")
        if not isinstance(flightNo, str) or len(flightNo) != 6 or not flightNo[:3].isalpha() or not flightNo[
                                                                                                    3:].isdigit():
            raise TypeError("The flight number format is incorrect")

        self._flightNo = flightNo
        self._origin = origAirport
        self._destination = destAirport

    def __repr__(self):
        return f"Flight({self._flightNo}): {self._origin.getCity()} -> {self._destination.getCity()} [{'domestic' if self.isDomesticFlight() else 'international'}]"

    def __eq__(self, other):
        if not isinstance(other, Flight):
            return False
        return self._origin == other._origin and self._destination == other._destination

    def getFlightNumber(self):
        # Getter that returns the Flight number string code
        return self._flightNo

    def getOrigin(self):
        # Getter that returns the object of the Flight origin
        return self._origin

    def getDestination(self):
        # Getter that returns the object of the Flight destination
        return self._destination

    def isDomesticFlight(self):
        # Returns True if the flight is domestic
        return self._origin.getCountry() == self._destination.getCountry()

    def setOrigin(self, origin):
        # Setter that updates the Flight origin
        return self._flightNo

    def setDestination(self, destination):
        # Setter that updates the Flight destination
        return self._destination
