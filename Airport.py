# Developed By: Yosra Alim
# Date: April 1st
# Description: A Python program that reads text files containing airport and flight data, then analyzes flights based on specific criteria.


class Airport:
    def __init__(self, code, city, country, continent):
        # Initialize the instance variables _code, _city, _country, and _continent based on the corresponding
        # parameters in the constructor
        self._code = code
        self._city = city
        self._country = country
        self._continent = continent

    def __repr__(self):
        # Return the representation of this Airport in the following format:
        # {code} ({city}, {country})
        return f"{self._code} ({self._city}, {self._country})"

    def getCode(self):
        # Getter that returns the Airport code
        return self._code

    def getCity(self):
        # Getter that returns the Airport city
        return self._city

    def getCountry(self):
        # Getter that returns the Airport country
        return self._country

    def getContinent(self):
        # Getter that returns the Airport continent
        return self._continent

    def setCity(self, city):
        # Setter that updates the Airport city
        self._city = city

    def setCountry(self, country):
        # Setter that updates the Airport country
        self._country = country

    def setContinent(self, continent):
        # Setter that sets updates the Airport continent
        self._continent = continent
