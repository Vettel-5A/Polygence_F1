from geopy.distance import geodesic
import pandas as pd
from optimization_calcs.drive import DriveSpecific


class Optimization():
    def __init__(self):
        self.airports_df = pd.read_csv('CodeSample/coordinates/airport_coordinates.csv')
        self.circuits_df = pd.read_csv('CodeSample/coordinates/circuit_coordinates.csv')
        self.europe_df = pd.read_csv('CodeSample/coordinates/europe_coordinates.csv')
        self.euro_dict = self.europe_df.to_dict()
        self.airports_remaining = []
        self.ordered_airports = []
        self.total_distance = 0
        self.driving_distance = 0
        self.flying_distance = 0
        self.drive = False
        self.euro = DriveSpecific()
   
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
                final_distance = self.euro_recalc(airport1, item, test)
                print(f"Test: {test}")
                print(f"Final Dist: {final_distance}")
                print(f"Drive: {self.drive}")
                print(f"{item} Test Dist: {final_distance}")
                if final_distance < closest:
                    closest = final_distance
                    drive_check = test
                    airport_name = item
            self.total_distance += closest
            if closest != drive_check:
                self.driving_distance += closest
            else:
                self.flying_distance += closest
            #     airport_to_circuit_commute = float(self.airport_to_circuit(airport1))
            #     for x in range(0, 9):
            #         if airport1 == self.airports_df["Airport"][x]:
            #             airport1_num = x
            #     self.total_distance += airport_to_circuit_commute
            #     self.driving_distance += airport_to_circuit_commute
            # self.drive = False


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

        self.airport_to_circuit()
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
        airport1_coords = f"{self.airports_df['Latitude'][airport1_num]},{self.airports_df['Longitude'][airport1_num]}"
        airport2_coords = f"{self.airports_df['Latitude'][airport2_num]},{self.airports_df['Longitude'][airport2_num]}"

        # Calculate the distance
        distance = geodesic(airport1_coords, airport2_coords).miles
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
            circuit1_coords = f"{self.europe_df['Latitude'][circuit1_num]},{self.europe_df['Longitude'][circuit1_num]}"
            circuit2_coords = f"{self.europe_df['Latitude'][circuit2_num]},{self.europe_df['Longitude'][circuit2_num]}"
            print(circuit1_coords)
            print(circuit2_coords)
            drive_distance = self.euro.get_driving_distance(circuit1_coords, circuit2_coords, test_distance)
            return drive_distance

        else:
            return test_distance

    def airport_to_circuit(self):
        for x in range(1, 23):
            if self.ordered_airports[x] not in self.euro_dict['Circuit'].values():
                place_index = x
            
                airport_coords = f"{self.airports_df['Latitude'][place_index]}, {self.airports_df['Longitude'][place_index]}"
                circuit_coords = f"{self.circuits_df['Latitude'][place_index]}, {self.circuits_df['Longitude'][place_index]}"

                print("Calculating Airport Distance")

                add = self.euro.get_driving_distance(airport_coords, circuit_coords, 0) * 2
                self.driving_distance += add
                self.total_distance 
            else:
                if self.ordered_airports[x - 1] in self.euro_dict['Circuit'].values():
                    last_airport_coords = f"{self.airports_df['Latitude'][x-1]}, {self.airports_df['Longitude'][x-1]}"
                    last_circuit_coords = f"{self.circuits_df['Latitude'][x-1]}, {self.circuits_df['Longitude'][x-1]}"
                    add_distance = self.euro.get_driving_distance(last_airport_coords, last_circuit_coords, 0)
                    self.driving_distance += add_distance
                    self.total_distance += add_distance
                elif self.ordered_airports[x + 1] in self.euro_dict['Circuit'].values():
                    next_airport_coords = f"{self.airports_df['Latitude'][x+1]}, {self.airports_df['Longitude'][x+1]}"
                    next_circuit_coords = f"{self.circuits_df['Latitude'][x+1]}, {self.circuits_df['Longitude'][x+1]}"
                    add_distance = self.euro.get_driving_distance(next_airport_coords, next_circuit_coords, 0)
                    self.driving_distance += add_distance
                    self.total_distance += add_distance
                
                # place_index = x
            
                # airport_coords = f"{self.airports_df['Latitude'][place_index]}, {self.airports_df['Longitude'][place_index]}"
                # circuit_coords = f"{self.circuits_df['Latitude'][place_index]}, {self.circuits_df['Longitude'][place_index]}"

                # print("Calculating Airport Distance")

                # return self.euro.get_driving_distance(airport_coords, circuit_coords, 0) * 2