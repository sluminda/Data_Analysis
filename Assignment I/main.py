import pandas as pd

# -----------------
# Assignment I
# -----------------

df = pd.read_csv("titanic.csv")

df.columns = df.columns.str.lower()

# by gender
print(df.groupby("sex")["survived"].mean())

# by class
print(df.groupby("pclass")["survived"].mean())

# Female passengers survival rate is much higher than male passengers.
# 1st class peoples have more chance to survive than 2nd and 3rd class.
# so gender and class both affecting survival.


# -----------------
# Assignment II
# -----------------

# create family size column
df["family_size"] = df["sibsp"] + df["parch"]

# family size
print(df["family_size"].mean())

# Most passengers are travel alone or with very small family.
# average family size is around 1 so not many big families.


# -----------------
# Assignment III
# -----------------

# average fare by embark port
print(df.groupby("embarked")["fare"].mean())

# Ticket price is not same for all ports.
# passengers from C port paying more money than others.
# so fare is depend on embarked location.

