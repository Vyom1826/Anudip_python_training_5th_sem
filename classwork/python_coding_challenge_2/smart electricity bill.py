'''Problem Statement
Monthly electricity consumption (units) of different houses in a residential society is stored as follows:
Sample Data
units = { "House101": 320, 
"House102": 180, 
"House103": 510, 
"House104": 275, 
"House105": 150, 
"House106": 430, 
"House107": 220, 
"House108": 390, 
"House109": 145, 
"House110": 600 
}

Tasks
    1.Display houses consuming more than 400 units.
    2.Find the highest-consuming house.
    3.Find the lowest-consuming house.
    4.Calculate the total units consumed.
    5.Create separate lists for:
        oLow Consumption (< 200)
        oMedium Consumption (200–400)
        oHigh Consumption (> 400)
    6.Count houses eligible for an energy-saving campaign (consumption > 300).
'''

units = { "House101": 320, 
"House102": 180, 
"House103": 510, 
"House104": 275, 
"House105": 150, 
"House106": 430, 
"House107": 220, 
"House108": 390, 
"House109": 145, 
"House110": 600 
}

#1. Display houses consuming more than 400 units.
print("Houses consuming more than 400 units:")
for house, units_consumed in units.items():
    if units_consumed > 400:
        print(house)

#2. Find the highest-consuming house.
highest_consuming = max(units, key=units.get)
print(f"\nHighest-consuming house: ")
print(highest_consuming, ":", (units[highest_consuming]),"Units")

#3. Find the lowest-consuming house
lowest_consuming = min(units, key=units.get)
print(f"\nLowest-consuming house: ")
print(lowest_consuming, ":", (units[lowest_consuming]),"Units")

#4. Calculate the total units consumed.
total_units = sum(units.values())
print(f"\nTotal units consumed: {total_units}")

'''5.
Create separate lists for:
o
Low Consumption (< 200)
o
Medium Consumption (200–400)
o
High Consumption (> 400)'''

low_consumption = []
medium_comsumption = []
high_consumption = []

for house , consumption in units.items() :

    if consumption < 200:
        low_consumption.append(house)

    elif 200 <= consumption <= 400:
        medium_comsumption.append(house)

    else:
        high_consumption.append(house)

print(f"\nLow Consumption: {low_consumption}")
print(f"\nMedium Consumption: {medium_comsumption}")
print(f"\nHigh Consumption: {high_consumption}")

# 6.Count houses eligible for an energy-saving campaign (consumption > 300).
eligible = []
campaign_count = 0

for house, consumption in units.items():
    if consumption > 300:
        campaign_count += 1
        eligible.append(house)

print(f"\nHouses eligible for an energy-saving campaign: {eligible}")

print(f"\nNumber of houses eligible for an energy-saving campaign: {campaign_count}")