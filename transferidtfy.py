from comfpy import weighting as s
import numpy as np
from scipy.signal import lti
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

fs = 0.01
f = np.arange(0.4, 80, fs)
By = s.By(fs, f)
Bz = s.Bz(fs, f)


def model1(x, gain1, tau1):
    y = lti(gain1, [tau1, 1]).step(T=x)[1]
    return y


time_interval = np.linspace(1, 100, 100)

output1 = model1(time_interval, 10, 4)

par1 = curve_fit(model1, time_interval, output1)

plt.loglog(f, By)
plt.loglog(f, Bz)
plt.show()
