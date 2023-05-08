# Cell 2 - Split decks into main decks and sideboards
import os

# declare variables to be used in main function, including system path and file directory
data_dir = r'C:\Users\Devin\Desktop\MTG Deckbuilding Algorithm\data'
deck_files = os.listdir(data_dir)
main_decks = []
sideboards = []

for deck_file in deck_files:
    file_path = os.path.join(data_dir, deck_file)
    with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
        deck_lines = file.readlines()
        sideboard_index = deck_lines.index('Sideboard\n')
        main_deck = ''.join(deck_lines[:sideboard_index])
        sideboard = ''.join(deck_lines[sideboard_index+1:])
        main_decks.append(main_deck)
        sideboards.append(sideboard)

# Cell 2 - Combine the sideboard (commander) and main deck
combined_decks = []

for main_deck, sideboard in zip(main_decks, sideboards):
    combined_decks.append(sideboard + main_deck)
