import requests
from bs4 import BeautifulSoup
import sys

# Define a function to scrape a webpage for relevant information
async def scrape_website(url, search_query):

    # Send an HTTP request to the webpage
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, "html.parser")

        # Search for relevant sections using the provided search query
        relevant_sections = []
        for paragraph in soup.find_all("p"):
            if search_query in paragraph.get_text():
                relevant_sections.append(paragraph.get_text())

        # Include the scraped information in your response
        scraped_info = "\n".join(relevant_sections)

        # Return the scraped information
        return scraped_info
    else:
        # unsuccessful. send back nothing, since gpt-2 will read this response as relevant data found
        return ""