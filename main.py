from optimization_calcs.serp import Optimization
from optimization_calcs.drive import DriveSpecific
from private.secret import key

optimize = Optimization()
euro = DriveSpecific()

country = input("Choose first race: ")


optimize.order_races(country)
