# main.py

"""
Main entry point for the Cruise Price Tracker application.

This script will orchestrate the different components of the application:
1. Trigger the web scrapers to collect cruise data.
2. Store the collected data in the database.
3. Perform analysis on the data to find deals.
4. Send alerts based on user-defined criteria.
"""
from scraper.msc_scraper import MSCScraper


def run_scraper():
    """
    Function to run the web scraping process.
    """
    print("🚀 Starting the scraping process...")
    
    # Initialize and run our new MSC scraper
    msc_scraper = MSCScraper()
    msc_cruises = msc_scraper.scrape()

    # Print the results to the console
    print("\n--- SCRAPED DATA ---")
    if msc_cruises:
        for cruise in msc_cruises:
            print(cruise)
    else:
        print("No data was scraped.")
    print("--------------------\n")

    print("✅ Scraping process finished.")

def run_analysis():
    """
    Placeholder function to run the data analysis.
    """
    print("📊 Starting data analysis...")
    # This will eventually generate graphs and identify best deals
    print("✅ Analysis complete.")


def send_alerts():
    """
    Placeholder function to send alerts.
    """
    print("📧 Sending alerts for best deals...")
    # This will check for price drops and notify the user
    print("✅ Alerts have been sent.")


def main():
    """
    Main function to orchestrate the application workflow.
    """
    print("--- Cruise Price Tracker Initialized ---")
    run_scraper()
    run_analysis()
    send_alerts()
    print("--- Application run concluded ---")


if __name__ == "__main__":
    # This ensures the main() function is called only when the script is executed directly
    main()