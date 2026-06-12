'''Problem Statement
Ratings given by users for movies are stored below.
Sample Data
ratings = { "Inception": 4.8, 
"Avatar": 4.3, 
"Titanic": 4.5, 
"Joker": 4.7, 
"Frozen": 3.8, 
"Interstellar": 4.9, 
"Dune": 4.6, 
"Up": 4.1, 
"Coco": 4.4, 
"Cars": 3.9 }
Tasks
1.
Display movies rated above 4.5.
2.
Find the highest-rated movie.
3.
Find the lowest-rated movie.
4.
Calculate average rating.
5.
Create a recommendation list (rating ≥ 4.5).'''

ratings = { "Inception": 4.8, 
"Avatar": 4.3, 
"Titanic": 4.5, 
"Joker": 4.7, 
"Frozen": 3.8, 
"Interstellar": 4.9, 
"Dune": 4.6, 
"Up": 4.1, 
"Coco": 4.4, 
"Cars": 3.9 }

# 1. display movies rating above 4.5
print("Movies rated above 4.5:")
for movie, rating in ratings.items():
    if rating > 4.5:
        print(movie)

# 2.find the highest rated movie.
highest_rated = max(ratings, key=ratings.get)
print("\nThe highest rated movie:")
print(highest_rated, ":", ratings[highest_rated])

# 3. find the lowest rated movie.
lowest_rated = min(ratings, key=ratings.get)
print("\nThe lowest rated movie:")
print(lowest_rated, ":", ratings[lowest_rated])

# 4. Calculate average rating.
average_rating = sum(ratings.values()) / len(ratings)
print("\nAverage rating:", average_rating)

# create a recommendation list (rating >= 4.5)
print("\nRecommendation list (rating >= 4.5):")
recommendation_list = []

for movie, rating in ratings.items():
    if rating >= 4.5:
        recommendation_list.append(movie)

print(recommendation_list)
