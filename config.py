# config.py

"""
Configuration file for the Cruise Price Tracker.

This file contains all the settings and parameters for the application,
such as target websites, search criteria, and database settings.
"""

# --- SCRAPER SETTINGS ---

# List of cruise line websites to scrape.
# We will need to find the specific search URLs for each.
# This is a starting point.
TARGET_URLS = {
    "MSC_BR": "https://www.msccruzeiros.com.br/",
    "MSC_USA": "https://www.msccruisesusa.com/",
    "Carnival": "https://www.carnival.com/",
    "RoyalCaribbean": "https://www.royalcaribbean.com/",
    "Costa": "https://www.costacruises.com/",
    "Princess": "https://www.princess.com/",
}


# --- SEARCH PARAMETERS ---

# User-defined search criteria for finding ideal cruises.
SEARCH_CRITERIA = {
    "MIN_NIGHTS": 20,
    "MAX_PRICE_USD": 2000,
    "DEPARTURE_MONTHS": ["July", "August"],
    "DEPARTURE_YEAR": 2026,
    "REGIONS": ["Transatlantic", "Africa", "Asia", "South America", "Europe"],
    "DEPARTS_OR_ARRIVES_BRAZIL": True,
}


# --- DATABASE SETTINGS ---

# The name of the SQLite database file.
# It will be created in the 'database' directory.
DATABASE_NAME = "cruise_data.db"


# --- ALERTER SETTINGS ---

# Email settings for sending price alerts.
# (We will use this later for notifications)
ALERT_EMAIL_RECIPIENT = "your_email@example.com"


# --- GENERAL SETTINGS ---

# Define the user agent to mimic a real web browser
# to avoid being blocked by websites.
HTTP_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
}