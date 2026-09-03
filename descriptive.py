import pandas as pd

transport = {
    'Transport_Name': ["Bus","Train","Car","Auto"],
    'Distance': [120, 300, 80, 50]
    }

df = pd.DataFrame(transport)
print(df)

mean = df['Distance'].mean()
print("Mean =", mean)

median = df['Distance'].median()
print("Median =", median)

mode = df['Distance'].mode()[0]
print("Mode =", mode)

variance = df['Distance'].var()
print("Variance =", variance)

std = df['Distance'].std()
print("Standard Deviation =", std)
