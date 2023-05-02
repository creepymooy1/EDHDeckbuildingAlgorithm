from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Embedding

model = Sequential([
    Embedding(total_words + 1, 256, input_length=seq_length),
    LSTM(256, return_sequences=True),
    LSTM(256),
    Dense(total_words + 1, activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam')
