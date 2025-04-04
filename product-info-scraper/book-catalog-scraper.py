import requests, re, csv

#get the raw HTML
url="https://books.toscrape.com/"
response = requests.get(url)
html=response.text

#save the HTML code into a file
with open("book-scraper.html", "w", encoding="utf-8") as file:
    file.write(html)

#extracting data
title=re.findall(r'<h3>.*?title="(.*?)".*?</h3>', html)
price=re.findall(r'<p class="price_color">Â£([0-9.]+)</p>', html)
in_stock=re.findall(r'<p class="instock availability">\s*<i.*?></i>\s*(.*?)\s*</p>', html)
raw_rating=re.findall(r'<p class="star-rating ([A-Za-z]+)">', html)

#saving to a CSV file
with open("output.csv", "w", newline="", encoding="utf-8") as file:
    writer=csv.writer(file)
    writer.writerow(["Title","Price","Availability","Rating"]) #first row

    for Title, Price, Availability, Rating in zip(title, price, in_stock, raw_rating):
        writer.writerow([Title, Price, Availability, Rating])

print(f"Titles: {len(title)}, Prices: {len(price)}, Availability: {len(in_stock)}, Ratings: {len(raw_rating)}")


