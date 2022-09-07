import pandas as pd

# Based in dataframe: Column and rows

# It only allows one type of data per column.
def main():
    ## ----------- READ AND OBTAIN INFO --------------------------------------
    # FIXME: Add relative path.
    df = pd.read_csv("dataset.csv", index_col ="id")
    print(df)

    # Print the flast ten position of the dataframe
    print(df.tail(10))

    # Generate a dataset description with mean, std, count, min and percentiles
    df.describe()

    # Generate a clean data or replace the NaN data,
    # you can also add a dictionary with the column and info
    # to replace while using df.fillna
    df_filter = df.dropna() #df.fillna(0)

    # Show the head of the data (First five rows)
    df_filter.head()

    ## ------------ SELECT AND FILTER COLUMNS DATA----------------------------
    # Select the data of only one category
    sel = df["favorites"]
    print(sel)

    # Select the data of multiple categories
    sel2 = df[["favorites","full_text"]]
    print(sel2)

    ## -------------- SELECT AND FILTER ROW DATA -----------------------------
    # You can identify by index or base category using df.iloc:
    row1=  df.iloc[0]
    print(row1)
    row2 = df.iloc[0:3]
    print(row2)
    row3 = df.iloc[[0,2,4]]
    print(row3)

    # You can also use the identifier with df.loc:
    row4 = df.loc[[183721, 183722]]

    # TODO: Improve documentation

if __name__ == "__main__":
    main()