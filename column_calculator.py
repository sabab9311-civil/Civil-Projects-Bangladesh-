# Column Load Calculator
print("=== Column Axial Load Calculator ===")

width = float(input("Column Width in mm: "))
depth = float(input("Column Depth in mm: "))
concrete_strength = float(input("Concrete Strength f'c in MPa: "))

area = width * depth
axial_load = 0.4 * concrete_strength * area / 1000

print(f"\nColumn Area: {area} mm²")
print(f"Safe Axial Load: {axial_load:.2f} KN")
Add: 1st Python Project - Column Calculator
