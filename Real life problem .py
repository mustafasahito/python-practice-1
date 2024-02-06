#REAL LIFE PROBLEMS
#Question no:1
dailySteps = 10000
distanceWalked = 5.5
caloriesBurned = 300

#To calculate the average steps per week, you can use the expression: 

averageStepsPerWeek = dailySteps * 7

#And to find the total distance covered in a month, you can use the expression: 

totalDistanceInMonth = distanceWalked*30

#Question no: 2

# Initialize variables for item names, quantities, and prices
itemNames = ["Apple", "Banana", "Milk"]
quantities = [3, 2, 1]
prices = [0.5, 0.3, 1.5]

# Calculate the total cost of items
totalCost = sum([quantity * price for quantity, price in zip(quantities, prices)])

# Check if you have enough budget
budget = 10.0  # Replace with your budget
if totalCost <= budget:
    print("You have enough budget to buy all the items!")
else:
    print("Oops! You don't have enough budget to buy all the items.")

#Question no:3
    
# Recipe ingredients and amounts
ingredient1 = "Flour"
amount1 = 2.5  # cups
ingredient2 = "Sugar"
amount2 = 1.5  # cups
ingredient3 = "Eggs"
amount3 = 3

# Number of servings
servings = 4

    # Calculate adjusted quantities
adjusted_amount1 = amount1 * servings
adjusted_amount2 = amount2 * servings
adjusted_amount3 = amount3 * servings

# Print adjusted quantities
print("Adjusted quantities for", servings, "servings:")
print(ingredient1, ":", adjusted_amount1, "cups")
print(ingredient2, ":", adjusted_amount2, "cups")
print(ingredient3, ":", adjusted_amount3)

#Question no:4
# User preferences
user_genre = "comedy"
user_rating = 7.5
user_release_year = 2010

# Movie database
movies = [
    {"title": "Movie 1", "genre": "comedy", "rating": 8.2, "release_year": 2012},
    {"title": "Movie 2", "genre": "action", "rating": 7.8, "release_year": 2011},
    {"title": "Movie 3", "genre": "comedy", "rating": 7.9, "release_year": 2010},
    {"title": "Movie 4", "genre": "drama", "rating": 8.5, "release_year": 2013},
    {"title": "Movie 5", "genre": "comedy", "rating": 7.2, "release_year": 2009}
]

# Find matching movies based on user preferences
matching_movies = []
for movie in movies:
    if (
        movie["genre"] == user_genre
        and movie["rating"] >= user_rating
        and movie["release_year"] >= user_release_year
    ):
        matching_movies.append(movie["title"])

# Print recommended movies
if len(matching_movies) > 0:
    print("Recommended movies based on your preferences:")
    for movie in matching_movies:
        print("- ", movie)
else:
    print("Sorry, there are no movies that match your preferences.")

#Question no:5
    # Task names and durations
tasks = {
    "Task 1": 2.5,
    "Task 2": 1.75,
    "Task 3": 3.25,
    "Task 4": 2.0,
    "Task 5": 1.5
}

# Calculate total time spent on each task
total_time = 0
for task, duration in tasks.items():
    total_time += duration
    print(f"Total time spent on {task}: {duration} hours")

# Identify areas for improvement
average_time = total_time / len(tasks)
for task, duration in tasks.items():
    if duration > average_time:
        print(f"You spent more time than average on {task}. Consider optimizing it.")
        