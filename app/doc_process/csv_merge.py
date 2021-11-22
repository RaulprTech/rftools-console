import pandas as pd


def generator():
    data1 = {"col_1": [1, 2, 3]}
    data2 = {"col_1": [4, 5, 6]}

    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)

    df = pd.concat([df1, df2], ignore_index=True)

    print(df)
