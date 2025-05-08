import cloudscraper
from bs4 import BeautifulSoup
import pandas as pd

# Connect to website that you want to scrape
URL = 'https://www.thewhiskyexchange.com/c/35/japanese-whisky'

scraper = cloudscraper.create_scraper(
    browser={
      "custom": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/114.0.0.0 Safari/537.36"
    }
)
page = scraper.get(URL)

print('It is working', page.status_code)

soup = BeautifulSoup(page.content, "lxml")  #pulls the content

productName = soup.find_all('li', class_='product-grid__item') #gets the specfic content I want

print('There are', len(productName), 'items on the FIRST page')

print('For each of the 24 items, these are the names:')

for position, item in enumerate(productName, 1):
    name_tag = item.find("p", class_="product-card__name")
    if name_tag:
        # .get_text(strip=True) returns the text without any HTML tags or extra whitespace
        print(f"{position}. {name_tag.get_text(strip=True)}")


productPrice = soup.find_all('p', class_='product-card__price')#gets the price of all
# the products

print('The price for each product:')
for position, tag in enumerate(productPrice, 1):
    # .get_text(strip=True) removes HTML and extra whitespace
    print(f"{position}. {tag.get_text(strip=True)}")

unit_prices = soup.find_all('p', class_='product-card__unit-price')

print('Unit price for each product:')
for position, up in enumerate(unit_prices, 1):
    # up.get_text(strip=True) → "(£49.29 per litre)"
    text = up.get_text(strip=True).strip('()')
    # now text == "£49.29 per litre"
    print(f"{position}. {text}")

data = {
    'name': [
        "Hakushu Distiller's Reserve",
        "Hibiki Harmony",
        "Yamazaki 12 Year Old",
        "Yamazaki 18 Year Old Gift Box",
        "Hibiki 17 Year Old Whisky",
        "Hibiki 21 Year Old",
        "Nikka Coffey Grain Whisky",
        "The Chita Distiller's Reserve",
        "Chichibu On the Way Bot.2024",
        "Suntory Toki",
        "Yamazaki Distiller's Reserve",
        "Chichibu 2015 9 Year Old Cask #4415 Berry Bros & Rudd Exceptional Cask",
        "Fuji Single Malt Whisky",
        "Ichiro's Malt Double Distilleries (46.5%)",
        "Yoichi Single Malt",
        "Kanosuke Single Malt",
        "Kaiyo Mizunara Oak",
        "Onikishi Cherry Blossom Japanese Blended Whisky",
        "Togouchi Single Malt",
        "The House of Suntory Triology Pack 3x20cl",
        "Fuji Single Blended Whisky",
        "Chichibu London Edition 2024",
        "Hibiki Harmony 100th Anniversary",
        "Akashi Blended Sherry Cask Finish"
    ],
    'price': [
        "£58.75",
        "£82.25",
        "£139",
        "£600",
        "£795",
        "£795",
        "£60.25",
        "£50.50",
        "£275",
        "£34.50",
        "£80.95",
        "£550",
        "£71.75",
        "£99.95",
        "£77.25",
        "£89.95",
        "£79.75",
        "£53.50",
        "£65.50",
        "£49.25",
        "£58.75",
        "£350",
        "£345",
        "£38.25"
    ],
    'litre': [
        "£83.93 per litre",
        "£117.50 per litre",
        "£198.57 per litre",
        "£857.14 per litre",
        "£1,135.71 per litre",
        "£1,135.71 per litre",
        "£86.07 per litre",
        "£72.14 per litre",
        "£392.86 per litre",
        "£49.29 per litre",
        "£115.64 per litre",
        "£785.71 per litre",
        "£102.50 per litre",
        "£142.79 per litre",
        "£110.36 per litre",
        "£128.50 per litre",
        "£113.93 per litre",
        "£76.43 per litre",
        "£93.57 per litre",
        "£82.08 per litre",
        "£83.93 per litre",
        "£500 per litre",
        "£492.86 per litre",
        "£76.50 per litre"
    ]
}

df = pd.DataFrame(data)

#allow unlimited columns and a wide display
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

print(df[["name", "price", "litre"]])

#use r to make it work, or you can just change each \ to a \\ and it will work
df.to_excel(r"C:\Users\mahru\Desktop\Whiskey_data.xlsx", index=False)







