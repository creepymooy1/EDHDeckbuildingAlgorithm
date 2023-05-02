# Cell 3 - Tokenize the combined decks
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

tokenizer = Tokenizer(char_level=False, filters='', split='\n')
tokenizer.fit_on_texts(combined_decks)
total_words = len(tokenizer.word_index)

# Cell 3 - Convert text to sequences
sequences = tokenizer.texts_to_sequences(combined_decks)

# Cell 3 - Prepare input and target sequences
seq_length = 100
input_data = []
target_data = []

for deck_seq in sequences:
    for i in range(len(deck_seq) - seq_length):
        input_data.append(deck_seq[i:i + seq_length])
        target_data.append(deck_seq[i + seq_length])

input_data = np.array(input_data)
target_data = np.array(target_data)
