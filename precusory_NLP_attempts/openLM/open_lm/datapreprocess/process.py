import argparse
import os
import json
from datasets import load_dataset

def process_tokenized_data(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for root, dirs, files in os.walk(input_dir):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            output_file = os.path.join(output_dir, f'{dir}.jsonl')

            with open(output_file, 'w', encoding='utf-8') as jsonl_file:
                for filename in os.listdir(dir_path):
                    if filename.endswith(".txt"):
                        file_path = os.path.join(dir_path, filename)
                        with open(file_path, 'r', encoding='utf-8') as file:
                            text = file.read()
                            data = {"text": text, "folder": dir}
                            jsonl_file.write(json.dumps(data) + '\n')

def main(output_dir):
    input_dir = 'C:/Users/at895452/Desktop/innovation/tokenizedFolders'  # Specify the path to your tokenized data
    process_tokenized_data(input_dir, output_dir)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-dir', type=str, required=True,
                        help="Where to store the processed .jsonl files")

    args = parser.parse_args()
    main(args.output_dir)