import requests
from bs4 import BeautifulSoup

def scrape_node(state):
    """ This function fetches the HTML content of the given URL and extracts text from it.
    It updates the state with the scraped text."""

    #     loader = WebBaseLoader(urls)
    #     docs = loader.load()

    # Ensure the state has a URL to scrape

    try:
        url = state["url"]
        if not url:
            raise ValueError("No URL provided for scraping.")
        
        # Validate the URL format
        if not url.startswith("http://") and not url.startswith("https://"):
            raise ValueError("Invalid URL format. URL must start with 'http://' or 'https://'.")
        
        # Use requests to fetch the content of the URL
        html = requests.get(url).text
        if not html:
            raise ValueError("No html provided for scraping.")
        # Parse the HTML content using BeautifulSoup
        # and extract the text content.
        soup = BeautifulSoup(html, "html.parser")
        if not html:
            raise ValueError("No soup provided for scraping.")

        # Extract text from the soup object
        text = soup.get_text()
        if not html:
            raise ValueError("No text provided for scraping.")
        
        # Update the state with the scraped text
        state["text"] = text
    except ValueError as ex:
        raise ex 
    
    return state