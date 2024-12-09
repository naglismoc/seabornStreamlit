import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# a = np.arange(1,11)
# b = np.random.randint(-5,25,10)
# sns.lineplot(x = a, y = b)
# plt.show()


# a = np.arange(1,11)
# b = np.random.randint(-5,25,10)
# sns.scatterplot(x = a, y = b)
# plt.show()



# Generate data for three shooters with specified distributions
np.random.seed(42)  # For reproducibility

# Shooter_A: Scattered around the center
shooter_a_x = np.random.normal(0, 3, 50)  # Mean 0, SD 3
shooter_a_y = np.random.normal(0, 3, 50)

# Shooter_B: Grouped around the top left (-5, 5)
shooter_b_x = np.random.normal(-5, 1, 50)  # Mean -5, SD 1
shooter_b_y = np.random.normal(5, 1, 50)

# Shooter_C: Random across the board
shooter_c_x = np.random.uniform(-10, 10, 50)
shooter_c_y = np.random.uniform(-10, 10, 50)

# Combine the data into a single DataFrame
data = pd.DataFrame({
    "X_Coordinate": np.concatenate([shooter_a_x, shooter_b_x, shooter_c_x]),
    "Y_Coordinate": np.concatenate([shooter_a_y, shooter_b_y, shooter_c_y]),
    "Shooter": ["Shooter_A"] * 50 + ["Shooter_B"] * 50 + ["Shooter_C"] * 50
})

# Scatterplot with hue to represent shooters
plt.figure(figsize=(8, 8))
sns.scatterplot(data=data, x="X_Coordinate", y="Y_Coordinate", hue="Shooter", palette="Set2", s=100)

# Add target circles
circle1 = plt.Circle((0, 0), 10, color='gray', fill=False, linestyle='--')
circle2 = plt.Circle((0, 0), 7, color='gray', fill=False, linestyle='--')
circle3 = plt.Circle((0, 0), 4, color='gray', fill=False, linestyle='--')
circle4 = plt.Circle((0, 0), 2, color='gray', fill=False, linestyle='--')

plt.gca().add_artist(circle1)
plt.gca().add_artist(circle2)
plt.gca().add_artist(circle3)
plt.gca().add_artist(circle4)

# Formatting the plot
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.title("Shooting Practice Results", fontsize=16)
plt.xlabel("X Coordinate")
plt.ylabel("Y Coordinate")
plt.xlim(-11, 11)
plt.ylim(-11, 11)
plt.grid(True)
plt.legend(title="Shooter", loc='upper right')
plt.show()
