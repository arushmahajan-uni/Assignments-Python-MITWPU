import pandas as pd
import numpy as np


sample_data = {
    "Name": ["Aarav", "Priya", "Rohan", "Ananya", "Rohan", "Sneha"],
    "City": ["Pune", "Mumbai", np.nan, "Delhi", "Mumbai", "Pune"],
    "Marks": [85.0, np.nan, 72.0, 90.0, 72.0, 65.0],
    "Attendance": [90, 85, 78, 92, 78, 60]
}

df_initial = pd.DataFrame(sample_data)
df_initial.to_csv("students.csv", index=False)
print("--- Sample students.csv file created successfully ---")


df = pd.read_csv("students.csv")
print("\n1. Original Dataset:")
print(df)

print("\nDataset Info:")
df.info()

print("\nSummary Statistics:")
print(df.describe())


print("\n2. Duplicate Rows Found:")
print(df[df.duplicated()])

df = df.drop_duplicates()
print("\nDataset After Removing Duplicates:")
print(df)


print("\n3. Missing values per column:")
print(df.isnull().sum())

mean_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(mean_marks)
print(f"\nMissing 'Marks' filled with mean value ({mean_marks:.2f}):")
print(df)


df = df.dropna(subset=["City"])
print("\nDataset after dropping rows where 'City' was NaN:")
print(df)


df = df.drop(columns=["Attendance"])
print("\n4. Dataset after dropping 'Attendance' column:")
print(df)


high_scorers = df.loc[df["Marks"] >= 80, ["Name", "Marks"]]
print("\n5. High Scorers (Marks >= 80) using loc[]:")
print(high_scorers)

df.to_csv("cleaned_students.csv", index=False)
print("\n--- Preprocessed data saved to 'cleaned_students.csv' ---")