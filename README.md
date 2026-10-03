# Cryptocurrency Price Tracker

## 1. Project Overview

Cryptocurrency Price Tracker is a Python-based web scraping application
that collects real-time cryptocurrency information using Selenium.

The application collects:

- Cryptocurrency Name
- Symbol
- Current Price
- 24-hour Change
- Market Capitalization
- Timestamp

The project also stores historical cryptocurrency data and provides
price trend analysis using graphs.

---

## 2. Objective

The main objective of this project is to develop an automated
cryptocurrency monitoring system that can collect live cryptocurrency
prices and store the information for further analysis.

---

## 3. Features

### Real-Time Price Scraping

The system automatically collects cryptocurrency information
from CoinPaprika using Selenium.

### Top 10 Cryptocurrencies

The application extracts the top 10 cryptocurrencies displayed
on the website.

### Automatic Monitoring

The system automatically updates cryptocurrency information
every 60 seconds.

### CSV Export

The latest cryptocurrency data is stored in:

data/crypto_data.csv

### Historical Data Logging

Historical cryptocurrency data is continuously stored in:

data/crypto_history.csv

### Price Filter

Users can enter a minimum price and find cryptocurrencies
above the specified price.

### 24-Hour Change Filter

Users can enter a minimum 24-hour percentage change and
filter cryptocurrencies based on the change.

### Trend Analysis

Historical cryptocurrency prices are analyzed to calculate:

- First Price
- Latest Price
- Price Change
- Percentage Change
- Trend

The trend is displayed as:

UP
DOWN
NO CHANGE

### Price Trend Graph

The application generates a graph showing the historical
price movement of the selected cryptocurrency.

---

## 4. Technologies Used

- Python
- Selenium
- Pandas
- Matplotlib
- WebDriver Manager
- Google Chrome
- CSV

---

## 5. Project Structure

cryptocurrency_price_tracer/
│
├── data/
│   ├── crypto_data.csv
│   └── crypto_history.csv
│
├── venv/
│
├── config.py
├── main.py
├── scraper.py
├── trend_analysis.py
├── requirement.txt
└── README.md

---

## 6. File Description

### config.py

Contains project configuration such as:

- Cryptocurrency website URL
- Number of cryptocurrencies
- Headless browser setting
- CSV file path

### scraper.py

Uses Selenium to open the cryptocurrency website
and extract cryptocurrency information.

### main.py

Controls the main cryptocurrency monitoring system.

It:

- Scrapes cryptocurrency data
- Creates DataFrame
- Saves CSV files
- Applies filters
- Adds timestamps
- Runs automatic monitoring

### trend_analysis.py

Reads historical cryptocurrency data and performs:

- Cryptocurrency selection
- Price history display
- Trend calculation
- Percentage change calculation
- Price trend graph

---

## 7. Installation

Create and activate a Python virtual environment.

Install the required packages using:

pip install -r requirement.txt

Required packages:

- selenium
- pandas
- webdriver-manager
- matplotlib

---

## 8. How to Run

### Step 1

Activate the virtual environment.

### Step 2

Run the main cryptocurrency tracker:

python main.py

### Step 3

Enter the required filter values.

Example:

Minimum 24h Change:

0

Minimum Price:

100

### Step 4

The application automatically collects cryptocurrency
information every 60 seconds.

Press:

Ctrl + C

to stop monitoring.

---

## 9. Trend Analysis

Run:

python trend_analysis.py

Select a cryptocurrency from the available list.

Example:

1. Bitcoin
2. Ethereum
3. Tether
4. BNB
5. XRP

The application displays the historical price data and
generates a price trend graph.

---

## 10. Output

The application provides:

- Top 10 cryptocurrency prices
- 24-hour price changes
- Market capitalization
- CSV files
- Historical data
- Price filters
- 24-hour change filters
- Trend analysis
- Price trend graphs

---

## 11. Future Enhancements

The project can be extended with:

- Email price alerts
- Telegram notifications
- Web dashboard
- Portfolio tracking
- Advanced trend prediction
- Machine learning-based price prediction
- Interactive charts
- Custom cryptocurrency selection

---

## 12. Conclusion

The Cryptocurrency Price Tracker provides an automated
solution for collecting and analyzing cryptocurrency data.

The project demonstrates the use of Selenium for web scraping,
Pandas for data processing, CSV files for historical storage,
and Matplotlib for price trend visualization.