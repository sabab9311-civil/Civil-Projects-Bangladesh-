# Slab Material & Steel Calculator for Bangladesh
print("=== Slab Calculator ===")

area = float(input("Slab Area in Square Feet: "))
thickness = float(input("Slab Thickness in inch: ")) # 5 inch standard

# 1. Concrete Volume
thickness_ft = thickness / 12
volume_cft = area * thickness_ft
volume_cum = volume_cft * 0.0283168

# 2. Concrete Mix 1:2:4 for Slab. Wastage 5%
dry_volume = volume_cum * 1.54 * 1.05
cement_bags = (dry_volume * 1/7) / 0.0347  # 1 bag = 0.0347 cum
sand_cum = dry_volume * (2/7)
khowa_cum = dry_volume * (4/7)

# 3. Steel Estimation: 1.5% of concrete volume
steel_kg = volume_cum * 0.015 * 7850  # 7850 = density of steel

print(f"\nFor {area} sft {thickness} inch Slab:")
print(f"Concrete Volume: {volume_cum:.2f} Cum")
print(f"Cement: {cement_bags:.0f} Bags")
print(f"Sand: {sand_cum:.2f} Cum")
print(f"Khowa/Stone: {khowa_cum:.2f} Cum")
print(f"Steel Rod: {steel_kg:.0f} kg")
6th Python Project - Slab Calculator
