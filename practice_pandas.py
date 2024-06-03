import pandas as pd

df = pd.read_csv("./titanic.csv")

# print(df[["Age", "Name"]])
# print(df[0:10])
# print(df.head(4))
# print(df.loc[[2],["Age"]])
# print(df.iloc[5,6])
# print(df.iat[0,3])
# print(df.at[4,"Age"])
# print(df["Age"]>=34)
# print(df[df["Age"]>=30])
# print(df[df["Age"].isin([20,30,40])])
# print(df.sort_values("PassengerId", inplace = True))
# print(df)
# df_ = df.dropna(how = "any")
# df_ = df.fillna(value = 0)
# df_ = df.isna()
# print(df_)
# print(df.groupby("Gender")[["Gender"]].count())
# print(df.groupby(["Gender", "Survived"])[["Survived"]].count())
# print(df["Gender"].value_counts())
# print(df)

for index, colmn in df.iterrows():
    print(colmn, df.at[20, "Age"])