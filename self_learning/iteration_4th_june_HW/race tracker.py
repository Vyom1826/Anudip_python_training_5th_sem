# program tracks the racers , first finisher , last finisher and difference between there time

n = int(input("Enter number of racers: "))

lap_time = float(input("Enter lap time for racer 1: "))

fastest_time = lap_time
slowest_time = lap_time
fastest_pos = 1
slowest_pos = 1

for i in range(2, n + 1):
    lap_time = float(input(f"Enter lap time for racer {i}: "))

    if lap_time < fastest_time:
        fastest_time = lap_time
        fastest_pos = i

    if lap_time > slowest_time:
        slowest_time = lap_time
        slowest_pos = i

difference = slowest_time - fastest_time

print("Fastest racer position:", fastest_pos)
print("Slowest racer position:", slowest_pos)
print("Difference between fastest and slowest lap time:", difference)