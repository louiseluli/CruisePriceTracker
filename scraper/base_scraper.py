# scraper/base_scraper.py

from abc import ABC, abstractmethod

class BaseScraper(ABC):
    """
    Abstract base class for all cruise line scrapers.

    This class defines the common interface (a contract) that every specific
    scraper must follow. This ensures that the main application can interact
    with any scraper in a consistent way.
    """

    def __init__(self, cruise_line_name):
        """
        Initializes the scraper with the name of the cruise line.
        
        Args:
            cruise_line_name (str): The name of the cruise line (e.g., 'MSC').
        """
        self.cruise_line_name = cruise_line_name
        print(f" scraper for {self.cruise_line_name} initialized.")

    @abstractmethod
    def scrape(self):
        """
        The main method to orchestrate the scraping process for a cruise line.
        
        This method should handle fetching the data, parsing it, and returning
        a structured format.
        """
        raise NotImplementedError("The 'scrape' method must be implemented by subclasses.")

    @abstractmethod
    def _fetch_page(self, url):
        """
        Fetches the HTML content of a single page.
        
        Args:
            url (str): The URL of the page to fetch.
        
        Returns:
            str: The HTML content of the page, or None if the request fails.
        """
        raise NotImplementedError("The '_fetch_page' method must be implemented by subclasses.")

    @abstractmethod
    def _parse_data(self, html_content):
        """
        Parses the HTML content to extract cruise information.
        
        Args:
            html_content (str): The HTML content of a search results page.
            
        Returns:
            list: A list of dictionaries, where each dictionary represents a cruise.
        """
        raise NotImplementedError("The '_parse_data' method must be implemented by subclasses.")