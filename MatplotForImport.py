import matplotlib.pyplot as plt
import numpy as np
def create_plot():
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([10, 20, 25, 30, 35])
    plt.plot(x, y)
    plt.title("Uploaded Plot")
    return plt