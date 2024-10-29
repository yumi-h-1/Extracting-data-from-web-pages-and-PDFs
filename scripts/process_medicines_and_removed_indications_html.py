# Function to find the removed indication in HTML using the query
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'DNT': '1',
    'Connection': 'keep-alive'
}

def process_medicines_and_removed_indications_html(variation_urls):
    removed_indications_dict = {}  # Dictionary to store indications for each URL

    # Loop over each URL
    for variation_url in variation_urls:
        try:
            response = requests.get(variation_url, headers=headers, timeout=(3.05, 27))
            response.encoding = 'utf-8'
            soup = BeautifulSoup(response.text, 'html.parser')
            html_content = soup.prettify()

            # Query the model with the individual HTML content
            removed_indications = query_model_for_removed_indication_html(html_content)

            # Store the indication in the dictionary with the URL as its key
            removed_indications_dict[variation_url] = removed_indications

        except Exception as e:
            print(f"Error processing {epar_url}: {e}")
            removed_indications_dict[variation_url] = "Error fetching or processing the page"

    return removed_indications_dict