# Foundation & Earthwork Calculator
print("=== Isolated Footing Calculator ===")

no_of_footing = int(input("Number of Footings: "))
length = float(input("Footing Length in ft: "))
width = float(input("Footing Width in ft: "))
depth = float(input("Footing Depth in ft: "))
pcc_thickness = float(input("PCC Thickness in inch: ")) # 3 inch standard

# 1. Earthwork Volume
earthwork_cft = no_of_footing * length * width * depth
earthwork_cum = earthwork_cft * 0.0283168

# 2. PCC Volume & Material 1:4:8
pcc_depth_ft = pcc_thickness / 12
pcc_cft = no_of_footing * length * width * pcc_depth_ft
pcc_cum = pcc_cft * 0.0283168
dry_pcc = pcc_cum * 1.54
cement_pcc = (dry_pcc * 1/13) / 0.0347

# 3. RCC Volume & Material 1:1.5:3
rcc_cft = no_of_footing * length * width * (depth - pcc_depth_ft)
rcc_cum = rcc_cft * 0.0283168
dry_rcc = rcc_cum * 1.54
cement_rcc = (dry_rcc * 1/5.5) / 0.0347

total_cement = cement_pcc + cement_rcc

print(f"\nFor {no_of_footing} Nos Footing:")
print(f"Earthwork: {earthwork_cft:.0f} CFT")
print(f"PCC 1:4:8: {pcc_cum:.2f} Cum, Cement: {cement_pcc:.0f} Bags")
print(f"RCC 1:1.5:3: {rcc_cum:.2f} Cum, Cement: {cement_rcc:.0f} Bags")
print(f"Total Cement: {total_cement:.0f} Bags")
7th Python Project - Isolated Footing Calculator
