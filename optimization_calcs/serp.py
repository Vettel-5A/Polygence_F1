from geopy.distance import geodesic
import pandas as pd


class Optimization():
    def __init__(self):
        self.airports_df = pd.read_csv('coordinates/circuit_coordinates.csv')
        self.airports_remaining = []
        self.ordered_airports = []
        self.total_distance = 0
   
    def order_races(self, airport1):

        # Finding index of airport1
        for x in range(0, 24):
            if airport1 == self.airports_df["Airport"][x]:
                airport1_num = x
        
        print(airport1_num)

        # Appending airports in airports_coordinates.csv into list self.airports remaining
        for y in range(0, 24):
            if y != airport1_num:
                self.airports_remaining.append(self.airports_df["Airport"][y])

        self.ordered_airports.append(airport1)

        print(self.airports_remaining)
        print(self.ordered_airports)
        
        airport_name = ""
        # While the length of the airport does not equal zero.
        while len(self.airports_remaining) != 0:
            
            # Loop through self.airports_remaining, closest value initially set to some large number.
            closest = 100000000000000
            
            for item in self.airports_remaining:
                test = self.airport2airport(airport1, item)
                print(f"{item} Test Dist: {test}")
                if test < closest:
                    closest = test
                    airport_name = item
            self.total_distance += closest
            print(f"Total Distance: {self.total_distance}")

            self.ordered_airports.append(airport_name)
            self.airports_remaining.remove(airport_name)
            airport1 = airport_name

            print(self.total_distance)

            count = 1
            for country in self.ordered_airports: 
                print(f"{count}: {country} \n")
                count += 1

    def airport2airport(self, airport1, airport2):
        
        # Finding indexes of airports
        for x in range(0, 24):
            if airport1 == self.airports_df["Airport"][x]:
                airport1_num = x
            if airport2 == self.airports_df["Airport"][x]:
                airport2_num = x
        
        # Assigning coordinates to airports from dataframe
        airport1_coords = self.airports_df["Latitude"][airport1_num], self.airports_df["Longitude"][airport1_num]
        airport2_coords = self.airports_df["Latitude"][airport2_num], self.airports_df["Longitude"][airport2_num]

        # Calculate the distance
        distance = geodesic(airport1_coords, airport2_coords).kilometers
        return distance
        
                

