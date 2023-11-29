import os
import json
import csv

directory = "./" # you might need to change this

unique_articles = []

for filename in os.listdir(directory):
    if filename.endswith(".json"):
        filepath = os.path.join(directory, filename)
        with open(filepath) as file:
            data = json.load(file)
            data = dict(data)
            for x in data['articles']:
                description = x.get('description')
                if description and description not in unique_articles:
                    unique_articles.append(description)

# Save descriptions to a CSV file
csv_file = "descriptions_2.csv" # you might need to chagne this path for your environment
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Description"])
    writer.writerows([[description] for description in unique_articles])
