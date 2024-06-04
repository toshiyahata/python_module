import pandas as pd

df = pd.read_csv("./titanic.csv")

#課題1
df_ = df[["Age", "Gender", "Pclass", "Fare", "Survived"]]
# print(df_)

#課題2
df_ =  df_.dropna(how = "any")
# print(len(df_))

#課題3
# print("Max Fare:",df_["Fare"].max())
# print("Min Fare:", df_["Fare"].min())

#課題4
# print(len(df_[df_["Age"] <= 30]))

#課題5
# print(df_.sort_values("Pclass"))

#課題6
# print((df[df["Survived"] == 1]).groupby(["Gender"])["Survived"].count())

#課題7
print(df.groupby(["Gender"])["Age"].mean())