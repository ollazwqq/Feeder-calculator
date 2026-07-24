def calculate_food(weight, activity_level, calories_per_100_grams):
    rer = 70 * (weight ** 0.75)  # formula for Resting Energy Requirement (RER)
    calories_daily = rer * activity_level
    return calories_daily / (calories_per_100_grams / 100)   # Adjust for calorie content