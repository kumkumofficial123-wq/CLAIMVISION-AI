import pandas as pd

history = pd.read_csv("dataset/user_history.csv")

print("USER HISTORY COLUMNS")
print(history.columns.tolist())

print("\nFIRST USER RECORD")
print(history.iloc[0])