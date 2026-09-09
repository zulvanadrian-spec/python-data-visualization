import pandas as pd

data = {
    "Departement":["Sales","IT","Sales","HR","IT","HR"],
    "Salary":[5000000,7000000,5500000,4500000,7500000,4800000],
    "Experience":[2, 5, 3, 1, 6, 2]
}

df = pd.DataFrame(data)
print(df)

# --- GROUP BY ---
print("\n+-+-+-+ GROUP BY DEPARTEMENT +-+-+-+\n")
print(df.groupby("Departement")) # simply creates an object for grouping purposes

# --- CALCULATE AVARAGE SALARY ---
print("\n+-+-+-+ AVARAGE SALARY EACH DEPARTEMENT +-+-+-+")
print(df.groupby("Departement")["Salary"].mean())

# --- CALCULATE SUM ---
print("\n+-+-+-+ TOTAL SALARY EACH DEPARTEMENT +-+-+-+")
print(df.groupby("Departement")["Salary"].sum())

# --- MULTIPLE AGGREGATION FUNCTION ---
print("\n+-+-+-+ CALCULATE MULTIPLE STATICS AT ONCE +-+-+-+")
print(
    df.groupby("Departement")["Salary"].agg(
        ["sum","mean","max","min"]
    )
)
# 'sum'(total salry), 'mean'(avarage salary), 'max'(highest salary), 'min'(lower salary)

# --- COUNT RECORDS ---
print("\n+-+-+-+ COUNT THE NUMBER OR ROWS PER GROUP +-+-+-+")
print(df.groupby("Departement").size()) # --> alphabetis

# --- COUNT UNIQUE VALUES ---
print("\n+-+-+-+ COUNT OCCURANCES +-+-+-+")
print(df["Departement"].value_counts()) # --> descending

# --- FIND UNIQUE VALUES ---
print("\n+-+-+-+ DISPLAY UNIQUE DEPARTEMENT NAMES +-+-+-+")
print(df["Departement"].unique()) # just count values "Departement" in the data

# --- SORT AGGREGATION RESLUTS ---
result = df.groupby("Departement")["Salary"].mean()
print("\n+-+-+-+ SORT DEPARTEMENT BY AVG SALARY +-+-+-+")
print(result.sort_values(ascending=False)) # --> descending