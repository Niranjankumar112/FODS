import pandas as pd

data = {
    "Customer ID":[1,2,3,4,5,6],
    "Age":[25,30,35,40,28,45],
    "Gender":["M","F","M","F","M","F"],
    "Total Spending":[1200,700,300,1500,450,800]
}

df = pd.DataFrame(data)

def segment(x):
    if x >= 1000:
        return "High"
    elif x >= 500:
        return "Medium"
    else:
        return "Low"

df["Segment"] = df["Total Spending"].apply(segment)

print(df.groupby("Segment")["Age"].mean())
