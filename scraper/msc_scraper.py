# scraper/msc_scraper.py

import time
import random
import requests
from bs4 import BeautifulSoup
from scraper.base_scraper import BaseScraper
from config import HTTP_HEADERS, TARGET_URLS

class MSCScraper(BaseScraper):
    """
    A scraper for MSC Cruises.

    This class is responsible for scraping cruise data from the MSC website,
    handling requests, parsing HTML, and structuring the data.
    """

    def __init__(self):
        """Initializes the MSCScraper."""
        super().__init__("MSC")
        # We'll start by targeting the MSC Brazil URL from our config.
        self.url = TARGET_URLS.get("MSC_BR")

    def _fetch_page(self, url):
        """
        Fetches the HTML content of a page with intelligent delays.

        This method mimics human behavior by:
        1. Using a realistic User-Agent.
        2. Introducing a randomized delay before each request to avoid
           overwhelming the server.

        Args:
            url (str): The URL of the page to fetch.

        Returns:
            str: The HTML content of the page, or None if the request fails.
        """
        print(f"Fetching URL: {url}...")
        try:
            # Introduce a randomized delay to be a "nice" scraper
            # This makes our requests less predictable.
            sleep_time = random.uniform(2.5, 5.5)
            print(f"Waiting for {sleep_time:.2f} seconds...")
            time.sleep(sleep_time)

            response = requests.get(url, headers=HTTP_HEADERS, timeout=15)
            # Raise an exception for bad status codes (4xx or 5xx)
            response.raise_for_status()
            print("Page fetched successfully.")
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching page {url}: {e}")
            return None

    def _parse_data(self, html_content):
        """
        Parses the HTML to extract cruise information.

        *** IMPORTANT NOTE ***
        This is the most crucial and fragile part of any scraper. The HTML
        structure of a website can change at any time, which would break
        this logic. The selectors used here ('div', 'class_', etc.) are
        placeholders and MUST be updated after inspecting the actual MSC
        website's live HTML source code.

        Returns:
            list: A list of dictionaries, each representing a cruise.
        """
        if not html_content:
            print("No HTML content to parse.")
            return []

        print("Parsing HTML content...")
        soup = BeautifulSoup(html_content, 'lxml')
        cruises = []

        # --- Placeholder Logic ---
        # The following is an EXAMPLE of how one might find cruise data.
        # You would need to use your browser's "Inspect Element" tool on the
        # MSC website to find the correct tags and classes for the elements
        # containing the cruise information.

        # Example: find all 'div' elements with a class that seems to hold cruise info.
        cruise_cards = soup.find_all('div', class_='cruise-card-item') # This class name is a guess

        for card in cruise_cards:
            try:
                # Find specific elements within the card by their tag and class.
                # Use .text.strip() to get the clean text content.
                ship_name = card.find('h3', class_='ship-name').text.strip()
                price = card.find('span', class_='price-value').text.strip()
                duration = card.find('span', class_='duration').text.strip()
                # ... and so on for itinerary, dates, ports, etc.

                cruise_data = {
                    'cruise_line': self.cruise_line_name,
                    'ship_name': ship_name,
                    'price': price,
                    'duration': duration,
                    'itinerary': "Placeholder Itinerary", # Placeholder
                    'departure_port': "Placeholder Port", # Placeholder
                    'departure_date': "Placeholder Date", # Placeholder
                }
                cruises.append(cruise_data)

            except AttributeError:
                # This handles cases where a card is missing some information.
                print("Skipping a card due to missing information.")
                continue
        
        # --- End of Placeholder Logic ---
        
        # For demonstration purposes, we will return a hardcoded list for now.
        # This allows us to test the rest of our application pipeline.
        print("Returning mock data as parsing logic is a placeholder.")
        mock_cruises = [
            {
                'cruise_line': self.cruise_line_name,
                'ship_name': 'MSC Grandiosa',
                'price': '$1899',
                'duration': '21 Nights',
                'itinerary': "Brazil to Italy (Transatlantic)",
                'departure_port': "Rio de Janeiro",
                'departure_date': "2026-07-15",
            },
            {
                'cruise_line': self.cruise_line_name,
                'ship_name': 'MSC Seaview',
                'price': '$1550',
                'duration': '24 Nights',
                'itinerary': "Brazil, South Africa, Mozambique",
                'departure_port': "Santos",
                'departure_date': "2026-08-02",
            }
        ]

        print(f"✅ Parsing complete. Found {len(mock_cruises)} mock cruises.")
        return mock_cruises


    def scrape(self):
        """
        Orchestrates the scraping process for MSC.
        """
        print(f"--- Starting scraper for {self.cruise_line_name} ---")
        if not self.url:
            print(f"❌ URL for {self.cruise_line_name} not found in config. Exiting.")
            return []
            
        # For a real scenario, we would construct a specific search URL
        # based on the criteria in config.py.
        # For now, we fetch the base URL.
        html = self._fetch_page(self.url)
        cruises = self._parse_data(html)
        print(f"--- Scraper for {self.cruise_line_name} finished ---")
        return cruises