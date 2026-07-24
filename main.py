from calculator import calculate_food

print("Input animal information")
species = input("Species:  ")
weight = float(input("Weight:  "))
age = int(input("Age:  "))
feedings = int(input("Feedings:  "))
calories_per_100_grams = float(input("Calories per 100 g:  "))

print("\nAnimal information")
print(f"Species: {species}")
print(f"Weight: {weight} kg")
print(f"Age: {age} years")
print(f"Feedings: {feedings}")
print(f"Calories per 100 g: {calories_per_100_grams} kcal")

if weight <= 0 or age <= 0 or feedings <= 0 or calories_per_100_grams <= 0:
    print("Error: Weight, age, feedings, and calories must be positive numbers.")
    exit()

species = species.lower()  # Normalize species input to lowercase

if species == "cat":
    activity_level = 1.4  # Standard activity level for cats
elif species == "dog":
    activity_level = 2  # Standard activity level for dogs
else:
    print("Error: Unknown species. Please enter 'cat' or 'dog'.")
    exit()
    
daily_food = calculate_food(weight, activity_level, calories_per_100_grams)
print(f"Daily food requirement: {daily_food:.1f} g")
per_feeding = (daily_food / feedings)  
print(f"Per feeding: {per_feeding:.1f} g")