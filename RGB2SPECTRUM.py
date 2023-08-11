import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def rgb2spec(rgb_bar, rgb_color, D65):
    wl = rgb_bar[:, 0]
    A = rgb_bar[:, 1:]
    s1 = np.dot(A[:, 1].T, D65)
    c1 = s1 * rgb_color
    E = np.dot(np.linalg.inv(np.dot(A.T, A)), A.T)
    f1 = np.dot(c1, E)
    return wl, f1.T

# DEMO
D65 = pd.read_csv("CIE-D65-5nm.csv").values
D65 = D65[:, 1:]
dark_red = np.atleast_2d([139,0,0])
brown = np.atleast_2d([165,42,42])
fire_brick = np.atleast_2d([178,34,34])
rgb_bar = pd.read_csv("CIE_rgb_bar_5nm_array.csv")
wl, dark_red_spec = rgb2spec(rgb_bar.values, dark_red, D65)
wl, brown_spec = rgb2spec(rgb_bar.values, brown, D65)
wl, fire_brick_spec = rgb2spec(rgb_bar.values, fire_brick, D65)
plt.plot(wl, dark_red_spec)
plt.plot(wl, brown_spec)
plt.plot(wl, fire_brick_spec)
plt.show()

    


