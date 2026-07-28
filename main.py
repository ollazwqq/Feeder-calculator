from calculator import calculate_food

class Animal:
    def __init__(self, species, weight, age, sterilized, feedings, calories_per_100_grams):
        self.species = species.lower()  # Normalize species input to lowercase
        self.weight = weight
        self.age = age
        self.sterilized = sterilized.lower()  # Normalize sterilized input to lowercase
        self.feedings = feedings
        self.calories_per_100_grams = calories_per_100_grams

    def mer_factor(self):
        if self.species == "cat":
            if self.sterilized == "yes":
                return 1.2  # Lower activity level for sterilized cats
            elif self.sterilized == "no":
                return 1.4  # Higher activity level for non-sterilized cats
            else:
                raise ValueError("Sterilized input must be 'yes' or 'no'.")
        elif self.species == "dog":
            if self.sterilized == "yes":
                return 1.6  # Lower activity level for sterilized dogs
            elif self.sterilized == "no":
                return 1.8  # Standard activity level for dogs    
            else:
                raise ValueError("Sterilized input must be 'yes' or 'no'.")
        else:
            raise ValueError("Unknown species. Please enter 'cat' or 'dog'.")

    def daily_food(self):
        return calculate_food(self)

print("Input animal information")
species = input("Species (cat/dog):  ")
weight = float(input("Weight:  "))
age = int(input("Age:  "))
sterilized = input("Sterilized (yes/no):  ")
feedings = int(input("Feedings:  "))
calories_per_100_grams = float(input("Calories per 100 g:  "))

if weight <= 0 or age <= 0 or feedings <= 0 or calories_per_100_grams <= 0:
    print("Error: Weight, age, feedings, and calories must be positive numbers.")
    exit()

species = species.lower()  # Normalize species input to lowercase
sterilized = sterilized.lower() 

animal = Animal(species, weight, age, sterilized, feedings, calories_per_100_grams)

print("\nAnimal information")
print(f"Species: {species}")
print(f"Weight: {weight} kg")
print(f"Age: {age} years")
print(f"Sterilized: {sterilized}")
print(f"Feedings: {feedings}")
print(f"Calories per 100 g: {calories_per_100_grams} kcal")

daily_food = animal.daily_food()
print(f"Daily food requirement: {daily_food:.1f} g")

per_feeding = (daily_food / animal.feedings)  
print(f"Per feeding: {per_feeding:.1f} g")