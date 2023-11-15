from geopy.distance import geodesic
import pandas as pd


class Airports():
    def __init__(self):
        self.airports_df = pd.read_csv('CodeSample/coordinates/airport_coordinates.csv')
        self.airports_remaining = []
        self.ordered_airports = []
   
    def order_algo(self, airport1):

        # Finding index of airport1
        for x in range(0, 24):
            if airport1 == self.airports_df["Airport"][x]:
                airport1_num = x
        
        print(airport1_num)

        for y in range(0, 24):
            if y != airport1_num:
                self.airports_remaining.append(self.airports_df["Airport"][y])

        self.ordered_airports.append(airport1)

        print(self.airports_remaining)
        print(self.ordered_airports)
        
        airport_name = ""
        # While the length of the airport does not equal zero.
        while len(self.airports_remaining) != 0:
            
            # Create 
            closest = 100000000000000

            # while closest == 0:
            #     closest = self.airport2airport(airport1, self.airports_df["Airport"][random.randint(0, 24)])
            
            for item in self.airports_remaining:
                test = self.airport2airport(airport1, item)
                print(f"{item} Test Dist: {test}")
                if test < closest:
                    closest = test
                    airport_name = item
            self.ordered_airports.append(airport_name)
            # print(ordered_airports)   
            self.airports_remaining.remove(airport_name)
            airport1 = airport_name
            # print(airports_remaining)
            # print(ordered_airports)   
            # print(len(airports_remaining))

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

        # print(airport1_coords)
        # print(airport2_coords)

        # Calculate the distance
        distance = geodesic(airport1_coords, airport2_coords).kilometers
        # print(distance)
        #     print(f"The distance between {airport1} and {airport2} is {distance} kilometers.")
        # else:
        #     print("Failed to retrieve coordinates from the SERP API.")
        return distance





        # closest = self.airport2airport(self.airports_df["Airport"][x], self.airport )
        # for x in range(0, 23):
        #     if airport1 != self.airports_df["Airport"][x]:
        #         airports_remaining.append(self.airports_df["Airport"][x])

        # for x in range(0, 22):
            
            
        #     closest = 0
        #     closest_distance = 100000000000000

        #     test_distance = self.airport2airport(self.airports_df["Airport"][airport1_num], self.airports_df["Airport"][x])

        #     if test_distance == 0:
        #         continue
            
        #     else:
        #         if test_distance < closest_distance:
        #             closest = x
        #             closest_distance = self.airport2airport(self.airports_df["Airport"][airport1_num], self.airports_df["Airport"][closest])
        #             airports_remaining.remove(self.airports_df["Airport"][x])
        #             ordered_airports.append(self.airports_df["Airport"][x])
        #     # print(airports_remaining)
        # print(ordered_airports)
        # # print(closest_distance)
        
                

