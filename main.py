from calculator import calculate_food

print("Input animal information")
species = input("Species (cat/dog):  ")
weight = float(input("Weight:  "))
age = int(input("Age:  "))
sterilized = int(input("Sterilized (yes/no):  "))
feedings = int(input("Feedings:  "))
calories_per_100_grams = float(input("Calories per 100 g:  "))

print("\nAnimal information")
print(f"Species: {species}")
print(f"Weight: {weight} kg")
print(f"Age: {age} years")
print(f"Sterilized: {sterilized}")
print(f"Feedings: {feedings}")
print(f"Calories per 100 g: {calories_per_100_grams} kcal")

if weight <= 0 or age <= 0 or feedings <= 0 or calories_per_100_grams <= 0:
    print("Error: Weight, age, feedings, and calories must be positive numbers.")
    exit()

species = species.lower()  # Normalize species input to lowercase
sterilized = sterilized.lower() 

if species == "cat":
    if sterilized == "yes":
        mer_factor = 1.2  # Lower activity level for sterilized cats
    elif sterilized == "no":
        mer_factor = 1.4  # Higher activity level for non-sterilized cats
    else:
        print("Error: Sterilized input must be 'yes' or 'no'.")
        exit()
elif species == "dog":
    if sterilized == "yes":
        mer_factor = 1.6  # Lower activity level for sterilized dogs
    elif sterilized == "no":
        mer_factor  = 1.8  # Standard activity level for dogs    
    else:
        print("Error: Sterilized input must be 'yes' or 'no'.")
        exit()
else:
    print("Error: Unknown species. Please enter 'cat' or 'dog'.")
    exit()
    
daily_food = calculate_food(weight, activity_level, calories_per_100_grams)
print(f"Daily food requirement: {daily_food:.1f} g")
per_feeding = (daily_food / feedings)  
print(f"Per feeding: {per_feeding:.1f} g")