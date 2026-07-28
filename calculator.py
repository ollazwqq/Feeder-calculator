def calculate_food(animal):
    rer = 70 * (animal.weight ** 0.75)  # formula for Resting Energy Requirement (RER)
    calories_daily = rer * animal.mer_factor()
    return calories_daily / (animal.calories_per_100_grams / 100)   # Adjust for calorie content