#program to display the battery charging status
battery_level = 20 

while battery_level <= 100:
	print("Battery level: ",battery_level,"%")
	battery_level += 10
	
print("Battery fully charged!")