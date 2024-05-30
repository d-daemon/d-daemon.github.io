import csv
import requests
from bs4 import BeautifulSoup

def get_brand_website(brand):
    url = f"https://www.google.com.hk/search?q={brand}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    search_results = soup.find_all('a')
    for result in search_results:
        if result.get('href').startswith('http'):
            return result.get('href')
    return None

def main():
    brands = []
    with open('brands.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            brands.extend(row)

    brand_websites = {}
    for brand in brands:
        website = get_brand_website(brand)
        brand_websites[brand] = website

    with open('brand_websites.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Brand', 'Website'])
        for brand, website in brand_websites.items():
            writer.writerow([brand, website])

if __name__ == "__main__":
    main()