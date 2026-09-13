# Concrete Mix Design Calculator for M20
print("=== M20 Concrete Mix Calculator for 1m³ ===")

volume = float(input("Enter Concrete Volume in m³: "))

# M20 Ratio 1:1.5:3, Total = 5.5 parts
cement = (volume * 1440) / 5.5  # kg
sand = cement * 1.5             # kg  
aggregate = cement * 3          # kg
water = cement * 0.5            # liters

print(f"\nFor {volume} m³ M20 Concrete:")
print(f"Cement: {cement:.2f} kg = {cement/50:.2f} Bags")
print(f"Sand: {sand:.2f} kg")
print(f"Aggregate: {aggregate:.2f} kg")
print(f"Water: {water:.2f} liters")
3rd Python Project -  Concrete Mix Calculator
