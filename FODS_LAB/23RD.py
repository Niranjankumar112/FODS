import numpy as np
from scipy.stats import ttest_ind
import matplotlib.pyplot as plt

control = [50, 52, 49, 51, 50, 48, 52, 51]
treatment = [60, 62, 59, 61, 63, 60, 64, 62]

t_stat, p_value = ttest_ind(control, treatment)

print("T-statistic:", round(t_stat, 2))
print("P-value:", p_value)

if p_value < 0.05:
    print("Treatment has a statistically significant effect")
else:
    print("Treatment has no statistically significant effect")

plt.bar(["Control", "Treatment"],
        [np.mean(control), np.mean(treatment)])

plt.title("Treatment vs Control")
plt.ylabel("Average Outcome")
plt.show()
