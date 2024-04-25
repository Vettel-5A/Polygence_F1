class EmissionCalcs:
    def __init__(self):
        # kg of CO2 per 1 km
        self.AIRPLANE_EMISSIONS = 24.17647
        self.TRUCK_EMISSIONS = 0.0133

    def find_carbon_emissions(self, drive_dist, fly_dist):
        flight_emissions = fly_dist * 1.60934 * self.AIRPLANE_EMISSIONS * 0.001
        print(flight_emissions)
        drive_emissions = drive_dist * 1.60934 * self.TRUCK_EMISSIONS * 0.001
        print(drive_emissions)
        total_emissions = flight_emissions + drive_emissions
        print(total_emissions)
        print(f"Total Emissions: {total_emissions} tonnes")
        print(f"Flight Emissions: {flight_emissions} tonnes")
        print(f"Drive Emissions: {drive_emissions} tonnes")