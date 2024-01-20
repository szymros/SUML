import pandas as pd


def create_dictionary_of_car_brands_as_key_and_models_as_value():
    df = pd.read_csv('data/Car_Prices_Poland_Kaggle.csv')
    df = df.drop_duplicates(subset=['mark', 'model'], keep='last')
    brands = df['mark'].unique()
    models = df['model'].unique()
    dictionary = {}
    for brand in brands:
        dictionary[brand] = []
    for model in models:
        dictionary[df[df['model'] == model]['mark'].values[0]].append(model)
    return dictionary


if __name__ == '__main__':
    dictionary_cars = create_dictionary_of_car_brands_as_key_and_models_as_value()
    print(dictionary_cars)
