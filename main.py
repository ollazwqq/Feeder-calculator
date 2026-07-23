def calculate_food(weight, food_percentage):
    return weight * food_percentage * 1000  # Convert to grams

print("Input animal information")
species = input("Species:  ")
weight = float(input("Weight:  "))
age = int(input("Age:  "))
feedings = int(input("Feedings:  "))

if weight <= 0 or age <= 0 or feedings <= 0:
    print("Error: Weight, age, and feedings must be positive numbers.")
    exit()

print("\nAnimal information")
print(f"Species: {species}")
print(f"Weight: {weight} kg")
print(f"Age: {age} years")
print(f"Feedings: {feedings}")

species = species.lower()  # Normalize species input to lowercase

if species == "cat":
    food_percentage = 0.03  # 3% of body weight
elif species == "dog":
    food_percentage = 0.05  # 5% of body weight
else:
    print("Error: Unknown species. Please enter 'cat' or 'dog'.")
    exit()
    
daily_food = calculate_food(weight, food_percentage)
print(f"Daily food requirement: {daily_food:.1f} g")
per_feeding = (daily_food / feedings)  
print(f"Per feeding: {per_feeding:.1f} g")