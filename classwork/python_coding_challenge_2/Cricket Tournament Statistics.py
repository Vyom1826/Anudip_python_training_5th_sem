'''Problem Statement
Runs scored by players in a tournament are given below.
Sample Data
runs = { "Virat": 645, 
"Rohit": 512, 
"Gill": 698, 
"Rahul": 435, 
"Hardik": 278, 
"Pant": 534, 
"Surya": 389, 
"Jadeja": 301, 
"Iyer": 455, 
"KL": 410 }
Tasks
1.
Find the Orange Cap winner.
2.
Find the lowest scorer.
3.
Calculate total runs scored.
4.
Display players scoring more than 500 runs.
5.
Create a list of players scoring below 400.'''

runs = { "Virat": 645, 
"Rohit": 512, 
"Gill": 698, 
"Rahul": 435, 
"Hardik": 278, 
"Pant": 534, 
"Surya": 389, 
"Jadeja": 301, 
"Iyer": 455, 
"KL": 410 }

# 1. Find the Orange Cap winner.
orange_cap = max(runs, key=runs.get)
print("The orange cap winner :")
print(orange_cap, ":", runs[orange_cap],"runs" )

# 2.find the lowest score/
lowest_scorer = min(runs, key=runs.get)
print("\nThe lowest scorer :")
print(lowest_scorer, ":", runs[lowest_scorer],"runs" )

# 3. Calculate total runs scored.
total_run = sum(runs.values())
print("\nTotal runs scored:", total_run)

# 4. Display players scoring more than 500 runs.
print("\nPlayers scoring more than 500 runs :")
for player, score in runs.items():
    if score > 500:
        print(player)

# 5.create a list of players scoring below 400.
print("players scoring below 400runs :")

list = []

for player , score in runs.items():
    if score < 400:
        list.append(player)

print(list)

