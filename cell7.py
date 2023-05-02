output_dir = r'C:\Users\Devin\Desktop\MTG Deckbuilding Algorithm\output'
output_file = os.path.join(output_dir, 'generated_deck.txt')

with open(output_file, 'w', encoding='utf-8') as file:
    file.write(generated_text)
