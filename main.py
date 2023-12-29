from optimization_calcs.serp import Optimization
from optimization_calcs.europe import EuroSpecific
from private.secret import key

optimize = Optimization()
euro = EuroSpecific()

country = input("Choose first race: ")

optimize.order_races(country)
