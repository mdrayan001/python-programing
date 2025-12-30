import requests # pip install requests
"""
News API Article Fetcher
This module fetches and displays news articles based on user-specified queries
using the NewsAPI service. It allows users to search for news topics of interest
and displays the article titles and URLs in a formatted manner.
Requirements:
    - requests library (install via: pip install requests)
    - Valid NewsAPI key from https://newsapi.org/
Example:
    User is prompted to enter a news topic, then the script fetches the latest
    articles matching that topic and displays them with their titles and URLs.
"""
import requests  # pip install requests
# Prompt user to enter the type of news they're interested in
# API key for NewsAPI authentication (obtain from https://newsapi.org/)
# Construct the API endpoint URL with query parameters
# q: search query
# from: start date for articles (YYYY-MM-DD format)
# sortBy: sort articles by publication date (newest first)
# apiKey: authentication key for the API
# Display the constructed URL for debugging purposes
# Send GET request to the NewsAPI endpoint and store the response
r = requests.get(url)
# Parse the JSON response into a Python dictionary
# Extract the list of articles from the response data
# Iterate through each article and display its information
# enumerate() provides both index and article object
    # Display article number (1-indexed), title, and URL
    # Print separator line for better readability

query = input("What type of news are you interested in today? ")
api = "5fb0689a16dc40e192c7d98cc6271761"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-11-30&sortBy=publishedAt&apiKey={api}"

print(f'url: {url}')
print("\n")
r =  requests.get(url)

data = r.json()

articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"], article["url"])
    print("\n****************************************\n")
