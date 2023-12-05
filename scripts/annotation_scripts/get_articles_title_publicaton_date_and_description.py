import json 
import argparse
from pathlib import Path
from datetime import datetime
import csv
import re

def get_article_title_publication_date_and_description(input_file):
    input_path = Path(input_file)
    
    extracted_data = []
    with open(input_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        articles = data['articles']
        for article in articles:
            title = article['title']
            description = article['description']
            filtered_description =  re.sub(r'\s+', ' ', description)
            publication_date_utc = article['publishedAt']
            publication_date = datetime.strptime(publication_date_utc, '%Y-%m-%dT%H:%M:%SZ')
            # Format the date as year/month/day
            formatted_date = publication_date.strftime('%Y/%m/%d')
            extracted_data.append({'date': formatted_date, 'title': title, 'description':filtered_description})
            
    return extracted_data 


def get_unique_aritcless_sepcs_from_directory(input_dir):
    unique_article_titles = set()
    duplicate_articles=0
    unique_articles = [] 
    input_dir_path = Path(input_dir)  # Convert to Path object
    
    for input_file in input_dir_path.glob('*.json'): #Go through each json file and get the articles 
        #print(input_file)
        extracted_data = get_article_title_publication_date_and_description(input_file)
        print(len(extracted_data))
        for article in extracted_data: #Make sure there is no duplicates
            if article['title'] in unique_article_titles: #If we found a duplicate article
                duplicate_articles+=1
              
            else:
                unique_articles.append(article)
               
                unique_article_titles.add(article['title'])
    print("DUPLICATE ARTICLES NUMBER : " + str(duplicate_articles))
    print("UNIQUE ARTICLES NUMBER : " + str(len(unique_articles)))
    return unique_articles
    

def write_to_csv(output_file, data):
    output_path = Path(output_file)
    with open(output_path, 'w', newline='', encoding='utf-8') as file:
        # Specify the fieldnames (column headers)
        fieldnames = data[0].keys()

        # Create a writer object
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Write the header
        writer.writeheader()

        # Write the data
        for row in data:
            writer.writerow(row)
    
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input_directory", help="directory of json files that contains article information")
    parser.add_argument("-o", "--output_filepath", help="csv file that contains article_title, article_description, type")
    args = parser.parse_args()
    
    all_unique_articles = get_unique_aritcless_sepcs_from_directory(args.input_directory)
    #print(all_unique_articles)
    # Write all data to CSV
    write_to_csv(args.output_filepath, all_unique_articles)
    
if __name__ == "__main__":
    main()