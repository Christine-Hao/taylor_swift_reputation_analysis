import requests
import json
from datetime import datetime, timedelta
import time

def download_articles(api_key, keyword, num_articles, output_file):
    # Calculate the date one month ago
    one_month_ago = datetime.now() - timedelta(days=30)
    # two_months_ago = one_month_ago - timedelta(days=60)
    from_date = one_month_ago.strftime("%Y-%m-%d")

    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={api_key}&pageSize={num_articles}" # change your parameters here. Like you can add &sortBy=Relevancy or Popularity or something else. Also the &from=from_date and &to=to_date could be useful to condense results from the API
    response = requests.get(url)
    data = response.json()

    with open(output_file, "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    # api_key = "7fb5552822664ed99f0896a7d7ba4db3" # simone key
    # api_key = "0796996332df4a1db198bf821505a8d7" # xlrdm key
    api_key = "3be484841b8846cea7d3c9c6d1f117de" # gandolph key
    keyword = "Taylor Swift"
    num_articles = 100 # this is the limit of the free tier of this API

    timestamp = time.strftime("%Y%m%d%H%M%S")
    output_file = f"./tswift_articles_{timestamp}.json"


    download_articles(api_key, keyword, num_articles, output_file) #run the API query
