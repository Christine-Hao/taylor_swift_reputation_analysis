import csv  # Import the CSV module to handle CSV file operations
import json  # Import the JSON module to handle JSON data
import requests  # Import the requests module to make HTTP requests
from bs4 import BeautifulSoup  # Import BeautifulSoup from bs4 for HTML parsing
from datetime import datetime, timedelta  # Import datetime and timedelta for date manipulation
import time  # Import time module for handling sleep (delay)

# Define a function to extract the 'standfirst' content from a given article URL
def get_standfirst_content(article_url):
    response = requests.get(article_url)  # Send an HTTP GET request to the URL
    if response.status_code == 200:  # Check if the request was successful (HTTP status code 200)
        soup = BeautifulSoup(response.content, 'html.parser')  # Parse the HTML content of the page
        # Find the div element that contains the 'standfirst' content
        standfirst_div = soup.find('div', attrs={"data-gu-name": "standfirst", "class": "dcr-1yi1cnj"})
        if standfirst_div:  # Check if the div was found
            return standfirst_div.get_text(strip=True)  # Return the text content of the div
    return None  # Return None if the request failed or the div was not found

# Define a function to download articles from The Guardian API
def download_articles_guardian(api_key, keyword, num_pages, output_file):
    base_url = "https://content.guardianapis.com/search"  # Base URL of The Guardian API
    # Calculate the date six months ago from the current date
    six_months_ago = datetime.now() - timedelta(days=182)
    from_date = six_months_ago.strftime("%Y-%m-%d")  # Format the date in YYYY-MM-DD
    all_articles = []  # Initialize a list to store all article data

    # Loop through the specified number of pages
    for page in range(1, num_pages + 1):
        # Construct the API request URL with the given parameters
        url = f"{base_url}?q={keyword}&api-key={api_key}&from-date={from_date}&page={page}"
        response = requests.get(url)  # Send the API request
        data = response.json()  # Parse the JSON response
        # Extract the article data from the response
        articles = data.get('response', {}).get('results', [])
        all_articles.extend(articles)  # Add the articles to the all_articles list
        time.sleep(1.5)  # Sleep for 1.5 seconds to respect the API's rate limit

    # Initialize a list to store article titles and standfirst contents
    articles_info = []
    # Loop through all articles
    for article in all_articles:
        title = article['webTitle']  # Get the title of the article
        url = article['webUrl']  # Get the URL of the article
        standfirst = get_standfirst_content(url)  # Get the standfirst content of the article
        articles_info.append((title, standfirst))  # Append the title and standfirst to the list

    # Write the articles' titles and standfirst contents to a CSV file
    with open(output_file, "w", newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Title', 'Standfirst'])  # Write the header row
        writer.writerows(articles_info)  # Write all articles' data

# Set the API key, search keyword, number of pages to retrieve, and output file name
api_key = "139a81f4-1193-4e0d-9aee-7ce81964e346"
keyword = "Taylor Swift"
num_pages = 100  # Number of pages to retrieve
timestamp = time.strftime("%Y%m%d%H%M%S")  # Current timestamp
output_file = f"./halfyear.csv"  # Output CSV file path

# Call the function to download articles and save them to the CSV file
download_articles_guardian(api_key, keyword, num_pages, output_file)
