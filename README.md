# EDHDeckbuildingAlgorithm
Experimental machine learning algorithm to generate top decklists from top deck data off of MTGTop8

This project uses a machine learning model to generate Magic: The Gathering (MTG) decklists in the Commander format. The model is trained on existing decklists and generates new decklists that contain only valid card names.

Dependencies:
- Python 3
- NumPy
- TensorFlow
- Keras
- requests

Directory Structure:
- data: Contains .txt files with sample decklists used for training the model.
- output: The directory where the generated decklist .txt files are saved.

Instructions:

1. Run the 'fetch_valid_card_names()' function to fetch all valid card names in the Commander format from the Scryfall API and store them in a set. This needs to be run only once.

2. Tokenize the text data in the sample decklists using the 'Tokenizer' class from Keras.

3. Preprocess the tokenized data to create input and target sequences for training the model.

4. Define the model architecture using TensorFlow and Keras. In this case, the model consists of an Embedding layer, two LSTM layers, and a Dense layer with a softmax activation function.

5. Train the model on the preprocessed data using the 'fit()' method.

6. Generate a new decklist by calling the 'generate_text()' function. This function takes a seed text, the trained model, the tokenizer, the sequence length, the number of cards to generate, and the set of valid card names as arguments. The function generates a decklist containing only valid card names.

7. Save the generated decklist to a .txt file in the 'output' directory.

Note: The generation process ensures that the model only produces valid card names by checking each predicted card name against the set of valid card names fetched from the Scryfall API. If a predicted card name is not valid, the model predicts the next most likely card name and checks it again until a valid card name is found. This process might slow down the text generation, as it requires additional checks for each predicted card name.
