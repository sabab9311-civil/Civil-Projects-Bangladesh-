# Brick & Mortar Calculator for 5 inch wall
print("=== Brick Work Calculator ===")

area = float(input("Wall Area in Square Feet: "))
brick_size = "10x5x3 inch"  # Standard Bangladesh Brick

# Calculation: 1 sft 5" wall = 5 bricks + 0.022 cft mortar
total_bricks = area * 5
mortar_cft = area * 0.022

# Mortar 1:4 ratio
cement_bags = (mortar_cft * 0.3) / 1.25  # 1 bag = 1.25 cft
sand_cft = mortar_cft * 0.8

print(f"\nFor {area} sft 5 inch Brick Wall:")
print(f"Bricks Needed: {total_bricks:.0f} pcs")
print(f"Cement: {cement_bags:.2f} Bags")
print(f"Sand: {sand_cft:.2f} CFT")
print(f"Mortar Volume: {mortar_cft:.2f} CFT")
4th Python Project - Brick Work Calculator
