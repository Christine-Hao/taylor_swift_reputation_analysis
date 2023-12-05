import json 
import argparse
from pathlib import Path

def get_article_title_and_description(input_file):
    input_path = Path(input_file)
    
    with open(input_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        

def write_to_csv(output_file):
    pass
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_directory", help="directory of json files that contains article information")
    parser.add_argument("-o", "--output_filepath", help="csv file that contains article_title, article_description, type")
    args = parser.parse_args()
    
    
    
if __name__ == "__main__":
    main()