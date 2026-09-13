# Beam Deflection Calculator
print("=== Beam Deflection Calculator ===")
load = float(input("Point Load in KN: "))
length = float(input("Beam Length in meter: "))
E = float(input("Modulus of Elasticity E in GPa: "))
I = float(input("Moment of Inertia I in mm^4: "))
L_mm = length * 1000
E_Nmm2 = E * 1000
deflection = (load * 1000 * L_mm**3) / (48 * E_Nmm2 * I)
print(f"\nMax Deflection at Center: {deflection:.3f} mm")
2nd Python Project - Beam Deflection Calculator
