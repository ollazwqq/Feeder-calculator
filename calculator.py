def calculate_food(weight, mer_factor, calories_per_100_grams):
    rer = 70 * (weight ** 0.75)  # formula for Resting Energy Requirement (RER)
    calories_daily = rer * mer_factor
    return calories_daily / (calories_per_100_grams / 100)   # Adjust for calorie content