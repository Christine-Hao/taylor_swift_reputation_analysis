import csv
import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time

def get_standfirst_content(article_url):
    response = requests.get(article_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        standfirst_div = soup.find('div', attrs={"data-gu-name": "standfirst", "class": "dcr-1yi1cnj"})
        if standfirst_div:
            return standfirst_div.get_text(strip=True)
    return None

def download_articles_guardian(api_key, keyword, num_pages, output_file):
    base_url = "https://content.guardianapis.com/search"
    six_months_ago = datetime.now() - timedelta(days=182)
    from_date = six_months_ago.strftime("%Y-%m-%d")
    all_articles = []

    for page in range(1, num_pages + 1):
        url = f"{base_url}?q={keyword}&api-key={api_key}&from-date={from_date}&page={page}"
        response = requests.get(url)
        data = response.json()
        articles = data.get('response', {}).get('results', [])
        all_articles.extend(articles)
        time.sleep(1.5)

    articles_info = []
    for article in all_articles:
        title = article['webTitle']
        url = article['webUrl']
        standfirst = get_standfirst_content(url)
        articles_info.append((title, standfirst))

    with open(output_file, "w", newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['Title', 'Standfirst'])
        writer.writerows(articles_info)

api_key = "139a81f4-1193-4e0d-9aee-7ce81964e346"
keyword = "Taylor Swift"
num_pages = 100
timestamp = time.strftime("%Y%m%d%H%M%S")
output_file = f"./halfyear.csv"

download_articles_guardian(api_key, keyword, num_pages, output_file)
