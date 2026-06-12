'''Problem Statement
Daily temperatures of different cities are stored below.
Sample Data
temperature = { "Delhi": 41, 
"Mumbai": 33, 
"Chennai": 37, 
"Kolkata": 39, 
"Bengaluru": 28, 
"Pune": 30, 
"Jaipur": 42, 
"Lucknow": 40, 
"Hyderabad": 35, 
"Ahmedabad": 43 }
Tasks
1.
Display cities with temperature above 40°C.
2.
Find the hottest city.
3.
Find the coolest city.
4.
Calculate average temperature.
5.
Create a list of pleasant cities (<35°C).'''

temperature = { "Delhi": 41, 
"Mumbai": 33, 
"Chennai": 37, 
"Kolkata": 39, 
"Bengaluru": 28, 
"Pune": 30, 
"Jaipur": 42, 
"Lucknow": 40, 
"Hyderabad": 35, 
"Ahmedabad": 43 }

# 1. Display cities with temperature above 40°C.
print("Cities with temperature above 40°C:")
for city, temp in temperature.items():
    if temp > 40:
        print(city)

# 2.find the hottest city
hottest_city = max(temperature, key=temperature.get)
print("\nThe hottest city:")
print(hottest_city, ":", temperature[hottest_city],"°C")

# 3. Find the coolest city.
coolest_city = min(temperature, key=temperature.get)
print("\nThe coolest city:")
print(coolest_city, ":", temperature[coolest_city],"°C  ")

# 4. Calculate average temperature.
average_temp = sum(temperature.values()) / len(temperature)
print("\nAverage temperature:",(average_temp),"°C")

# 5. Create a list of pleasant cities (<35°C).
print("\nPleasant cities (<35°C):")
pleasant_cities = []

for city, temp in temperature.items():
    if temp < 35:
        pleasant_cities.append(city)

print(pleasant_cities)