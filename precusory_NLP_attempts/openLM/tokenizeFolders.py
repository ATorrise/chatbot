import os
import spacy

nlp = spacy.load("en_core_web_sm")

def tokenize_text(text):
    # Tokenize the text using spaCy
    doc = nlp(text)
    # tokens = [token.text for token in doc]
    return [token.text for token in doc]

def process_folder_recursive(folder_path, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate through the items in the folder (both files and subfolders)
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        print(item_path)
        if os.path.isfile(item_path):
            # This is a file, so tokenize it
            with open(item_path, 'r', encoding='utf-8') as file:
                text = file.read()
                tokens = tokenize_text(text)

            # Save the tokenized text to an output file
            output_path = os.path.join(output_folder, item)
            with open(output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(' '.join(tokens))

        elif os.path.isdir(item_path):
            # This is a subfolder, so recursively process it
            subfolder_output = os.path.join(output_folder, item)
            process_folder_recursive(item_path, subfolder_output)

if __name__ == "__main__":
    input_folder = 'cliCode'
    output_folder = 'tokenizedFolders'

    process_folder_recursive(input_folder, output_folder)