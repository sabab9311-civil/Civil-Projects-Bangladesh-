# Steel Bar Weight & Cutting Length Calculator
print("=== Steel Bar Calculator ===")

diameter = float(input("Enter Bar Diameter in mm: "))
length = float(input("Enter Total Length in meter: "))
lapping = float(input("Enter Lapping Length in meter per joint: "))
no_of_joints = int(input("Enter Number of Lapping Joints: "))

# Formula: Weight = d² / 162.2 kg/m
weight_per_meter = (diameter ** 2) / 162.2
total_length = length + (lapping * no_of_joints)
total_weight = total_length * weight_per_meter

print(f"\nFor {diameter}mm Bar:")
print(f"Weight per meter: {weight_per_meter:.3f} kg/m")
print(f"Total Cutting Length: {total_length:.2f} meter")
print(f"Total Weight: {total_weight:.2f} kg")
5th Python Project - Steel Bar Calculator
