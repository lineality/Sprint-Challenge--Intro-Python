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

# # #GGA work

# skip header
#https://www.alexkras.com/how-to-read-csv-file-in-python/

# import library
import csv # for opening csv files

# creating an OOP Class
class City():
    # constructor method (function)
    def __init__(self, name, lat, lon):
        # new attributes (name, latitude, longitude)
        self.name = name
        self.lat = lat
        self.lon = lon
    # # Just to be thorough:
    # # this allows for clean printing of objects for inspection
    # def __str__(self):
    #     # using fstring to manage the format of priting
    #     return f"City Name:{self.name}, Latitude:{self.lat}, Longitude:{self.lon}"



# create variables
#
# cities-list will contain the target results
cities = []
# these 3 are used to process the data
names = []
lats = []
lons = []

# instructions:
# Implement the functionality to read from the 'cities.csv' file
# For each city record, create a new City instance and add it to the 
# `cities` list

# function to read and process a CSV file
def cityreader(cities=[]):
## this is the full list of options for column-features
## city,state_name,county_name,lat,lng,population,density,timezone,zips

    # opens csv file
    with open('cities.csv') as csvfile:

        # reading the csv file using the imported library
        readCSV = csv.reader(csvfile, delimiter=',')

        # skip header (new method)
        next(readCSV) 

        # this loop iterates through the csv 
        # and pulls out the 3 required columns
        for row in readCSV:
            # city names
            names.append(row[0])
            # city latitudes
            lats.append(row[3])
            # city longitudes
            lons.append(row[4])

        # original method to drop header
        # # remove header (the top row)
        # names.pop(0)
        # lats.pop(0)
        # lons.pop(0)

    # this iterates through the values, 
    # putting them into class Objects
    # adding city lat lon to class instances
    # the length is set to be the same as
    # the number of city names in the CSV
    for i in range(0,len(names)):
        # iterate
        cities.append(City(names[i], lats[i], lons[i]))

    # finally this returns the completed list of city-objects
    return cities

#run function    
cities = cityreader(cities)

# print a list of just names
# for all the listed cites
#print([i.name for i in cities])

# Print city information:
for c in cities:
    print(c)