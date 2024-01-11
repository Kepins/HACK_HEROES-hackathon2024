import pandas as pd


def order_csv(initial_df):
    weights_df = pd.read_csv('TASK-FILES/ProductsList.csv')

    joined = initial_df.join(weights_df, on="ID Produktu", rsuffix="_weights")

    joined = joined.sort_values(by="Waga (kg)", ascending=False)

    return joined
