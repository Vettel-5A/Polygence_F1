# Polygence_F1

## O/V
Formula One Racing (F1) travels across the globe, racing in more than 20 countries each year. While the series has placed an increased focus on environmental sustainability, the calendar order of the races in the season has not been optimized, leading to excess carbon emissions. This project determines the most emissions-efficient order of the Formula 1 Season Race calendar to reduce the organization’s carbon footprint from transportation logistics.

## Algorithm
Given a starting race,  distances from the airport of that first race are compared to those of all other race circuits. The closest airport is selected, and the corresponding race circuit is added to the calendar. This process is repeated until all 24 races are added. Thus, the starting city is key in determining the circuit's order. For example, if Bahrain, the first race of the 2024 season, is selected, it returns a different order than if Miami was selected as the first race.
