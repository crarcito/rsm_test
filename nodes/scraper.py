import requests
from bs4 import BeautifulSoup


def scrape_node(state):
    """ This function fetches the HTML content of the given URL and extracts text from it.
    It updates the state with the scraped text."""

    #     loader = WebBaseLoader(urls)
    #     docs = loader.load()

    # Ensure the state has a URL to scrape
    url = state["url"]
    if not url:
        raise ValueError("No URL provided for scraping.")
    # Validate the URL format
    if not url.startswith("http://") and not url.startswith("https://"):
        raise ValueError("Invalid URL format. URL must start with 'http://' or 'https://'.")
    
    # Use requests to fetch the content of the URL
    html = requests.get(url).text

    # Parse the HTML content using BeautifulSoup
    # and extract the text content.
    soup = BeautifulSoup(html, "html.parser")

    # Extract text from the soup object
    text = soup.get_text()

    # Update the state with the scraped text
    state["text"] = text
    return state