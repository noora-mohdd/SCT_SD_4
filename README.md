# Book Catalog Scraper

A Python project that scrapes book data (title, price, availability, and rating) from [Books to Scrape](https://books.toscrape.com/) and saves it to a CSV file.

---

## Features

- Extracts book titles, prices, availability status, and star ratings  
- Saves the data into a neat CSV file  
- Also saves a copy of the HTML for reference  

---

## Tools Used

- `requests` — to fetch the website’s HTML  
- `re` (regular expressions) — to extract info from the HTML  
- `csv` — to save the data in a structured format  

---

## How It Works

1. Sends a request to the website and downloads the HTML  
2. Uses regular expressions to extract:
   - Book titles  
   - Prices  
   - Availability status  
   - Star ratings  
3. Saves the data into:
   - `output.csv` – structured book data  
   - `book-scraper.html` – saved copy of the full HTML page  

---

## File Details

### `book-catalog-scraper.py`

This is the main Python script that:

- Sends a request to the website  
- Uses regular expressions to extract book data  
- Writes the results into a CSV file  

### `book-scraper.html`

The saved HTML code of the webpage that was scraped.  
This helps users understand where the data was pulled from and inspect the structure of the page.

### `output.csv`

A CSV file that stores the scraped data in a structured format,  
with columns for **Title**, **Price**, **Availability**, and **Rating**.


