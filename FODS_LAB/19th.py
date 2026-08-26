import pandas as pd

data = {
    "Product":["A","B","C","D","E","F"],
    "Quantity Sold":[100,80,120,60,90,70],
    "Unit Price":[200,300,150,400,250,350]
}

df = pd.DataFrame(data)

df["Total Sales"] = df["Quantity Sold"] * df["Unit Price"]
df["Profit"] = df["Total Sales"] * 0.20

print(df.sort_values("Profit", ascending=False).head(5))
