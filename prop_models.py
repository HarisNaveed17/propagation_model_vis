import numpy as np
import matplotlib.pyplot as plt
import math


log_axis = np.logspace(0, 4, 500)
log_axis[-1] = 4*log_axis[-1]
freq = 800*math.pow(10, 6)
lmda = 3*math.pow(10, 8)/freq
ht = hr = 10

L_free = 10*np.log10((np.square(4*np.pi)*np.square(log_axis))/lmda)
L_2ray = 10*np.log10(np.power(np.square(lmda/(4*np.pi*log_axis))*4*np.square(np.sin((2*np.pi*ht*hr)/(lmda*log_axis))), -1))

plt.figure()
plt.xscale('log')
# plt.yscale('log')
plt.plot(log_axis, L_free, label='Free space')
plt.plot(log_axis, L_2ray, label='Flat Earth')
plt.title('Path Loss Comparison between Free Space and Flat Earth models', fontsize=16)
plt.xlabel('Distance (Log-scale)', fontsize=14)
plt.ylabel('Path Loss (dB)', fontsize=14)
plt.legend(loc=2, frameon=False, fontsize='medium')
plt.show()
