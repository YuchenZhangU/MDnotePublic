import matplotlib.pyplot as plt
import numpy as np

def vis_1(a, b, t):
    return a * np.exp(-b * T)

def vis_2(a, b, t, Tref = 122):
    tmp = a * np.log10((Tref+460)/(T+460)) + np.log10(np.log10(b))
    return 10**10**tmp

# relperm params
swc = 0.300445
sor = 0.300624
nw = 1
no = 2.74262
krw_end = 0.23606
kro_end = 0.450008
sw_end = 1-sor
#sw_end = 0.35
sw = np.linspace(swc, sw_end, 2000)

# visco params
a = 4.708
b = 1500
muw = 0.50856 # @T=122
T_ref = 122
T_arr = np.linspace(122,300, 5)

# compute relperm
krw = np.power((sw - swc)/(1 - swc - sor), nw) * krw_end
kro = np.power((1  - sw - sor)/(1 - swc - sor), no) * kro_end

# plot fw of T = T_init
T = 122
muo_dead = vis_2(a, b, T, T_ref)
muo = muo_dead*0.92
fw_mu = krw/muw/(kro/muo + krw/muw)
ax = plt.subplot(111)
ax.plot(sw, fw_mu, c='k', linestyle='--', lw=3, alpha=0.45)
ax.set_xlabel('Sw')
ax.set_ylabel('Fw')
ax.axhline(y=0.8, color='r', linestyle='--', xmax=0.155)
ax.axvline(x=0.30155748, color='r', linestyle='--', ymax=0.8)
ax.axhline(y=0.95, color='r', linestyle='--', xmax=0.52)
ax.axvline(x=0.30558389, color='r', linestyle='--', ymax=0.95)
ax.grid()
ax.set_title('water fraction flow curve')

# interpolate to get sw_init
from scipy.interpolate import interp1d
sw_out = interp1d(fw_mu,sw)
#   focal = [                2     3     4    5      6      9]
fw_list = [0.7, 0.75, 0.8,  0.85, 0.9, 0.95, 0.98, 0.99]  #sw_init = 0.5
print(f'fw_list = {fw_list}')
print(f'mobile sw = {sw_out(fw_list)}')
print(f'so_init = {1 - sw_out(fw_list)}')