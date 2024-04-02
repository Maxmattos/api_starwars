import requests
import pandas as pd


def get_data_character_api():
    url = 'https://swapi.dev/api/people/'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        characters = []
        for result in data['results']:
            character = {
                "name": result["name"],
                "height": int(result["height"]),
                "mass": int(result["mass"])
            }
            characters.append(character)
        return characters
    else:
        print("Failed Connection. Status Code:", response.status_code)
        return None


def create_dataframe(dados):
    return pd.DataFrame(dados)


def order_characters(df, sort_column='height'):
    return df.sort_values(by=[sort_column], ascending=False)


def create_csv(data, filename):
    try:
        df = pd.DataFrame(data)
        df.to_csv(filename, index=False)
        print(f'File {filename} created successfully.')
    except Exception as err:
        print(f'Error creating CSV file {filename}:', err)


def main():
    try:
        data = get_data_character_api()
        df = create_dataframe(data)
        ordered_characters = order_characters(df)
        create_csv(ordered_characters, "star_wars_characters.csv")
    except Exception as err:
        print("There was an error with Star Wars API. Please try again!", err)


main()
