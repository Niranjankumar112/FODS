import numpy as np
from scipy import stats

data = np.array([12.5, 13.2, 11.8, 12.9, 13.5, 12.1, 13.0, 12.7, 13.3, 12.4])

n = int(input("Enter sample size: "))
confidence = float(input("Enter confidence level (e.g. 0.95): "))
precision = float(input("Enter desired precision: "))

sample = data[:n]

mean = np.mean(sample)
std = np.std(sample, ddof=1)

alpha = 1 - confidence
t_value = stats.t.ppf(1 - alpha / 2, n - 1)

margin = t_value * (std / np.sqrt(n))

lower = mean - margin
upper = mean + margin

print("Sample Mean:", round(mean, 2))
print("Confidence Interval:", (round(lower, 2), round(upper, 2)))

if margin <= precision:
    print("Desired precision achieved")
else:
    print("Desired precision not achieved")
