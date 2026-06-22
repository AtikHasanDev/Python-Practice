import math

# Bandwidth and receiver parameters
B = 1e6      # Hz
NF = 2       # dB
Lother = 2   # Other losses (dB)

# Uplink parameters
f_up = 14000     # MHz
d_up = 38000     # km
Pt_up = 40       # dBm
Gt_up = 45       # dBi
Gr_sat = 35      # dBi

# Downlink parameters
f_down = 12000   # MHz
d_down = 38000   # km
Pt_down = 50     # dBm
Gt_down = 35     # dBi
Gr_down = 40     # dBi

# Noise power
N = -174 + 10 * math.log10(B) + NF

# ---------- UPLINK ----------
fspl_up = 20 * math.log10(d_up) + 20 * math.log10(f_up) + 32.44

link_budget_up = Pt_up + Gt_up + Gr_sat - fspl_up - Lother
CN_up = link_budget_up - N

# ---------- DOWNLINK ----------
fspl_down = 20 * math.log10(d_down) + 20 * math.log10(f_down) + 32.44

link_budget_down = Pt_down + Gt_down + Gr_down - fspl_down - Lother
CN_down = link_budget_down - N

# ---------- OVERALL C/N ----------
cn_up_lin = 10 ** (CN_up / 10)
cn_down_lin = 10 ** (CN_down / 10)

cn_total_lin = 1 / ((1 / cn_up_lin) + (1 / cn_down_lin))
CN_total = 10 * math.log10(cn_total_lin)

# Results
print(f"Uplink Link Budget = {link_budget_up:.2f} dBm")
print(f"Downlink Link Budget = {link_budget_down:.2f} dBm")
print(f"Uplink C/N = {CN_up:.2f} dB")
print(f"Downlink C/N = {CN_down:.2f} dB")
print(f"Overall C/N = {CN_total:.2f} dB")