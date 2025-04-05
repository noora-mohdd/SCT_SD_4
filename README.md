# Skillcraft Technology Internship – Task 4: E-commerce Data Scraper
  
This repository contains **Task 4** assigned during my internship as a **Software Development Intern** at **Skillcraft Technology**.

This task focuses on enhancing my programming, problem-solving, and software development skills through a real-world coding challenge: building a **E-commerce Data Scraper** in Python.

---

##  Task 4: Book Catalog Scraper

A Python project that scrapes book data (title, price, availability, and rating) from [Books to Scrape](https://books.toscrape.com/) and saves it to a CSV file.
> **Note:** This project uses only core Python libraries.  
> No **BeautifulSoup** or **pandas** were used — everything was done using `requests`, `re`, and `csv`.
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


