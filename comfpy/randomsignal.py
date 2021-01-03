import numpy as np


def generate_random_samples(tend=360):
    x = np.linspace(0, tend, tend * 1200)
    return np.sin(x) * np.cos(x + np.random.normal(scale=0.1, size=len(x))) + np.random.normal(scale=0.1, size=len(x))
