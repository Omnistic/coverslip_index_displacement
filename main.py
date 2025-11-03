from math import asin, pi, tan

wavelength_um = 0.85

n_coverslip = 1.5153
n_water = 1.3290

na = 0.95

tt_mm = 0.170

dd_mm = 2.0

alpha = asin( na / n_water )
beta = asin( na / n_coverslip )

hh_mm = tan( alpha ) * dd_mm

dd_prime_mm = ( hh_mm - tt_mm * tan( beta ) ) / tan( alpha )

delta_focus_mm = dd_mm - dd_prime_mm

print(f"Delta focus (mm): {delta_focus_mm:.6f}")