import pandas as pd


class Nutrition:
    # nutrition class to get nutrition data of given food item
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)

    def get_nutrition(self, key):
        # get nutrition data of given food item
        # key: food item name
        # return: nutrition data
        try:
            return self.df[self.df["key"] == key].iloc[0].to_dict()
        except:
            return None

