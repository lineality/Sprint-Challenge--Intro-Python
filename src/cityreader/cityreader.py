# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.

#GGA work

class City():
    # give it an additional name attribute
    def __init__(self, name, lat, lon):
        # new attribute
        self.name = name
        self.lat = lat
        self.lon = lon
    # this allows for clean printing
    def __str__(self):
        # using fstring to manage the format of priting
        return f"City Name:{self.name}, Latitude:{self.lat}, Longitude:{self.lon}"
    # read about this but did not impliment
    #def __repr__()

# city = City("city_name", 41.70505, -121.51521)

# import library
import csv

# create variable
cities = []

def cityreader(cities=[]):
    # TODO Implement the functionality to read from the 'cities.csv' file
    # For each city record, create a new City instance and add it to the 
    # `cities` list
    with open('cities.csv') as csvfile:
        # reading the csv file
        readCSV = csv.reader(csvfile, delimiter=',')

        # adding just the city column to the list of cities
        for row in readCSV:
            cities.append(row[0])

        # # adding city lat lon to class instances
        # for row in readCSV:
        #     # iterate?
        #     city = City(row[0], row[3], row[4])

    # # drop header
    cities.pop(0)


  # with open('cities.csv', newline='') as f:
  #   reader = csv.reader(f)
  #   cities = list(reader)
    
    return cities

cityreader(cities)

print(cities)

