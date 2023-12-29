from geopy.distance import geodesic
import pandas as pd
from optimization_calcs.drive import EuroSpecific


class Optimization():
    def __init__(self):
        self.airports_df = pd.read_csv('CodeSample/coordinates/airport_coordinates.csv')
        self.circuits_df = pd.read_csv('CodeSample/coordinates/circuit_coordinates.csv')
        self.europe_df = pd.read_csv('CodeSample/coordinates/europe_coordinates.csv')
        self.airports_remaining = []
        self.ordered_airports = []
        self.total_distance = 0
        self.driving_distance = 0
        self.flying_distance = 0
        self.drive = False
        self.euro = EuroSpecific()
   
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
                    closest = self.euro_recalc(airport1, item, test)
                    airport_name = item
            self.total_distance += closest
            if self.drive == True:
                self.driving_distance += closest
            else:
                self.flying_distance += closest

            self.ordered_airports.append(airport_name)
            self.airports_remaining.remove(airport_name)
            airport1 = airport_name

            count = 1
            for country in self.ordered_airports: 
                print(f"{count}: {country} \n")
                count += 1
                
            print(f"Total Distance: {self.total_distance}")
            print(self.ordered_airports)
            print(f"Flying distance: {self.flying_distance}")
            print(f"Driving distance: {self.driving_distance}")

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

    def euro_recalc(self, circuit1, circuit2, test_distance):
        exist1 = False
        exist2 = False
        for x in range(0, 9):
            if circuit1 == self.europe_df["Circuit"][x]:
                circuit1_num = x
                exist1 = True

            if circuit2 == self.europe_df["Circuit"][x]:
                circuit2_num = x
                exist2 = True

        if exist1 and exist2:
            print("getting driving distance")
            circuit1_coords = f"{self.europe_df['Latitude'][circuit1_num]}, {self.europe_df['Longitude'][circuit1_num]}"
            circuit2_coords = f"{self.europe_df['Latitude'][circuit2_num]}, {self.europe_df['Longitude'][circuit2_num]}"
            print(circuit1_coords)
            print(circuit2_coords)
            drive_distance = self.euro.get_driving_distance(circuit1_coords, circuit2_coords)
            self.drive = True
            return drive_distance

        else:
            self.drive = False
            return test_distance
