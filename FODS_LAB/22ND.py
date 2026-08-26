import pandas as pd
import numpy as np
from scipy import stats

# Create sample ratings
data = {
    "Rating": [4, 5, 4, 3, 5, 4, 5, 4, 3, 5]
}

df = pd.DataFrame(data)

ratings = df["Rating"]

mean = ratings.mean()
std = ratings.std()
n = len(ratings)

confidence = 0.95
alpha = 1 - confidence

t_value = stats.t.ppf(1 - alpha / 2, n - 1)
margin = t_value * (std / np.sqrt(n))

lower = mean - margin
upper = mean + margin

print("Average Rating:", round(mean, 2))
print("95% Confidence Interval:", (round(lower, 2), round(upper, 2)))

if mean >= 4:
    print("Customer Satisfaction: High")
else:
    print("Customer Satisfaction: Moderate")
