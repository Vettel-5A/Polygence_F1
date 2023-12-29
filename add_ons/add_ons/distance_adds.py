from optimization_calcs.serp import Optimization

class Adds:
    def __init__(self):
        self.optimize = Optimization()
    
    def airport_to_circuit(self, place):
        for x in range(0, 24):
            if place == self.airports_df["Airport"][x]:
                place_index = x
            
        airport_coords = self.optimize.airports_df["Latitude"][place_index], self.optimize.airports_df["Longitude"][place_index]
        circuit_coords = self.optimize.circuits_df["Latitude"][place_index], self.optimize.circuits_df["Longitude"][place_index]
        