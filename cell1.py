# dependencies
import requests
import json

# main function to fetch valid card names from the scryfall API
def fetch_valid_card_names():
    valid_card_names = set()
    url = "https://api.scryfall.com/catalog/card-names?q=legal:commander"
    while url:
        response = requests.get(url)
        data = json.loads(response.text)
        cards = data.get("data", [])

        for card in cards:
            valid_card_names.add(card)  # No need to access a "name" key

        if data.get("has_more"):
            url = data["next_page"]
        else:
            break

    return valid_card_names

valid_card_names = fetch_valid_card_names()
