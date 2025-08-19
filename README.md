# Cruise Price Tracker

## 🚢 About the Project

This project is a Python-based application designed to track the prices of cruises from various cruise lines and websites. It automatically scrapes pricing data, stores it, analyzes price evolution, and provides insights and alerts to help find the best deals.

## ✨ Key Features

- **Automated Scraping:** Periodically fetches cruise data (prices, itineraries, dates) from specified cruise line websites.
- **Price History:** Stores historical price data to track the evolution of cruise fares over time.
- **Data Visualization:** Generates graphs and charts to visualize price trends.
- **Smart Alerts:** Notifies the user when a price drops or a good deal is found based on predefined criteria.
- **Custom Search:** Allows users to search for cruises based on specific filters like budget, duration, and travel dates.
- **Predictive Analysis (Future Goal):** Implement a machine learning model to predict future price fluctuations.

## 🛠️ Tech Stack

- **Language:** Python
- **Data Scraping:** BeautifulSoup, Scrapy (or similar)
- **Data Storage:** SQLite (initially), PostgreSQL (for scalability)
- **Data Analysis & Visualization:** Pandas, Matplotlib, Seaborn
- **Automation:** GitHub Actions or a system scheduler (like cron).
